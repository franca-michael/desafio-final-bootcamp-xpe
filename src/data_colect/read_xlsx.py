import pandas as pd 

def leitura_arquivo_xlsx(path_arquivo):
    return pd.read_excel(path_arquivo)