# extract.py
import pandas as pd

def load_data(file_path):
    """
    Carrega o arquivo CSV em um DataFrame pandas.
    
    Args:
        file_path (str): Caminho para o arquivo CSV.
        
    Returns:
        pd.DataFrame: DataFrame contendo os dados do CSV.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Dados carregados com sucesso do arquivo: {file_path}")
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None
