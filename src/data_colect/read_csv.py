import pandas as pd 

def leitura_arquivo_csv(path_arquivo, sep = ';', encoding = 'utf-8'):
    return pd.read_csv(path_arquivo,sep = sep, encoding= encoding)