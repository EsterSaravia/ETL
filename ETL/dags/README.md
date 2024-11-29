# Dags

Esta pasta contém os DAGs (Directed Acyclic Graphs) para automação dos fluxos de trabalho no Apache Airflow. Os DAGs são responsáveis por gerenciar as tarefas de ETL, análise de dados, e outras automações no processo.

## Estrutura dos DAGs

O DAG define um fluxo de trabalho, com etapas como extração de dados, transformação, carregamento (ETL). Abaixo está a descrição de cada um dos DAGs presentes:

- **etl_pipeline_dag.py**: DAG para a execução do processo completo de ETL (Extração, Transformação e Carga) com o uso de funções do módulo `ETL`, automação do processo de ETL. Cada DAG pode ser agendado e executado automaticamente.

## Como Rodar

1. Certifique-se de que o Apache Airflow está configurado corretamente e em execução.
2. Coloque o arquivo de DAG na pasta `dags` no seu diretório.
3. Abra a interface web do Airflow (`localhost:8080`).
4. Habilite e execute o DAG de sua escolha a partir da interface do Airflow.

## Dependências

- **apache-airflow**: Para orquestrar os fluxos de trabalho.

## Observações

- Os DAGs são definidos como scripts Python que dependem do Airflow para serem executados.
- É necessário configurar um banco de dados backend para o Airflow e garantir que todas as dependências de pacotes estejam instaladas.
