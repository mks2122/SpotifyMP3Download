from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'requests_html',
    'beautifulsoup4',
    'youtube_dl',
    'pathlib',
    'pandas'
]

setup(
    name='SpotifyDownload',
    version='1.0',
    description='An application that gets your Spotify songs and downloads the YoutubeMP3 version',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)