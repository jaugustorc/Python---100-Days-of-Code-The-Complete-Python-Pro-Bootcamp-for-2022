import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

#step1

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

#step2


# Inicializa a autenticação com a API do Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="Day 46 Scraping project with authentication\\token.txt"
    )
)
# Busca o ID do usuário atual
user_id = sp.current_user()["id"]

#step 3
# Inicializa uma lista vazia para armazenar os URIs das músicas
song_uris = []
# Extrai o ano da data fornecida
year = date.split("-")[0]
# Itera sobre cada música encontrada
for song in song_names:
    # Busca a música no Spotify pelo nome e ano
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # Imprime o resultado da busca
    print(result)
    try:
        # Tenta extrair o URI da primeira música encontrada
        uri = result["tracks"]["items"][0]["uri"]
        # Adiciona o URI da música à lista
        song_uris.append(uri)
    except IndexError:
        # Caso nenhum resultado seja encontrado, entra no bloco de exceção
        # Informa que a música não foi encontrada e será ignorada
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Itera sobre os primeiros 4 índices
for i in range(4):
    # Imprime o nome e o URI da música correspondente
    print(f"{song_names[i]}: {song_uris[i]}")
    
