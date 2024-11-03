import yt_dlp
import os
from pathlib import Path
from yt_dlp.postprocessor import FFmpegPostProcessor

def create_music_folder():
    music_dir = Path('music')
    music_dir.mkdir(exist_ok=True)
    return music_dir

def download_music(url, output_filename):
    music_dir = create_music_folder()
    ydl_opts = {
        'ffmpeg_location': "ffmpeg/bin/ffmpeg.exe",
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320', # 320 paling tinggi untuk format mp3
        }],
        'outtmpl': str(music_dir / f'{output_filename}.%(ext)s'),
        'verbose': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"\nDownloaded successfully, and saved at: {music_dir}/{output_filename}.mp3")
        except Exception as e:
            print(f"Error: {str(e)}")

def main():    
    while True:
        url = input("\nYoutube or Youtube Music URL: ")
        output_filename = input("Output name (withouth extention): ")
        download_music(url, output_filename)

if __name__ == "__main__":
    main()