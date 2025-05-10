import sys
sys.path.append('../')


import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator
import pandas as pd
import geopandas as gpd
import seaborn as sns
import math



from src.data_viz.config_viz import setup_viz, formatador_abreviado



####################################################################################################################################

def grafico_linha(dataframe: pd.DataFrame, titulo: str, numero_linhas_plot: int, numero_colunas_plot: int):
    setup_viz()
    # Tamanho da figura com base no número de linhas
    fig, axes = plt.subplots(numero_linhas_plot, numero_colunas_plot, figsize=(16, 4 * numero_linhas_plot))
    
    # Garante que axes seja uma matriz mesmo com 1 subplot
    if numero_linhas_plot * numero_colunas_plot == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    # Plot de cada série em subplot separado
    for i, coluna in enumerate(dataframe.columns):
        if i >= len(axes):
            break
        dataframe[coluna].plot(ax=axes[i], title=coluna, linewidth=2)
        axes[i].set_facecolor('#e5e5e5')
        axes[i].ticklabel_format(style='plain', axis='y')
        axes[i].yaxis.set_major_formatter(FuncFormatter(formatador_abreviado))
        axes[i].xaxis.set_major_locator(MaxNLocator(integer=True))
        if len(dataframe.index) < 24:
            axes[i].set_xticks(dataframe.index)
            axes[i].tick_params(axis='x', rotation=60)
        else:
            pass

    # Fundo da figura
    fig.patch.set_facecolor('#f0f0f0')
    fig.suptitle(titulo, fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()
    
#########################################################################################################################################


    
def grafico_linhas_categorias(dataframe: pd.DataFrame, coluna_x : str , nome_coluna_categoria:str , coluna_valores: str, titulo: str):
   
   setup_viz()
   
   df_linhas = dataframe.pivot(index=coluna_x, columns = nome_coluna_categoria, values = coluna_valores).fillna(0)
   
   # Plot do gráfico de linhas
   fig, ax = plt.subplots(figsize=(12, 6))
   fig.patch.set_facecolor('#f0f0f0')   # fundo da figura
   ax.set_facecolor('#e5e5e5') 
   
   for coluna in df_linhas.columns:
       plt.plot(df_linhas.index, df_linhas[coluna], marker='o', linewidth=2, label=coluna)
       
      
   # Formatação
   plt.gca().yaxis.set_major_formatter(FuncFormatter(formatador_abreviado))
   plt.title(titulo)
   plt.xlabel(coluna_x)
   plt.ylabel(coluna_valores)
   plt.legend(title = nome_coluna_categoria)
   plt.grid(True, linestyle='--', alpha=0.5)
   plt.xticks(df_linhas.index) 
   plt.tight_layout()
   plt.show()   
   
   
############################################################################################################################   



def mapas_consumo_por_estado(dataframe: pd.DataFrame, titulo: str):
    # Carrega mapa dos estados do Brasil (GeoJSON online)
    url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    geo_estados = gpd.read_file(url)
    
    # Corrige a coluna para bater com o DataFrame
    geo_estados.rename(columns={'name': 'estado'}, inplace=True)

    
    # Junta os dados com a geometria
    mapa = geo_estados.merge(dataframe, on='estado', how='left')

    # Colunas a plotar
    colunas_plot = ['consumo_total', 'consumo_medio', 'consumo_std']
    titulos = ['Consumo Total', 'Consumo Médio', 'Desvio Padrão do Consumo']

    # Cria subplots
    fig, axes = plt.subplots(1, 3, figsize=(24, 8))
    fig.patch.set_facecolor('#f0f0f0')

    for i, col in enumerate(colunas_plot):
        ax = axes[i]
        mapa.plot(column=col, cmap='YlOrRd', linewidth=0.8, edgecolor='0.8', legend=False, ax=ax)

        # Rótulos com valores abreviados
        for idx, row in mapa.iterrows():
            if pd.notna(row[col]):
                valor_formatado = formatador_abreviado(row[col], None)
                ax.annotate(text=valor_formatado,
                            xy=(row['geometry'].centroid.x, row['geometry'].centroid.y),
                            ha='center', fontsize=9, color='black')

        ax.set_title(titulos[i])
        ax.axis('off')

    fig.suptitle(titulo, fontsize=18)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

############################################################################################################################




def plotar_barras_em_subplots(df, titulo:str, ncols:int=2, ):
    """
    Gera subplots de gráficos de barras verticais a partir de um DataFrame com índice categórico e colunas numéricas.
    Parâmetros:
        df (pd.DataFrame): DataFrame com índice categórico e colunas numéricas.
        titulo (str): Título geral da figura.
        ncols (int): Número de colunas de subplots (linhas são calculadas automaticamente).
        
    """
    n_metrics = len(df.columns)
    nrows = math.ceil(n_metrics / ncols)

    fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(6*ncols, 4*nrows))
    fig.suptitle(titulo, fontsize=16)
    axs = axs.flatten() if n_metrics > 1 else [axs]
    

    for idx, col in enumerate(df.columns):
        dados_ordenados = df[col].sort_values(ascending=False)
        ax = axs[idx]

        bars = ax.bar(dados_ordenados.index, dados_ordenados.values)
        ax.set_title(col.capitalize())
        ax.set_xticklabels(dados_ordenados.index, rotation=45, ha='right')
        
        
        # Desativa notação científica no eixo Y
        ax.ticklabel_format(style='plain', axis='y')
        ax.yaxis.set_major_formatter(FuncFormatter(formatador_abreviado))
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # Adiciona rótulos de dados nas barras
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + yval*0.01, 
                    formatador_abreviado(yval, None), 
                    ha='center', va='bottom', fontsize=9)

    for j in range(idx+1, len(axs)):
        fig.delaxes(axs[j])

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
    
    
#######################################################################################################################

def mapa_coropletico_brasil(dataframe: pd.DataFrame, coluna_cor: str, titulo: str, legenda: bool = True, exibir_rotulos: bool = True):
    """
    Gera um mapa coroplético do Brasil onde a intensidade da cor dos estados
    é determinada pelos valores de uma coluna específica do DataFrame.

    Args:
        dataframe (pd.DataFrame): DataFrame contendo os dados a serem plotados,
                                   com uma coluna de nomes de estados.
        coluna_cor (str): Nome da coluna do DataFrame cujos valores determinarão
                          a intensidade da cor dos estados.
        titulo (str): Título do mapa.
        legenda (bool, optional): Indica se a legenda deve ser exibida. Defaults to True.
        exibir_rotulos: Indica se os rótulos de dados devem ser exibidos
       
    """
    # Carrega mapa dos estados do Brasil (GeoJSON online)
    url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    geo_estados = gpd.read_file(url)

    # Corrige a coluna para bater com o DataFrame
    geo_estados.rename(columns={'name': 'estado'}, inplace=True)

    # Junta os dados com a geometria
    mapa_brasil = geo_estados.merge(dataframe, on='estado', how='left')

    # Cria a figura e os eixos
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    fig.patch.set_facecolor('#f0f0f0')

    # Plota o mapa coroplético
    mapa_brasil.plot(column=coluna_cor, cmap='YlOrRd', linewidth=0.8, edgecolor='0.8', legend=legenda, ax=ax) 
    
    # Adiciona os rótulos de dados
    if exibir_rotulos:
        for idx, row in mapa_brasil.iterrows():
            if pd.notna(row[coluna_cor]):
                valor_formatado = f'{row[coluna_cor]:.2f}'  # Formata o valor (opcional)
                ax.annotate(text=valor_formatado,
                            xy=(row['geometry'].centroid.x, row['geometry'].centroid.y),
                            ha='center', fontsize=8, color='black')

    # Adiciona o título
    ax.set_title(titulo, fontsize=16)

    # Remove os eixos
    ax.axis('off')

    plt.tight_layout()
    plt.show()
    
    
#######################################################################################################################################
def correlacao(df, titulo='Mapa de Correlação', cmap='coolwarm', annot=True, figsize=(10, 8)):
    """
    Gera um heatmap com a correlação entre variáveis numéricas de um DataFrame.

    Parâmetros:
        df (pd.DataFrame): DataFrame com os dados.
        titulo (str): Título do gráfico.
        cmap (str): Paleta de cores.
        annot (bool): Exibir valores de correlação nas células.
        figsize (tuple): Tamanho da figura.
    """
    # Seleciona apenas colunas numéricas
    df_numerico = df.select_dtypes(include='number')
    
    # Calcula a matriz de correlação
    matriz_corr = df_numerico.corr()

    # Cria o gráfico
    plt.figure(figsize=figsize)
    sns.heatmap(matriz_corr, annot=annot, fmt=".2f", cmap=cmap, square=True, cbar_kws={"shrink": .8}, vmax=1,vmin=-1)
    plt.title(titulo, fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()