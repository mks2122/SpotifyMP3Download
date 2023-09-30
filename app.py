from flask import Flask,request,url_for,redirect,session
import spotipy
import time
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from downloadSongs import DownloadVideosFromTitles

app=Flask(__name__)

app.secret_key="##############"
app.config['SESSION_COOKIE_NAME']='sdmp3 cookie'
TOKEN_INFO="token_info"

@app.route('/')
def index():
    spotify_oauth=create_spotify_oauth()
    auth_url=spotify_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    spotify_oauth=create_spotify_oauth()
    session.clear()
    code=request.args.get('code')
    token_info=spotify_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info

    
    return redirect(url_for('gettracks',_external=True))


@app.route('/tracks')
def gettracks():
    try:
        token_info=get_token()
    except:
        print("User not logged in")
        return redirect("/")
    sp=spotipy.Spotify(auth=token_info['access_token'])
    playlist_id=getPlaylistId(sp)
    
    names=list(playlist_id.keys())
    for i in range(len(names)):
        print(f"{i}:{names[i]}")
    choice=int(input("Give the corresponding number to the playlist: "))
    play=playlist_id[names[choice]]
    songs=[]
    for i in sp.playlist_items(play,limit=20, offset=0)['items']:
        songs.append(i['track']['name'])
    
    DownloadVideosFromTitles(songs)
    return "Done"
    

def getPlaylistId(sp):
    
    playlist_id= {}
    
    for i in sp.current_user_playlists(limit=50, offset=0)['items']:
        playlist_id[str(i['name'])]=(str(i['id']))
    return playlist_id


def get_token():
    token_info=session.get(TOKEN_INFO,None)
    if not token_info:
        raise "exception"
    now=int(time.time())
    isExpired=token_info['expires_at']-now <60
    if isExpired:
        spotify_oauth=create_spotify_oauth()
        token_info=spotify_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id= '4fb684bca2cc47f2ac037aad5327f1cd',
        client_secret= 'c9ba404a0ae247de8047549d58002ce8',
        redirect_uri=url_for('redirectPage',_external=True),
        scope= 'user-library-read'
    )
if __name__ == '__main__':
    app.run(debug=False)