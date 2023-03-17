
from requests_html import HTMLSession
from pathlib import Path
from lxml import etree
import youtube_dl
import re
import requests
import pandas
import os

def DownloadVideosFromTitles(los):
	ids = []
	for index, item in enumerate(los):
		vid_id = ScrapeVidId(item)
		ids += [vid_id]
	print(ids)
	print("Downloading songs")
	DownloadVideosFromIds(ids)


def DownloadVideosFromIds(lov):
	SAVE_PATH = str(os.path.join(Path.home(), "Documents/songs"))
	try:
		os.mkdir(SAVE_PATH)
	except:
		print("download folder exists")
	print(f"downvidid{lov}")
	ydl_opts = {
   
		'ffmpeg_location' : r"C:\Users\Karthick Sriram\AppData\Local\Programs\Python\Python39\Scripts\ffmpeg.exe",
		'format': 'bestaudio/best',
    	'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    	}],
   
    
		'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(lov)


def ScrapeVidId(query):

    url = f"https://www.youtube.com/results?search_query={query}"
    query = url.replace(" ", "+")
    response = requests.get(url)
    video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
    return video_ids[0]

def __main__():

	data = pandas.read_csv('songs.csv')
	data = data['song names'].tolist()
	print("Found ", len(data), " songs!")
	DownloadVideosFromTitles(data)
__main__()
