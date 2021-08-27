import requests
import time
import enviar_email as email
from bs4 import BeautifulSoup


def transformar_preco_em_valor_real(preco_texto):
    preco_em_valor_real = preco_texto.strip().rstrip()
    preco_em_valor_real = preco_em_valor_real.split()[1]
    preco_em_valor_real = preco_em_valor_real.replace(',', '.')

    return float(preco_em_valor_real)


pagina = 'https://www.dafiti.com.br/Tenis-Converse-Chuck-Taylor-All-Star-Azul-7717087.html'
PRECO_MAXIMO = 300

while True:
    try:
        response = requests.get(pagina)

        soup = BeautifulSoup(response.text, 'html.parser')
        preco_do_produto = soup.find(
            'span', {'class': 'catalog-detail-price-value'}).text

        preco_do_produto = transformar_preco_em_valor_real(preco_do_produto)

        if preco_do_produto <= PRECO_MAXIMO:
            email.enviar()

        time.sleep(1800)
    except Exception as e:
        print(e)
