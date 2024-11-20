import os
import argparse
import yt_dlp
from moviepy.editor import AudioFileClip

# Argument parser setup
parser = argparse.ArgumentParser(description="Download YouTube audio and convert to MP3.")
parser.add_argument("url", help="YouTube video URL")
parser.add_argument("output_dir", help="Directory to save the MP3 file")

args = parser.parse_args()

url = args.url
output_dir = args.output_dir

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# yt-dlp options
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
}

print("Downloading and converting to MP3...")

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)
        print(f"Audio download and conversion complete! MP3 saved at {os.path.join(output_dir, result['title'] + '.mp3')}")
except Exception as e:
    print(f"An error occurred: {e}")
