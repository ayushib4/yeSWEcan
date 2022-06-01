import urllib.request
import re
from dotenv import load_dotenv

load_dotenv()

def get_music_videos(tracks):
    videos = {}

    for track, artist in tracks.items():
        t = track.replace("’", "'")
        t = t.replace(" ", "+")
        a = artist.replace(" ", "+")
        a = a.replace("’", "'")
        search_keyword = f"{t}+{a}"
        url = "https://www.youtube.com/results?search_query=" + search_keyword
        html = urllib.request.urlopen(url)
        video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        videos[track] = "https://www.youtube.com/watch?v=" + video_id[0]
    
    return videos
