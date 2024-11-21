import sqlite3
import pandas as pd
from sqlalchemy import create_engine
import unicodedata

sqlite_db_path = "C:\\Users\\ester\\Downloads\\rota-etl\\superstore.db"
postgresql_db_url = "postgresql://postgres:1234@localhost:5432/postgres"

sqlite_conn = sqlite3.connect(sqlite_db_path)
sqlite_conn.text_factory = lambda x: x.decode('iso-8859-1', errors='replace')
postgres_engine = create_engine(postgresql_db_url, connect_args={"options": "-c client_encoding=UTF8"})

sqlite_cursor = sqlite_conn.cursor()
sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
sqlite_tables = [table[0] for table in sqlite_cursor.fetchall()]

for table_name in sqlite_tables:
    try:
        print(f"Processando a tabela: {table_name}")
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", sqlite_conn)

        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].apply(
                lambda x: unicodedata.normalize('NFKD', str(x)).encode('ascii', 'ignore').decode('utf-8') if isinstance(x, str) else x
            )
        
        df.to_sql(table_name, postgres_engine, index=False, if_exists="replace", method='multi')
        print(f"Tabela '{table_name}' migrada com sucesso.")
    except Exception as e:
        print(f"Erro ao migrar a tabela '{table_name}': {e}")

sqlite_conn.close()
postgres_engine.dispose()
print("Migração completa!")
