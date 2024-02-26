import os

folder = 'audio_16khz'

# Get list of .wav files
files = os.listdir(folder)
wav_files = [f for f in files if f.endswith('.wav')]

# Rename files with spaces in name
for f in wav_files:
  if ' ' in f:
    # Replace space with hyphen
    new_name = f.replace(' ', '-')
    # Rename file
    os.rename(os.path.join(folder, f), os.path.join(folder, new_name))

print('Files renamed:')

# Confirm new filenames
renamed_files = os.listdir(folder)
for f in renamed_files:
  if f.endswith('.wav'):
    print(f)