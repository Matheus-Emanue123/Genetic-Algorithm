<div align="center">
    <img src="/logo.png" width="200" height="200">

# 🪐 Meta-Heurística Algoritmo Genético na Otimização de Fazendas Eólicas 🪐
</div>

---

## 🌌 Visão Geral

Este projeto implementa um Algoritmo Genético para otimizar a disposição de turbinas eólicas em uma determinada área, minimizando o impacto de interferência entre elas.

---

## 🧠 Como Funciona

1. **Inicialização**: Geração de uma população aleatória de layouts possíveis.
2. **Avaliação**: Cada layout é avaliado com base no impacto total entre turbinas.
3. **Seleção**: Indivíduos com menor impacto são selecionados por torneio.
4. **Cruzamento e Mutação**: Geração de novas soluções através de recombinação e perturbações aleatórias.
5. **Iteração**: Repetição do processo por várias gerações até encontrar a melhor solução.

---

## 📁 Estrutura de Arquivos

```
📂 genetic-algorithm-turbines
├── 📂 input/
│   └── matriz_interferencia.txt     # Matriz de interferência entre turbinas
├── 📂 output/
│   └── layout_saida.txt             # Melhor layout encontrado
├── main.py                          # Código-fonte do algoritmo genético
└── README.md                        # Este arquivo
```

---

## 📥 Entrada

O arquivo `matriz_interferencia.txt` deve conter:

```
<número de turbinas>
<linha 1 da matriz>
<linha 2 da matriz>
...
```

**Exemplo**:

```
3
0.0 0.1 0.2
0.1 0.0 0.3
0.2 0.3 0.0
```

---

## 📤 Saída

O arquivo `layout_saida.txt` conterá as coordenadas ideais de cada turbina, como:

```
Turbina 1: (x=10.23, y=55.67)
Turbina 2: (x=88.12, y=12.45)
...
```

---

## 🚀 Executando o Projeto

### ✔ Pré-requisitos

- Python 3.x

### ▶ Rodando

```bash
python main.py
```

Ao fim da execução, o layout ótimo será salvo em `output/layout_saida.txt`.

### ⚙ Parâmetros Personalizáveis

No arquivo `main.py`:

- `area_limite = (0, 100)` — Define os limites do terreno onde turbinas podem ser colocadas.
- `tamanho_populacao = 100` — Tamanho da população em cada geração.
- `num_geracoes = 500` — Número de gerações do algoritmo.
- `taxa_mutacao = 0.1` — Probabilidade de mutação para cada indivíduo.

---

## 🧪 Exemplo de Uso

```
Geração 0 - Impacto: 0.01238
Geração 50 - Impacto: 0.00457
Geração 100 - Impacto: 0.00211
...
Layout salvo em: output/layout_saida.txt
```

---

## 🛠️ Autores

- **Matheus Emanuel da Silva** - Engenharia de Computação - CEFET-MG
- **João Francisco Teles da Silva** - Engenharia de Computação - CEFET-MG

---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

