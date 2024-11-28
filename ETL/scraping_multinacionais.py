# scraping_multinacionais.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Novo URL base para a lista de maiores empresas de varejo do mundo
URL_BASE = "https://en.wikipedia.org/wiki/List_of_supermarket_chains"

def extrair_empresas_retail(url):
    """
    Extrai os nomes, links e países/regiões das empresas da página de varejo.
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
                if len(colunas) > 2:  # Garantir que haja pelo menos 3 colunas
                    nome_empresa = colunas[0].text.strip()
                    link_empresa = colunas[0].find('a')
                    link_empresa = f"https://en.wikipedia.org{link_empresa['href']}" if link_empresa else None
                    
                    # Capturar o país ou região da 2ª ou 3ª coluna
                    pais_ou_regiao = colunas[1].text.strip()  # Alterar índice para 1 ou 2 conforme necessidade

                    empresas.append({
                        "Empresa": nome_empresa,
                        "Região/Pais": pais_ou_regiao,
                        "Link": link_empresa
                    })
        else:
            print("Tabela de empresas não encontrada.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL {url}: {e}")

    return empresas

def carregar_empresas_super_store():
    """
    Carrega os países presentes no dataset da Super Store.
    """
    df_super_store = pd.read_csv('dataset/superstore.csv')
    print("Colunas disponíveis no dataset:", df_super_store.columns)
    
    # Retornar a lista de países únicos
    return df_super_store['country'].unique().tolist()

def comparar_empresas(super_store_paises, multinacionais_empresas):
    """
    Compara os países/regiões das empresas da Super Store com os das multinacionais.
    """
    empresas_comparadas = []

    for empresa in multinacionais_empresas:
        presente_na_super_store = "Sim" if empresa["Região/Pais"] in super_store_paises else "Não"
        empresas_comparadas.append({
            "Empresa": empresa["Empresa"],
            "Região/Pais": empresa["Região/Pais"],
            "Link": empresa["Link"],
            "Presente_na_Super_Store": presente_na_super_store
        })

    return empresas_comparadas

def main():
    """
    Extrai empresas de varejo, compara com as da Super Store,
    e salva o resultado em um arquivo CSV.
    """
    # Carregar países da Super Store
    super_store_paises = carregar_empresas_super_store()

    # Extrair empresas e países de varejo
    print("Extraindo empresas e países de varejo da página Wikipedia.")
    empresas_retail = extrair_empresas_retail(URL_BASE)

    # Comparar empresas e países extraídos com os da Super Store
    empresas_comparadas = comparar_empresas(super_store_paises, empresas_retail)

    if empresas_comparadas:
        # Salvar o resultado em CSV
        df_empresas_comparadas = pd.DataFrame(empresas_comparadas)
        df_empresas_comparadas.to_csv("dataset/empresas_comparadas.csv", index=False, encoding="utf-8")
        print("Dados salvos em dataset/empresas_comparadas.csv")
    else:
        print("Nenhuma empresa foi extraída. Verifique o código ou as páginas da Wikipedia.")

# Executar o código principal
if __name__ == "__main__":
    main()
