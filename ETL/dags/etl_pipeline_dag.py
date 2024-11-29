# etl_pipeline_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging
from etl.extract import load_data
from etl.transform import clean_data

from etl.load import load_to_sqlite

# Configurações gerais do DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Funções específicas
def executar_etl_completo():
    """Executa o pipeline completo do ETL."""
    try:
        from main import pipeline_completo  # Certifique-se de que `pipeline_completo` está no `main.py`
        pipeline_completo()
        logging.info("Pipeline ETL completo executado com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao executar o pipeline completo: {e}")
        raise

def atualizar_dim_produto():
    """Atualiza a dimensão de produto."""
    try:
        # Carregar dados
        df = load_data('dataset/superstore.csv')
        _, _, dim_produto, _ = clean_data(df)

        # Carga
        load_to_sqlite(dim_produto=dim_produto)
        logging.info("Atualização da dimensão de produto concluída.")
    except Exception as e:
        logging.error(f"Erro ao atualizar dimensão de produto: {e}")
        raise

# Criação do DAG
with DAG(
    dag_id='etl_superstore_pipeline',
    default_args=default_args,
    description='Pipeline ETL para atualizar tabelas fato e dimensão',
    schedule_interval='@daily',  # Ajuste conforme necessidade @weekly ou cron
    start_date=datetime(2024, 11, 28),
    catchup=False,
) as dag:

    # Tarefa para executar o ETL completo
    tarefa_etl_completo = PythonOperator(
        task_id='executar_etl_completo',
        python_callable=executar_etl_completo,
        execution_timeout=timedelta(minutes=30),
    )

    # Tarefa para atualizar dimensão de produto semanalmente
    tarefa_atualizar_dim_produto = PythonOperator(
        task_id='atualizar_dimensao_produto',
        python_callable=atualizar_dim_produto,
        execution_timeout=timedelta(minutes=15),
    )

    # Dependências entre tarefas (se necessário)
    tarefa_etl_completo >> tarefa_atualizar_dim_produto
