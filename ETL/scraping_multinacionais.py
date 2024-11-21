# scraping_multinacionais.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Novo URL base para a lista de maiores empresas de varejo do mundo
URL_BASE = "https://en.wikipedia.org/wiki/List_of_largest_retail_companies"

def extrair_empresas_retail(url):
    """
    Extrai os nomes e informações das empresas da página de varejo.
    """
    empresas = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar a tabela de empresas
        tabela = soup.find('table', {'class': 'wikitable'})
        if tabela:
            linhas = tabela.find_all('tr')
            for linha in linhas[1:]:  # Ignorar cabeçalho
                colunas = linha.find_all('td')
                if len(colunas) > 1:
                    nome_empresa = colunas[0].text.strip()
                    # Capturar um link, se houver
                    link_empresa = colunas[0].find('a')
                    link_empresa = f"https://en.wikipedia.org{link_empresa['href']}" if link_empresa else None

                    empresas.append({"Empresa": nome_empresa, "Link": link_empresa})
        else:
            print("Tabela de empresas não encontrada.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")

    return empresas

def carregar_empresas_super_store():
    """
    Carrega as empresas concorrentes da Super Store (exemplo: arquivo CSV ou banco de dados).
    """
    # Ajuste o caminho do arquivo conforme necessário
    df_super_store = pd.read_csv('dataset/superstore.csv')
    print("Colunas disponíveis no dataset:", df_super_store.columns)
    
    # Escolha a coluna apropriada, como 'customer_name' ou 'product_name'
    return df_super_store['product_name'].unique().tolist()  # Evitar duplicatas

def comparar_empresas(super_store_empresas, multinacionais_empresas):
    """
    Compara as empresas da Super Store com as multinacionais extraídas.
    """
    empresas_comparadas = []

    for empresa in multinacionais_empresas:
        if empresa["Empresa"] in super_store_empresas:
            empresas_comparadas.append({
                "Empresa": empresa["Empresa"],
                "Link": empresa["Link"],
                "Presente_na_Super_Store": "Sim"
            })
        else:
            empresas_comparadas.append({
                "Empresa": empresa["Empresa"],
                "Link": empresa["Link"],
                "Presente_na_Super_Store": "Não"
            })

    return empresas_comparadas

def main():
    """
    Extrai todas as empresas de varejo, compara com as da Super Store,
    e salva o resultado em um arquivo CSV.
    """
    # Carregar empresas da Super Store
    super_store_empresas = carregar_empresas_super_store()

    # Extrair empresas de varejo
    print("Extraindo empresas de varejo da página Wikipedia.")
    empresas_retail = extrair_empresas_retail(URL_BASE)

    # Comparar empresas extraídas com as da Super Store
    empresas_comparadas = comparar_empresas(super_store_empresas, empresas_retail)

    if empresas_comparadas:
        # Converter dados para DataFrame e salvar em CSV
        df_empresas_comparadas = pd.DataFrame(empresas_comparadas)
        df_empresas_comparadas.to_csv("dataset/empresas_comparadas.csv", index=False, encoding="utf-8")
        print("Dados salvos em dataset/empresas_comparadas.csv")
    else:
        print("Nenhuma empresa foi extraída. Verifique o código ou as páginas da Wikipedia.")

# Executar o código principal
if __name__ == "__main__":
    main()
