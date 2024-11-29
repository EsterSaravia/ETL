# Projeto ETL e Análise de Dados com Automação 

Este projeto é uma solução completa para realizar Extração, Transformação e Carga (ETL) de dados, análise exploratória, com a automação dos processos utilizando Apache Airflow. Inclui também uma comparação de empresas concorrentes, integração com banco de dados PostgreSQL e visualizações interativas.

## Estrutura do Diretório

ETL 
/.amb # Ambiente Python 
/airflow_env   # Ambiente para execução do Apache Airflow 
/dataset   # Dados brutos utilizados no projeto 
   --empresas comparadas.csv 
   --superstore.csv /etlTL 
--pycache 
--README.md   # Descrição do módulo 
/etl 
   --extract.py   # Script para extração dos dados 
   --transform.py   # Script para transformação dos dados 
   --load.py   # Script para carga dos dados no SQLite 
/notebooks   # Notebooks para exploração e modelagem 
   --README.md   # Detalhes sobre os notebooks 
   --exploratoria.ipynb   # Análise exploratória dos dados 
   --modelagem.ipynb   # Modelagem preditiva e avaliação 
/dags   # DAGs para automação com Airflow 
   --README.md   # Descrição dos DAGs 
   --etl_pipeline_dag.py   # DAG para automação do ETL 
--Relatório ETL.pdf   # Resumo didático do processo de ETL 
--main.py   # Pipeline completo 
--migracao.py   # Migração de dados para PostgreSQL 
--scraping_multinacionais.py   # Comparação de empresas concorrentes 
--superstore.db  # Banco de dados SQLite com tabelas de fatos e dimensões

---

## Funcionalidades Principais

1. **ETL (Extração, Transformação e Carga):**
   - **Extração:** Importação de dados brutos em CSV para um DataFrame do pandas.
   - **Transformação:** Limpeza, estruturação, e criação de tabelas de fatos e dimensões.
   - **Carga:** Carregamento dos dados no banco SQLite ou PostgreSQL.

2. **Análise Exploratória:**
   - Utiliza visualizações interativas (Plotly) para analisar padrões, tendências e concorrência no mercado.
   - Realiza análise de dados brutos e estruturados para insights iniciais.

3. **Modelagem Preditiva:**
   - Construção e avaliação de modelos para prever eventos ou tendências baseados nos dados estruturados.

4. **Automação com Airflow:**
   - DAG para execução e agendamento do processo de ETL.
   - Suporte para atualização automatizada de dados e integração com o pipeline completo.

5. **Comparação de Empresas Concorrentes:**
   - Scraping de dados para analisar empresas multinacionais e realizar benchmarks.

6. **Migração de Banco de Dados:**
   - Migração dos dados processados para PostgreSQL para maior escalabilidade e integração com Power BI.

---

## Como Rodar o Projeto

**1. Pré-requisitos**
- Python 3.8 ou superior
- Instalar as dependências listadas em `requirements.txt`:
  ```bash
  pip install -r requirements.txt

Configurar o Apache Airflow:
Criar um ambiente no diretório /airflow_env.
Configurar o backend do Airflow (SQLite ou PostgreSQL).

---

**2. Executar o ETL**
- Executar os scripts na pasta /etl em sequência:
```bash
python etl/extract.py
python etl/transform.py
python etl/load.py

---

**3. Rodar os Notebooks**
- Abra os notebooks com Jupyter:
```bash
jupyter notebook

-**Execute:**
exploratoria.ipynb para análise exploratória.
modelagem.ipynb para modelagem preditiva.

---

**4. Automação com Airflow**
Adicione o DAG etl_pipeline_dag.py na pasta dags do seu Airflow.
Inicie o Airflow:
```bash
airflow webserver & airflow scheduler

Habilite e execute o DAG na interface web (http://localhost:8080).

---

**5. Migração para PostgreSQL**
Execute o script migracao.py:
```bash
python migracao.py

---

**6. Scraping de Dados de Concorrentes**
Execute o script de scraping:
```bash
python scraping_multinacionais.py

---

## Dependências

O projeto utiliza as seguintes bibliotecas e ferramentas:

### ETL e Análise:
pandas, numpy, sqlite3

### Modelagem e Visualizações:
scikit-learn, plotly

### Automação:
apache-airflow

### Web Scraping:
beautifulsoup4, requests

### Banco de Dados:
psycopg2 (PostgreSQL)

## Observações

### Banco de Dados:
O SQLite é utilizado para armazenamento inicial dos dados. A migração para PostgreSQL pode ser realizada para escalabilidade e conecao com Power BI.

### Airflow:
Certifique-se de configurar o backend do Airflow antes de executar os DAGs.

### Documentação:
Consulte o arquivo Relatório ETL.pdf para um resumo didático do processo.

---

### Principais Melhorias:
1. **Detalhamento**: Descrevi todas as funcionalidades principais do projeto.
2. **Estrutura**: Apresentei uma visão clara do diretório com explicações sobre cada componente.
3. **Instruções de Execução**: Forneci etapas detalhadas para rodar cada parte do projeto.
4. **Dependências**: Listei as bibliotecas usadas em categorias.
5. **Documentação Centralizada**: Incluí menções ao arquivo `Relatório ETL.pdf` para facilitar consultas.

---
