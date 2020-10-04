import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from client import clientID,secretID

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clientID,
                                                           client_secret=secretID))

results = sp.search(q='joji', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])