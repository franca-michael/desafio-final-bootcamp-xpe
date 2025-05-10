import pandas as pd


def coluna_mes_ano(dataframe: pd.DataFrame, coluna: str):
    dict_mes = {
        'janeiro'   : 1,
        'fevereiro' : 2,
        'março'     : 3,
        'abril'     : 4,
        'maio'      : 5,
        'junho'     : 6,
        'julho'     : 7,
        'agosto'    : 8,
        'setembro'  : 9,
        'outubro'   : 10,
        'novembro'  : 11,
        'dezembro'  : 12 
        }

    # Divide a coluna 'Mês' em duas colunas: nome do mês e ano
    dataframe[['nome_mes', 'ano']] = dataframe[coluna].str.split(' ', expand=True)

    # Converte o nome do mês para número
    dataframe['mes'] = dataframe['nome_mes'].map(dict_mes)

    # Converte 'ano' para inteiro
    dataframe['ano'] = dataframe['ano'].astype(int)

    # Remove a coluna intermediária (opcional)
    dataframe.drop(columns=coluna, inplace=True)
    
    return dataframe.head()

###########################################################################################################################

def criar_coluna_data(df, coluna_ano='ano', coluna_mes='mes', nova_coluna='data_yyyy_mm'):
    """
    Cria uma nova coluna no formato yyyy-mm a partir das colunas de ano e mês.

    Parâmetros:
        df (pd.DataFrame): DataFrame contendo as colunas de ano e mês.
        coluna_ano (str): Nome da coluna com o ano (formato inteiro).
        coluna_mes (str): Nome da coluna com o mês (formato inteiro).
        nova_coluna (str): Nome da nova coluna a ser criada.
    """
    df[nova_coluna] = df.apply(
        lambda row: f"{int(row[coluna_ano])}-{int(row[coluna_mes]):02d}", axis=1
    )
    return df