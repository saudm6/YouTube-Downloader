from pytubefix import YouTube
from pytubefix.cli import on_progress
from sys import argv
import sys

# Custom progress function
def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = int(bytes_downloaded / total_size * 100)

    bar_length = 50 
    filled_length = int(bar_length * percentage // 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write(f"\rDownloading: |{bar}| {percentage}%")
    sys.stdout.flush()

    if percentage == 100:
        print("\n✅ Download Complete!")


link = argv[1]

yt = YouTube(link, on_progress_callback=progress_func)

print("Title: ", yt.title)
print("Views: ", yt.views)

ys = yt.streams.get_highest_resolution()
print("Starting download...")
ys.download("D:/youtube/videos")
