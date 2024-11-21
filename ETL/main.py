#main
from etl.extract import load_data
from etl.transform import clean_data
from etl.load import load_to_sqlite
from scraping_multinacionais import main 

# Executa o scraping
main()

# Caminho do arquivo CSV
file_path = 'dataset/superstore.csv'

# Extração
df = load_data(file_path)

# Verificar se os dados foram carregados
if df is not None:
    print("Primeiras linhas do DataFrame carregado:\n", df.head())
    
    # Transformação
    result = clean_data(df)

    if isinstance(result, tuple) and len(result) == 4:
        fact_vendas, dim_cliente, dim_produto, dim_localidade = result
    else:
        raise ValueError("A função clean_data não retornou os DataFrames esperados.")
    
    # Carga
    load_to_sqlite(fact_vendas, dim_cliente, dim_produto, dim_localidade)
else:
    print("Erro: arquivo CSV não encontrado ou não pôde ser carregado.")
