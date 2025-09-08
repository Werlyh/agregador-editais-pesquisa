import requests
from bs4 import BeautifulSoup
from .models import db, Edital
from datetime import datetime
import certifi
import locale
try:
    # Tenta configurar a locale para pt_BR
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    try:
        # Fallback para locale padrão do sistema
        locale.setlocale(locale.LC_TIME, '')
        print("Usando locale padrão do sistema")
    except locale.Error:
        # Se nada funcionar, continua sem locale específico
        print("Locale não disponível, continuando sem configuração específica")
        pass




URL_FAPESB = "http://www.fapesb.ba.gov.br/category/upload/"

def buscar_editais_fapesb():
    """
    Busca por editais abertos no site da FAPESB e salva os novos no banco.
    """
    print("Iniciando busca por editais da FAPESB...")
    try:
        response = requests.get(URL_FAPESB, timeout=20, verify=False)
        
        response.raise_for_status() 

        soup = BeautifulSoup(response.content, 'html.parser')

        lista_de_links = soup.find_all('a', class_='link-pdf')
        
        if not lista_de_links:
            print("Nenhum link com a classe 'link-pdf' foi encontrado. Verifique a URL e a estrutura do site.")
            return

        novos_editais_adicionados = 0
        
        for link_tag in lista_de_links:
            titulo = link_tag.get_text(strip=True)
            link = link_tag['href']

            if not titulo or not link:
                continue

            existe = Edital.query.filter(Edital.link == link).first()
            if existe:
                continue

            data_limite = None

            novo_edital = Edital(
                titulo=titulo,
                link=link,
                agencia="FAPESB",
                data_limite=data_limite
            )
            db.session.add(novo_edital)
            novos_editais_adicionados += 1
            print(f"Novo edital encontrado: {titulo}")

        if novos_editais_adicionados > 0:
            print(f"Sucesso! {novos_editais_adicionados} novos editais da FAPESB salvos no banco.")
        else:
            print("Nenhum novo edital da FAPESB encontrado.")

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao acessar o site da FAPESB: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado no scraper da FAPESB: {e}")


def rodar_todos_scrapers():
    """Função que será chamada pelo agendador para rodar todos os scrapers."""
    buscar_editais_fapesb()
    # Futuramente, você pode adicionar outros aqui:
    # buscar_editais_cnpq()