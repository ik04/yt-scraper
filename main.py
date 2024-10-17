import os
import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress
from moviepy.editor import AudioFileClip

parser = argparse.ArgumentParser(description="Download YouTube audio and convert to MP3.")
parser.add_argument("url", help="YouTube video URL")
parser.add_argument("output_dir", help="Directory to save the MP3 file")

args = parser.parse_args()

url = args.url
output_dir = args.output_dir

yt = YouTube(url, on_progress_callback=on_progress)

print(f"Title: {yt.title}")

audio_stream = yt.streams.filter(only_audio=True).first()

if audio_stream:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    temp_audio_file = audio_stream.download(output_path=output_dir)
    mp3_file = temp_audio_file.replace(".mp4", ".mp3").replace(".webm", ".mp3")

    print("Converting to MP3...")
    audio_clip = AudioFileClip(temp_audio_file)
    audio_clip.write_audiofile(mp3_file)
    audio_clip.close()
    os.remove(temp_audio_file)
    print(f"Audio download and conversion complete! MP3 saved at {mp3_file}")
else:
    print("No audio stream available.")
