import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

SCOPE = "user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    cache_path=".cache"
))

def get_user_top_tracks():
    results = sp.current_user_top_tracks(limit=5, time_range='short_term')
    tracks = results['items']
    # Return list of dicts with song and artist
    return [{'name': track['name'], 'artist': track['artists'][0]['name']} for track in tracks]

def quiz():
    tracks = get_user_top_tracks()
    score = 0
    print("\nGuess the song title! I'll give you the artist name.\n")
    
    for i, track in enumerate(tracks, 1):
        print(f"Artist: {track['artist']}")
        guess = input(f"Song #{i} title? ").strip()
        
        if guess.lower() == track['name'].lower():
            print("Correct! 🎉\n")
            score += 1
        else:
            print(f"Oops, the answer was '{track['name']}'.\n")
    
    print(f"Game over! Your final score: {score} out of {len(tracks)}")

if __name__ == "__main__":
    quiz()

