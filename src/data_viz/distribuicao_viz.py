import sys
sys.path.append('../')

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

from src.data_viz.config_viz import setup_viz, formatador_abreviado



def boxplot_histograma(dataframe : pd.DataFrame,  lista_colunas:list):
    '''
    Esta função exibe gráficos de boxplot e histograma, para visualizar a distribuição dos dados de um dataframe pandas
    e precisam ser necessariamente colunas numéricas não categóricas.
    
    Parâmetros:
        dataframe: Dataframe do pandas.
        lista_colunas: Lista de nomes das colunas numéricas não categóricas.
        
    Retorna:
        Visualização de distribuição de dados com boxplot e histograma da série de colunas colocadas na lista
    '''
    setup_viz()
    
   
    
    # Loop pelas colunas e geração dos gráficos
    for i in lista_colunas:
        print('\n')
        print('*' * 100)
        print(f"{'*' * 40} {i} {'*' * 40}")
        print('*' * 100)
        print('\n')

        f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, 
                                            gridspec_kw={"height_ratios": (.15, .85)},
                                            figsize=(10, 6))

        sns.boxplot(dataframe[i], orient="h", ax=ax_box)
        sns.histplot(data=dataframe, x=i, ax=ax_hist)

        # Remove label do boxplot
        ax_box.set(xlabel='')

        # Desativa notação científica
        ax_hist.ticklabel_format(style='plain', axis='x')

        # Aplica formatação personalizada
        ax_hist.xaxis.set_major_formatter(FuncFormatter(formatador_abreviado))
        ax_box.xaxis.set_major_formatter(FuncFormatter(formatador_abreviado))

        plt.tight_layout()
        plt.show()
