# ETL (Extract, Transform, Load)

Este módulo é responsável pela extração, transformação e carga dos dados no banco de dados SQLite. Ele realiza as seguintes funções:

- **Extração (extract.py)**: Carrega os dados a partir de um arquivo CSV para um DataFrame do pandas.
- **Transformação (transform.py)**: Realiza a limpeza e transformação dos dados, criando tabelas de fatos e dimensões.
- **Carga (load.py)**: Carrega os dados transformados para um banco de dados SQLite, criando as tabelas necessárias.

## Como funciona

1. **Extração**: O arquivo CSV é carregado usando a função `load_data` do `extract.py`.
2. **Transformação**: Os dados extraídos são limpos e transformados na função `clean_data` do `transform.py`. 
3. **Carga**: As tabelas resultantes são carregadas no banco de dados SQLite usando a função `load_to_sqlite` do `load.py`.

### Dependências

- pandas
- sqlite3
- requests
- beautifulsoup4
