import os
from youtube import *
from spotify_client import SpotifyClient


def run():

	# Directions
	print("\nThis script will help make your YouTube playlist-making process a lot faster!\n")
	while True:
		try:
			num_songs = int(input("To get started, how many of your top songs would you like to add? "))
		except ValueError:
			print("Please enter a number.")
			continue
		else:
			break
	print("Great!\n")

	input("Retrieve your access token here: https://developer.spotify.com/console/get-current-user-top-artists-and-tracks/\n\nOnce you are done, press enter. \n")

	# Getting the user's OAuth Token
	token = input("Enter your Spotify OAuth Token: ")
	try:
		env_file = open(".env", "x")
	except FileExistsError:
		print("Refreshing the .env file...\n")
		os.remove(".env")
		env_file = open(".env", "x")
	env_file.write(f"SPOTIFY_AUTH_TOKEN={token}")
	spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
	
	# Getting the top x songs
	top_tracks = spotify_client.get_tracks(num_songs)
	top_tracks = get_music_videos(top_tracks)
	for name, video in top_tracks.items():
		print(f"{name} ----- {video}")


if __name__ == '__main__':
	run()