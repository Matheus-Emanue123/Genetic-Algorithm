import math
import random

# Função para calcular a distância Euclidiana entre duas turbinas
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Função para calcular o impacto entre duas turbinas com base na distância
def impacto(x1, y1, x2, y2):
    d = distancia(x1, y1, x2, y2)
    if d == 0:
        return float('inf')  # Evitar divisão por zero
    return 1 / (d ** 2)

# Função para calcular o impacto total de um layout (somatório dos impactos)
def impacto_total(positions, matriz_interferencia):
    total_impacto = 0
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            total_impacto += matriz_interferencia[i][j]  # Impacto dado pela matriz de interferência
    return total_impacto

# Gerando população inicial com soluções aleatórias
def gerar_populacao(tamanho_populacao, num_turbinas, area_limite):
    populacao = []
    for _ in range(tamanho_populacao):
        # Gerando posições aleatórias para cada turbina
        positions = [(random.uniform(area_limite[0], area_limite[1]), random.uniform(area_limite[0], area_limite[1])) for _ in range(num_turbinas)]
        populacao.append(positions)
    return populacao

# Função de seleção por torneio
def selecionar_torneio(populacao, matriz_interferencia, tamanho_torneio=3):
    torneio = random.sample(populacao, tamanho_torneio)
    torneio.sort(key=lambda individuo: impacto_total(individuo, matriz_interferencia))  # Menor impacto = melhor
    return torneio[0]  # Retorna o melhor indivíduo  # Retorna o melhor indivíduo

# Função de cruzamento (crossover) entre dois pais
def cruzamento(pai1, pai2):
    ponto_corte = random.randint(1, len(pai1) - 1)
    filho = pai1[:ponto_corte] + pai2[ponto_corte:]
    return filho

# Função de mutação (pequena mudança aleatória nas posições)
def mutacao(individuo, area_limite, taxa_mutacao=0.1):
    if random.random() < taxa_mutacao:
        turbina = random.randint(0, len(individuo) - 1)
        novo_x = random.uniform(area_limite[0], area_limite[1])
        novo_y = random.uniform(area_limite[0], area_limite[1])
        individuo[turbina] = (novo_x, novo_y)
    return individuo

# Função do Algoritmo Genético
def algoritmo_genetico(num_turbinas, area_limite, tamanho_populacao=100, num_geracoes=500, taxa_mutacao=0.1, matriz_interferencia=None):
    # Gerando população inicial
    populacao = gerar_populacao(tamanho_populacao, num_turbinas, area_limite)
    
    # Evoluindo as gerações
    melhor_solucao = None
    melhor_impacto = float('inf')
    
    for geracao in range(num_geracoes):
        nova_populacao = []
        
        # Seleção, cruzamento e mutação
        for _ in range(tamanho_populacao // 2):
            pai1 = selecionar_torneio(populacao, matriz_interferencia)
            pai2 = selecionar_torneio(populacao, matriz_interferencia)
            
            filho1 = cruzamento(pai1, pai2)
            filho2 = cruzamento(pai2, pai1)
            
            filho1 = mutacao(filho1, area_limite, taxa_mutacao)
            filho2 = mutacao(filho2, area_limite, taxa_mutacao)
            
            nova_populacao.extend([filho1, filho2])
        
        populacao = nova_populacao
        
        # Avaliar as soluções da nova população
        for individuo in populacao:
            impacto_atual = impacto_total(individuo, matriz_interferencia)
            if impacto_atual < melhor_impacto:
                melhor_impacto = impacto_atual
                melhor_solucao = individuo
        
        # Exibir progresso
        if geracao % 50 == 0:
            print(f"Geração {geracao} - Impacto: {melhor_impacto}")
    
    return melhor_solucao

# Função para ler a matriz de interferência do arquivo
def ler_matriz_interferencia(arquivo):
    with open(arquivo, "r") as f:
        linhas = f.readlines()
        num_turbinas = int(linhas[0].strip())
        matriz_interferencia = []
        for i in range(1, num_turbinas + 1):
            linha = list(map(float, linhas[i].strip().split()))
            matriz_interferencia.append(linha)
    return num_turbinas, matriz_interferencia

# Função para escrever o layout no arquivo de saída
def salvar_layout(layout, arquivo_saida):
    with open(arquivo_saida, "w") as f:
        for i, (x, y) in enumerate(layout):
            f.write(f"Turbina {i+1}: (x={x:.2f}, y={y:.2f})\n")

# Parâmetros
arquivo_entrada = "input/matriz_interferencia.txt"  # Arquivo de entrada com a matriz de interferência
arquivo_saida = "output/layout_saida.txt"  # Arquivo de saída para o layout das turbinas
area_limite = (0, 100)  # Limites da área (x_min, x_max), (y_min, y_max)

# Ler a matriz de interferência do arquivo
num_turbinas, matriz_interferencia = ler_matriz_interferencia(arquivo_entrada)

# Rodar o Algoritmo Genético
melhor_layout = algoritmo_genetico(num_turbinas, area_limite, matriz_interferencia=matriz_interferencia)

# Exibir o melhor layout encontrado
salvar_layout(melhor_layout, arquivo_saida)

print("\nLayout salvo em:", arquivo_saida)
