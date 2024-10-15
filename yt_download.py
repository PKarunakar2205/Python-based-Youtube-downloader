#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pytube')


# In[2]:


pip install customtkinter


# In[3]:


pip install --upgrade pytube


# In[6]:


from pytube import YouTube
from pytube.exceptions import VideoUnavailable, AgeRestrictedError
import urllib.error

# Function to download YouTube video or fallback to audio
def download_video(youtube_url):
    try:
        # Create a YouTube object with the URL
        yt = YouTube(youtube_url)

        # Try downloading the video with the highest resolution
        try:
            print(f"Downloading video: '{yt.title}'...")
            stream = yt.streams.get_highest_resolution()
            stream.download()
            print(f"Download complete: '{yt.title}'")

        # Fallback to audio if video fails
        except Exception as e:
            print(f"Error downloading video: {e}. Trying to download audio...")
            stream = yt.streams.get_audio_only()
            stream.download()
            print(f"Audio download complete: '{yt.title}'")

    except VideoUnavailable:
        print("The video is unavailable. Please check the URL.")
    except AgeRestrictedError:
        print("The video is age-restricted and cannot be downloaded.")
    except urllib.error.HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
youtube_link = input("Enter the YouTube video URL: ")
download_video(youtube_link)


# In[7]:


pip install yt-dlp


# In[12]:


import yt_dlp
import os

def download_video(url, output_path):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Specify output template
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')  # Output file name template
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Set the output directory where you want to save the downloaded videos
output_directory = r"D:\from c drive\Downloads"  # Specify your desired output path

# Get the YouTube link from the user
youtube_link = input("Enter the YouTube video URL: ")
download_video(youtube_link, output_directory)


# In[ ]:




