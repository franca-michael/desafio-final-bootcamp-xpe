import pandas as pd

def juncao_inner(dataframe_1: pd.DataFrame, dataframe_2: pd.DataFrame, chave_1: str, chave_2: str, lista_colunas_df_2 : list ):
    
    '''
    Esta função junta dois dataframes pandas somente onde as chaves são existentes nas duas bases.
    
    Parâmetros:
        dataframe_1: Primeiro dataframe a ser unido.
        dataframe_2: Segundo dataframe a ser unido.
        chave_1: chave de identificação do primeiro dataframe.
        chave_2: chave de identificaçã do segundo dataframe.
        lista_colunas_df2 : lista de colunas para serem relacionadas do segundo dataset
        
        
    Retorna:
        retorna um dataframe pandas com a junção de dois dataframes no formato inner.
    
    '''
    return pd.merge(left= dataframe_1, right= dataframe_2[lista_colunas_df_2], left_on = chave_1, right_on = dataframe_2[chave_2], how= 'inner' )