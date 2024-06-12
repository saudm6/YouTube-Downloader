from pytube import YouTube                      # Import the YouTube class from the pytube library
from sys import argv                            # Import the argv function from the sys module to handle command-line arguments

link = argv[1]                                  # Get the YouTube link from the command-line argument

yt = YouTube(link)                              # Create a YouTube object with the provided link

print("Title: ", yt.title)                      # Display the title of the video

print("Views: ", yt.views)                      # Display the number of views the video has

yd = yt.streams.get_highest_resolution()        # Download the highest resolution available

yd.download("D:/youtube/videos")                # Change it to to the directory you want

# Read the Readme file to get the instructions on how to use the downloader
