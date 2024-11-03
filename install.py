import requests
import zipfile
import os
from tqdm import tqdm

def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as progress_bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            progress_bar.update(size)

def extract_zip():
    with zipfile.ZipFile('ffmpeg.zip', 'r') as zip_ref:
        zip_ref.extractall()

def cleanup():
    if os.path.exists('ffmpeg.zip'):
        os.remove('ffmpeg.zip')

def main():
    url = "https://github.com/shiwildy/YTMusicDownload/releases/download/ffmpeg/ffmpeg.zip"
    
    try:
        print("Downloading FFmpeg...")
        download_file(url, 'ffmpeg.zip')
        
        print("\nExtracting...")
        extract_zip()
        cleanup()
        
        print("\nDone! FFmpeg has been installed.")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()