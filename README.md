# YoutubeDownloader

## Description

YoutubeDownloader is an application built on the Python package <a href="http://ytdl-org.github.io/youtube-dl/">youtube_dl</a> to download audio from YouTube videos. This application utilizes the Python package pydub to trim audio files upon download and was created using PyQt5 and PyQt5 Designer.

All input fields in the program are optional except for the URL text box.

## Installation
To run the program, create a Python virtual environment and install all the requirements in requirements.txt.

Then, to bundle this application as a .app for MacOS, run:

`pyinstaller --onefile --windowed --icon=resource/icon.icns --add-binary=ffmpeg_mac/bin/*:. -n "Youtube Downloader" --clean app/app.py`

To compile this program into a .exe for Windows, install the Windows <a href="https://ffmpeg.org/download.html#build-windows">FFmpeg</a> binaries in the root of the project directory. Then run:

`python3 -m PyInstaller --onefile --windowed --icon=resource\icon.ico --add-binary=ffmpeg_windows\bin\*;. -n "Youtube Downloader" --paths=.venv\Lib\site-packages --clean app\app.py`

