# transform.py
import pandas as pd

def clean_data(df):
    """
    Realiza a limpeza e transformação dos dados para criar tabelas de fatos e dimensões.
    
    Args:
        df (pd.DataFrame): DataFrame com os dados extraídos.
        
    Returns:
        tuple: DataFrames `fact_vendas`, `dim_cliente`, `dim_produto`, `dim_localidade`.
    """
    # Padronizar nomes das colunas
    df.columns = df.columns.str.lower().str.replace('_', ' ')

    # Remover colunas desnecessárias
    df = df.drop(columns=['row id', 'unknown'], errors='ignore')

    # Converter colunas de data
    df['order date'] = pd.to_datetime(df['order date'], errors='coerce')
    df['ship date'] = pd.to_datetime(df['ship date'], errors='coerce')

    # Remover duplicatas de `order_id` e `customer_id`
    df = df.drop_duplicates(subset=['order id', 'customer id'], keep='first')

    # Criar DataFrame `dim_cliente` sem duplicatas
    dim_cliente = df[['customer id', 'customer name', 'segment']].drop_duplicates().reset_index(drop=True)
    dim_cliente.columns = ['customer_id', 'customer_name', 'segment']

    # Criar DataFrame `dim_produto`
    dim_produto = df[['product id', 'product name', 'category', 'sub category']].drop_duplicates().reset_index(drop=True)
    dim_produto.columns = ['product_id', 'product_name', 'category', 'sub_category']

    # Criar DataFrame `dim_localidade`
    dim_localidade = df[['ship mode', 'state', 'country', 'region']].drop_duplicates().reset_index(drop=True)
    dim_localidade.columns = ['ship_mode', 'state', 'country', 'region']

    # Criar DataFrame `fact_vendas` com as colunas necessárias
    fact_vendas = df[['order id', 'order date', 'ship date', 'customer id', 'product id', 'sales', 'profit', 'ship mode', 'state', 'quantity', 'discount', 'shipping cost']].reset_index(drop=True)
    fact_vendas.columns = ['order_id', 'order_date', 'ship_date', 'customer_id', 'product_id', 'sales', 'profit', 'ship_mode', 'state', 'quantity', 'discount', 'shipping_cost']

    print("Dados transformados com sucesso.")
    return fact_vendas, dim_cliente, dim_produto, dim_localidade
