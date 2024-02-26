import os # wave, subprocess, audioop
from pydub import AudioSegment

src_folder = 'audio'
dest_folder = 'audio_16khz'

os.makedirs(dest_folder, exist_ok=True)

mp4_files = [f for f in os.listdir(src_folder) if f.endswith('.mp4')]

for i in range(0, len(mp4_files), 2):
  chunk = mp4_files[i:i+2]
  
  for f in chunk:
    src = os.path.join(src_folder, f)
    dest = os.path.join(dest_folder, os.path.splitext(f)[0] + '.wav')
    
    # Convert .mp4 to .wav
    sound = AudioSegment.from_file(src, format="mp4")
    sound = sound.set_frame_rate(16000)
    sound.export(dest, format="wav")