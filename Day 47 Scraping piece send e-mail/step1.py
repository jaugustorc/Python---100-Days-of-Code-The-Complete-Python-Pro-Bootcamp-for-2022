import requests
import lxml
from bs4 import BeautifulSoup

# Define a URL do produto na Amazon
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# Configura os cabeçalhos para simulação de uma requisição de navegador
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Faz a requisição para a URL do produto
response = requests.get(url, headers=header)

# Parseia o conteúdo da resposta com BeautifulSoup
soup = BeautifulSoup(response.content, "lxml")
# Imprime o HTML formatado
#print(soup.prettify())

# Busca o preço do produto e extrai o texto
price = soup.find(class_="a-offscreen").get_text()
# Remove a moeda do preço (ex: transforma "$23.50" em "23.50")
price_without_currency = price.split("$")[1]
# Converte a string do preço para float
price_as_float = float(price_without_currency)
# Imprime o preço como float
print(price_as_float)