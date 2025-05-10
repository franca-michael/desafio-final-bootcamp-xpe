import pandas as pd

def verfica_duplicados(dados : pd.DataFrame):
    '''
    Esta função verifica a existência de dados duplicados em um dataframe pandas.
    
    Parâmetros:
        dados:dataframe pandas.
        
        
    Retorna:
        Uma mensage com o número de dados duplicados e um dataframe que identifica quais são os dados duplicados.
    
    '''
    print(f'Existem {dados.duplicated().sum()} duplicados neste dataset')
    filtro = dados.duplicated()
    return dados[filtro]




def exclui_duplicados(dados : pd.DataFrame):
    '''
    Esta função exclui dados duplicados em um dataframe pandas.
    
    Parâmetros:
        dados:dataframe pandas.
        
        
    Retorna:
        Modifica inplace o dataframe, com a exclusão dos dados duplicados.
    
    '''
    
    dados.drop_duplicates(inplace=True)