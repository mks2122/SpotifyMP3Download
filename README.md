# Spotify Playlist to YouTube Downloader

![GitHub](https://img.shields.io/github/license/yourusername/your-repo)
![Python](https://img.shields.io/badge/python-v3.7%2B-blue)
![Flask](https://img.shields.io/badge/flask-v2.0%2B-green)

This web application allows users to authenticate with their Spotify accounts, select a playlist, and then download the corresponding songs from YouTube. It uses the Spotify API for playlist retrieval and a custom script for downloading videos based on song titles.

## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)


## Features

- Authenticate users using Spotify OAuth.
- Retrieve a list of the user's Spotify playlists.
- Select a playlist to download.
- Download songs from the selected playlist using YouTube.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask 2.0 or higher
- [Spotipy](https://github.com/plamere/spotipy)
- [YouTube Data API v3 Key](https://developers.google.com/youtube/registering_an_application)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/mks2122/SpotifyMP3Download/
   cd SpotifyMP3Download

2. Install the required dependencies
     ```bash
     python setup.py install

3. Get the api key and secret from [spotify developers](https://developer.spotify.com/)

## Usage
1. Run the app by:
      ```bash
      flask run 
2. Access the application in your web browser at http://localhost:5000
3. Click the "Login with Spotify" button to authenticate with your Spotify account
4. Go back to the terminal, and give the playlist to download
5. The default download folder is Downloads
