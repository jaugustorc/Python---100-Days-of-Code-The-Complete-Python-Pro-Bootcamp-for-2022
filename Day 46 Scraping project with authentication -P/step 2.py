import spotipy
from spotipy.oauth2 import SpotifyOAuth

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