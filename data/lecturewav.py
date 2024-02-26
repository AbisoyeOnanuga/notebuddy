import pytube
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError
import os
from itertools import zip_longest

# List of YouTube video urls
links = [
    "https://www.youtube.com/watch?v=TyVAU5iGe0k",
    "https://www.youtube.com/watch?v=Twb_APQpzkk",
    # The American Novel since 1945
    "https://www.youtube.com/watch?v=MvPTVgGUsyc",
    "https://www.youtube.com/watch?v=Rf3xSqgpFHE",
    "https://www.youtube.com/watch?v=iJtNvwpKyo4",
    "https://www.youtube.com/watch?v=c52Y2ObjFms",
    "https://www.youtube.com/watch?v=0B69rnynnCA",
    # Entrepreneurship
    "https://www.youtube.com/watch?v=153qWm92uRk",
    "https://www.youtube.com/watch?v=McXlRI_BJNg",
    "https://www.youtube.com/watch?v=C5TWHj2Eqew",
    # The Science of Storytelling
    "https://www.youtube.com/watch?v=nykOeWgQcHM",
    "https://www.youtube.com/watch?v=SE4P7IVCunE",
    "https://www.youtube.com/watch?v=MjbuarJ7SE0",
    # Introductin to Computer Science and Programming in Python
    "https://www.youtube.com/watch?v=Igl8hE3Eac0",
    "https://www.youtube.com/watch?v=yy989li6xgY",
    # Lecture collectin: Particle Physics
    "https://www.youtube.com/watch?v=pjDbQDNOBYY",
    "https://www.youtube.com/watch?v=bB2E0PI2N_o",
    # Web3 Blockchain Fundamentals MOOC
    "https://www.youtube.com/watch?v=L3LMbpZIKhQ",
    "https://www.youtube.com/watch?v=z8HKWUWS-lA",
    # MIT 6.042J Mathematics for computer Science
    "https://www.youtube.com/watch?v=L1ung0wil9Y",
    # MIT Performance Engineering of Software Systems
    "https://www.youtube.com/watch?v=Unzc731iCUY",
    # How to Speak IAP 2018
    "https://www.youtube.com/watch?v=6mbFO0ZLMW8",
    # Hardware - CS50's Understanding Technology 2017
    "https://www.youtube.com/watch?v=3G5hWM6jqPk"
    # MIT 6.S191: Deep Generative Modeling  
    # list of lecture video urls
]

if not os.path.exists('audio'):
    os.makedirs('audio') 
os.chdir('audio')

# Download videos in batches of 2 
for batch in zip_longest(*[iter(links)]*2):
    for url in batch:
        if url is None:
            continue
        try:
            filename = url.split("=")[1] + '.wav'
            if os.path.exists(filename):
                print(f"{filename} already exists, skipping download")
                continue 
            # download and convert audio 
            yt = YouTube(url)
        except AgeRestrictedError as e:
            print(f"{url} is age restricted, and can't be accessed without logging in.")
            continue 
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            continue
        audio = yt.streams.filter(only_audio=True).first()
        try: 
            outfile = audio.download()
            new_file = outfile.replace('.mp4', '.wav')
            os.system(f'ffmpeg -i {outfile} {new_file}')
        except Exception as e:
            print(f"Error converting {url}: {e}")
            continue
        else:
            # successful download
            print('Download complete!')


'''# Delete original mp4 files
for url in batch:
    mp4_file = url.split("=")[1] + '.mp4'
    os.remove(mp4_file)'''