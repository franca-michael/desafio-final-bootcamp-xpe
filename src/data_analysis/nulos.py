import pandas as pd
import matplotlib.pyplot as plt



###############################################################################################
def percent_null(dataframe : pd.DataFrame, ascending = False):
    '''
    Esta função exibe percentual de nulos por coluna de um dataframe pandas .
    
    Parâmetros:
        dataframe: Dataframe do pandas.
        ascending: False por padrão
        
    Retorna:
        Um novo dataframe com o percentual de nulos por coluna, ordenado do maior percentual para o menor.
    '''
    df_missing = (
                    dataframe.isna().sum()
                    .to_frame('missing_count')
                    .join((dataframe.isna().sum() / dataframe.shape[0]).to_frame('missing_pct'))
                    .sort_values('missing_count', ascending = ascending))

    return df_missing.style.format('{:.2%}', subset = ['missing_pct'])



###############################################################################################
def vis_null(dataframe:pd.DataFrame):
    '''
    Esta função exibe número de nulos por coluna um dataframe pandas em um gráfico de barras .
    
    Parâmetros:
        dataframe: Dataframe do pandas.
    
        
    Retorna:
        Retorna um gráfico de barras vertical com a quantidade de nulos por coluna.
    '''
    
    # variável para plotar em gráfico dados nulos
    dados_nulos = dataframe.isna().sum().to_frame().rename(columns={0:'Qtd_nulos'})

    #plotagem dados Nulos
    plt.figure(figsize=(10, 5))

    barras = plt.barh(
                      dados_nulos.index,
                      dados_nulos['Qtd_nulos'],
                      color='red',
                      alpha=0.50,
                      )

    plt.bar_label(barras, fontsize=10, fontweight='bold', color='black', padding= 5)
    plt.box(False)
    plt.xticks([])
    plt.tick_params(axis='y', length=0)
    plt.title('Quantidade de Nulos por Coluna', color='gray', fontsize=14, fontweight='bold')
    plt.show()
    
    
    
################################################################################################

def exclui_null(dataframe : pd.DataFrame):
    '''
    Esta função exclui a linha que contem dados nulos de um dataframe pandas.
    
    Parâmetros:
        dataframe: data frame do pandas .
        
    Retorna:
        Dataframe sem os dados nulos.
    '''
    dataframe.dropna(inplace = True)
    
    
###############################################################################################

def identifica_linhas_nulas(dataframe: pd.DataFrame):
    '''
    Esta função identifica os dados nulos em qualquer linha ou coluna.
    
    Parâmetros:
        dataframe: data frame do pandas .
        
    Retorna:
        Dataframe somente com as linhas que possuem algum dado nulos.
    '''
    
    filtro = dataframe.isna().any(axis = 1)
    return dataframe[filtro]
