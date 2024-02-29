from bs4 import BeautifulSoup
import requests

# Pede ao usuário para inserir uma data
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Solicita a página do Billboard Hot 100 para a data especificada
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

# Analisa o conteúdo HTML
soup = BeautifulSoup(response.text, 'html.parser')
# Seleciona os nomes das músicas do HTML analisado
song_names_spans = soup.select("li ul li h3")
# Extrai e limpa os nomes das músicas
song_names = [song.getText().strip() for song in song_names_spans]

# Imprime a lista de nomes de músicas
print(song_names)