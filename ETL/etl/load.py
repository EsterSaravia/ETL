# load.py

import sqlite3

def load_to_sqlite(fact_vendas, dim_cliente, dim_produto, dim_localidade, db_name='superstore.db'):
    try:
        # Conectar ao banco de dados SQLite (se o arquivo não existir, ele será criado)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Criar a tabela `dim_cliente`
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS dim_cliente (
            customer_id TEXT PRIMARY KEY,
            customer_name TEXT,
            segment TEXT
        )
        ''')

        # Criar a tabela `dim_produto`
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS dim_produto (
            product_id TEXT PRIMARY KEY,
            product_name TEXT,
            category TEXT,
            sub_category TEXT
        )
        ''')

        # Criar a tabela `dim_localidade`
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS dim_localidade (
            ship_mode TEXT,
            state TEXT,
            country TEXT,
            region TEXT,
            PRIMARY KEY (ship_mode, state)
        )
        ''')

        # Criar a tabela `fact_vendas`
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS fact_vendas (
            order_id TEXT PRIMARY KEY,
            order_date DATE,
            ship_date DATE,
            customer_id TEXT,
            product_id TEXT,
            sales FLOAT,
            profit FLOAT,
            ship_mode TEXT,
            state TEXT,
            quantity INT,
            discount FLOAT,
            shipping_cost FLOAT,
            FOREIGN KEY(customer_id) REFERENCES dim_cliente(customer_id),
            FOREIGN KEY(product_id) REFERENCES dim_produto(product_id),
            FOREIGN KEY(ship_mode, state) REFERENCES dim_localidade(ship_mode, state)
        )
        ''')

        # Carregar dados nas tabelas
        dim_cliente.to_sql('dim_cliente', conn, if_exists='replace', index=False)
        dim_produto.to_sql('dim_produto', conn, if_exists='replace', index=False)
        dim_localidade.to_sql('dim_localidade', conn, if_exists='replace', index=False)
        fact_vendas.to_sql('fact_vendas', conn, if_exists='replace', index=False)

        # Commit das transações
        conn.commit()
        print("Dados carregados com sucesso no banco de dados SQLite.")
        
    except Exception as e:
        print(f"Erro ao carregar dados no SQLite: {e}")
    finally:
        conn.close()
