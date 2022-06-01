import requests
from dotenv import load_dotenv
import os

load_dotenv()

class SpotifyClient(object):
	def __init__(self, api_token):
		self.api_token = api_token

	def get_tracks(self, numtracks):
		url = f'https://api.spotify.com/v1/me/top/tracks?limit={numtracks}'
		spotify_auth_token = os.getenv("SPOTIFY_AUTH_TOKEN")
		response = requests.get(
			url, 
			headers={
				"Content-Type": "application/json",
				"Authorization": f"Bearer {spotify_auth_token}"
			}
		)

		response_json = response.json()
		tracks = {track["name"] : track["artists"][0]["name"] for track in response_json["items"]}

		return tracks