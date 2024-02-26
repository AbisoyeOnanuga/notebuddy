from pytube import YouTube
import os

# List of YouTube video URLs
lecture_urls = [
'''    "https://www.youtube.com/watch?v=TyVAU5iGe0k",
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
    "https://www.youtube.com/watch?v=C5TWHj2Eqew",'''
    # The Science of Storytelling
    "https://www.youtube.com/watch?v=nykOeWgQcHM",
    "https://www.youtube.com/watch?v=SE4P7IVCunE",
    "https://www.youtube.com/watch?v=MjbuarJ7SE0",
    # Introductin to Computer Science and Programming in Python
    '''"https://www.youtube.com/watch?v=Igl8hE3Eac0",
    "https://www.youtube.com/watch?v=yy989li6xgY",
    # Lecture collectin: Particle Physics
    "https://www.youtube.com/watch?v=pjDbQDNOBYY",
    "https://www.youtube.com/watch?v=bB2E0PI2N_o",
    # Web3 Blockchain Fundamentals MOOC
    "https://www.youtube.com/watch?v=L3LMbpZIKhQ",
    "https://www.youtube.com/watch?v=z8HKWUWS-lA",
    # MIT 6.042J Mathematics for computer Science
    "https://www.youtube.com/watch?v=CzrUquTurzw",
    "https://www.youtube.com/watch?v=vTDCChTAnrs",
    "https://www.youtube.com/watch?v=Suodr0VVHgM",
    "https://www.youtube.com/watch?v=MNAshR_e9sk",
    "https://www.youtube.com/watch?v=NYBAxql8-Xo",
    # Stanfor CS105 - Introduction
    "https://www.youtube.com/watch?v=MNAshR_e9sk",
    "https://www.youtube.com/watch?v=4cfctnaHyFM",
    "https://www.youtube.com/watch?v=jVYs-GTqm5U",
    "https://www.youtube.com/watch?v=d5d0ORQHNYs",
    "https://www.youtube.com/watch?v=mOiY1fOROOg",
    "https://www.youtube.com/watch?v=7haZCrQDHpA"'''
    # Fourier Analysis [Data-Driven Science and Engineering]
    # list of lecture video urls
] 

import moviepy.editor as mp
from multiprocessing.pool import ThreadPool

# Folder to save audio
AUDIO_DIR = 'lecture_audio'  

if not os.path.exists(AUDIO_DIR):
    os.mkdir(AUDIO_DIR)

def download_audio(yt_url):
    """Download audio from YouTube video as WAV file"""
    
    # Download YouTube video using Pytube
    yt = YouTube(yt_url)
    video = yt.streams.filter(only_audio=True).first()

    # Download the audio stream to memory 
    audio_bytes = video.stream_to_buffer()

    # Load in-memory audio to MoviePy 
    audio_clip = mp.AudioFileClip(audio_bytes.getvalue())

    # Save audio clip as WAV file
    file_name = yt.title + ".wav"
    output_path = os.path.join(AUDIO_DIR, file_name)
    audio_clip.write_audiofile(output_path)

    print(f"Saved {file_name}")

# Use thread pool to download videos in parallel 
with ThreadPool(2) as pool:
    pool.map(download_audio, lecture_urls)
    
print("Download complete!")