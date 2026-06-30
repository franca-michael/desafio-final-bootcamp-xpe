# Análise de Consumo de Energia Elétrica no Brasil - Desafio Final Bootcamp XP

Repositório destinado ao desafio final do bootcamp de Data Science da XP Educação. Este projeto realiza uma análise exploratória e correlacional dos dados de consumo de energia elétrica no Brasil, integrando informações de consumo, localização regional e índices de inflação (IPCA).

---

## 📋 Objetivo do Projeto

O objetivo principal é **analisar o consumo de energia elétrica no Brasil ao longo dos anos**, compreendendo tendências, padrões regionais e o impacto de fatores econômicos. Especificamente:

1. **Entender as tendências de consumo**: Identificar como o consumo de energia evoluiu ao longo do tempo e quais fatores influenciam essas mudanças
2. **Identificar padrões regionais e temporais**: Analisar variações entre diferentes regiões (estados) e ao longo dos meses e anos
3. **Avaliar correlações econômicas**: Compreender a relação entre consumo de energia e inflação (IPCA) como indicador econômico

---

## 🎯 O que foi Feito

### 1. **Coleta de Dados**
   - Importação de dados de três fontes principais:
     - **Consumo de Energia**: Base com informações de consumo por estado e tipo de consumo
     - **Estados/Região**: Mapeamento de estados brasileiros com suas respectivas regiões
     - **IPCA/Inflação**: Índice Nacional de Preços ao Consumidor (dados do IBGE)

### 2. **Análise Exploratória de Dados (EDA)**
   - **Verificação de Qualidade**:
     - Identificação e exclusão de dados duplicados
     - Tratamento de dados ausentes (valores nulos)
     - Validação de tipos de dados
   - **Análise de Distribuição**:
     - Boxplots e histogramas para visualizar distribuições
     - Identificação de outliers
     - Estatísticas descritivas

### 3. **Integração de Bases de Dados**
   - Junção das bases usando operador `INNER JOIN`
   - Criação de coluna unificada de data (ano-mês)
   - Sincronização de períodos entre as diferentes fontes

### 4. **Análise Correlacional**
   - Teste de hipótese: correlação entre consumo de energia e inflação (IPCA)
   - Análise por região e tipo de consumo
   - Identificação de padrões sazonais

### 5. **Visualizações**
   - Gráficos de linha para tendências temporais
   - Mapas coroplético do Brasil mostrando consumo por estado
   - Análises segmentadas por tipo de consumo (Residencial, Comercial, Industrial, etc.)
   - Correlogramas para relações entre variáveis

---

## 🏗️ Estrutura do Projeto

```
desafio-final-bootcamp-xpe/
│
├── README.md                          # Este arquivo
├── requirements.txt                   # Dependências Python
│
├── data/                              # Dados do projeto
│   ├── raw/                           # Dados brutos (originais)
│   │   ├── consumo_energia_eletrica/
│   │   │   └── consumo_energia_eletrica.csv
│   │   ├── estado_regiao/
│   │   │   └── estado_regiao.csv
│   │   └── ipca_inflacao/
│   │       └── ipca_2004_2022.xlsx
│   │
│   └── processed/                     # Dados processados (gerados)
│
├── notebook/
│   └── desafio_final.ipynb            # Notebook principal com toda análise
│
└── src/                               # Código modularizado (módulos reutilizáveis)
    ├── data_colect/                   # Coleta e leitura de dados
    │   ├── read_csv.py                # Função para ler arquivos CSV
    │   ├── read_xlsx.py               # Função para ler arquivos Excel
    │   ├── juncao_inner.py            # Função para realizar INNER JOIN
    │   └── coluna_mes_ano.py          # Funções para manipulação de datas
    │
    ├── data_analysis/                 # Análise exploratória de dados
    │   ├── nulos.py                   # Funções para identificar/tratar dados nulos
    │   └── duplicated.py              # Funções para identificar/excluir duplicados
    │
    └── data_viz/                      # Visualizações e gráficos
        ├── config_viz.py              # Configurações gerais de visualização
        ├── distribuicao_viz.py        # Boxplots e histogramas
        └── graficos_analiticos.py     # Gráficos avançados (linha, mapas, etc.)
```

---

## 🔧 Abordagens e Tecnologias Utilizadas

### **Modularização**
- **Separação em módulos**: O código foi organizado em módulos temáticos dentro de `src/`:
  - `data_colect/`: Responsável pela leitura e carregamento de dados
  - `data_analysis/`: Ferramentas para análise exploratória
  - `data_viz/`: Funções de visualização reutilizáveis
- **Benefícios**: Reutilização de código, manutenção facilitada, testes mais simples

### **Jupyter Notebook**
- **Arquivo Principal**: `notebook/desafio_final.ipynb`
- **Estrutura**: O notebook está dividido em seções lógicas:
  1. Importações e configurações
  2. Coleta de dados
  3. Análise exploratória por dataset
  4. Integração de bases
  5. Análises correlacionais
  6. Visualizações e conclusões
- **Abordagem**: Combina documentação em Markdown com código executável para narrativa clara

### **Bibliotecas Principais**
- **Pandas**: Manipulação e análise de dados
- **Matplotlib & Seaborn**: Visualizações estáticas
- **GeoPandas**: Mapas coroplético do Brasil
- **NumPy**: Operações numéricas

### **Práticas de Dados**
- **Tratamento de Dados**: Exclusão de duplicatas e valores nulos conforme instruções
- **Exploração**: Análise de qualidade antes de qualquer transformação
- **Documentação**: Docstrings em funções explicando parâmetros e retornos

---

## 📊 Bases de Dados Utilizadas

### 1. **Consumo de Energia Elétrica**
Fonte: https://www.leandrolessa.com.br/datasets

| Coluna | Descrição |
|--------|-----------|
| Ano | Ano de referência |
| Mês | Mês de referência |
| Sigla UF | Estado (Unidade Federativa) |
| Tipo de Consumo | Classificação (Residencial, Comercial, Industrial, etc.) |
| Número de Consumidores | Total de consumidores por tipo e estado |
| Consumo (kWh) | Quantidade de energia consumida |

### 2. **Estados e Região**
Fonte: https://www.leandrolessa.com.br/datasets

Mapeamento entre estados brasileiros e suas regiões geográficas.

### 3. **IPCA - Índice Nacional de Preços ao Consumidor Amplo**
Fonte: https://sidra.ibge.gov.br/tabela/3065

Índice mensal de inflação do Brasil (2004-2022), utilizado para correlação com consumo de energia.

---

## 🚀 Como Usar o Projeto

### **Pré-requisitos**
- Python 3.8+
- Virtual Environment (venv)

### **Instalação**

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/desafio-final-bootcamp-xpe.git
   cd desafio-final-bootcamp-xpe
   ```

2. **Crie uma virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Ative a virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

### **Executar a Análise**

1. **Abra o Jupyter Notebook**
   ```bash
   jupyter notebook notebook/desafio_final.ipynb
   ```

2. **Execute as células** na ordem apresentada (de cima para baixo)

3. **Interprete os resultados** e visualizações geradas

---

## 📈 Principais Descobertas

- A análise exploratória revelou que os dados de consumo e número de consumidores não seguem distribuição normal, concentrando-se em faixas específicas com presença de outliers
- A integração das três bases permitiu análises multidimensionais envolvendo consumo, localização e contexto econômico
- Padrões regionais distintos foram identificados, com variações significativas entre estados

---

## 📝 Estrutura do Código - Exemplos

### Exemplo de Modularização: Leitura de CSV
```python
# Em src/data_colect/read_csv.py
import pandas as pd 

def leitura_arquivo_csv(path_arquivo, sep=';', encoding='utf-8'):
    return pd.read_csv(path_arquivo, sep=sep, encoding=encoding)

# No notebook
df_energia = r_csv.leitura_arquivo_csv(path_consumo_energia, sep=',')
```

### Exemplo de Análise: Detecção de Nulos
```python
# Em src/data_analysis/nulos.py
def percent_null(dataframe: pd.DataFrame, ascending=False):
    '''Exibe percentual de nulos por coluna'''
    df_missing = (
        dataframe.isna().sum()
        .to_frame('missing_count')
        .join((dataframe.isna().sum() / dataframe.shape[0])
              .to_frame('missing_pct'))
        .sort_values('missing_count', ascending=ascending))
    return df_missing.style.format('{:.2%}', subset=['missing_pct'])

# No notebook
percent_null(df_energia)
```

---

## 🔍 Fluxo de Análise no Notebook

1. **Setup**: Importação de módulos e configurações
2. **Coleta**: Leitura das 3 bases de dados
3. **EDA Individual**: Análise de cada dataset separadamente
   - Detecção de duplicatas
   - Análise de dados nulos
   - Distribuição e estatísticas
4. **Integração**: Junção das bases via INNER JOIN
5. **Análise Integrada**: Correlações e padrões multidimensionais
6. **Visualizações**: Gráficos e mapas para storytelling

---

## 📚 Conceitos Aplicados

- ✅ Análise Exploratória de Dados (EDA)
- ✅ Manipulação de dados com Pandas
- ✅ Tratamento de dados ausentes e duplicados
- ✅ Operações de banco de dados (INNER JOIN)
- ✅ Visualização de dados com Matplotlib, Seaborn e GeoPandas
- ✅ Análise correlacional
- ✅ Modularização e reutilização de código
- ✅ Documentação de código com docstrings
- ✅ Ambiente virtual e gestão de dependências

---

## 👨‍💻 Autor

Desenvolvido como atividade prática do **Bootcamp Data Science XP Educação**

---

## 📄 Licença

Este projeto é fornecido para fins educacionais.
