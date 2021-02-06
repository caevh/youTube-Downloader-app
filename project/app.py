import PySimpleGUI as ps
from pytube import YouTube
import os

video_url = "https://www.youtube.com/watch?v=ApXoWvfEYVU"
download_destination = "/home/harry/Projects/youTube-Downloader-app/downloads"

vid = YouTube(video_url)

def video_downloader(video):
    video_stream = vid.streams.filter(adaptive=True, file_extension='mp4').first()
    video_stream.download('/home/harry/Projects/youTube-Downloader-app/downloads/video')
    print('success')

def audio_downloader(audio):
    audio_stream = vid.streams.filter(adaptive=True, file_extension='mp4').last()
    audio_stream.download('/home/harry/Projects/youTube-Downloader-app/downloads/audio')
    print('success')

def video_audio_merge():
    return True
video_downloader(vid)
audio_downloader(vid)