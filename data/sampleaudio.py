import subprocess, os, wave
import audioop

def convert_samplerate(data, source_sr, target_sr):
  """Resample audio data from source_sr to target_sr"""
  if source_sr == target_sr:
    return data
  if source_sr < target_sr:
    # Upsample
    factor = target_sr / source_sr
    data = audioop.lin2lin(data, 2, factor)
  else:
    # Downsample
    factor = source_sr / target_sr
    data = audioop.lin2lin(data, 2, factor)
  return data

# Get list of .mp4 files in current directory
mp4_files = [f for f in os.listdir('audio') if f.endswith('.mp4')]

for in_file in mp4_files:
  # Check if file is valid
  try:
    subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=codec_name', in_file])
  except subprocess.CalledProcessError:
    print(f"{in_file} is invalid!")
    continue

for filename in mp4_files:
    subprocess.run(['ffmpeg', '-i', filename, f'{filename}.wav'])
    # Load .wav file
    wav = wave.open(f'{filename}.wav', 'rb')
    # Resample if needed
    frame_rate = wav.getframerate()
    if frame_rate != 16000:
        data = wav.readframes(wav.getnframes())
        converted = convert_samplerate(data, frame_rate, 16000)

        # Save 16khz version
        out = wave.open(f'{filename}_16khz.wav', 'wb') 
        out.setframerate(16000)
        out.writeframes(converted)
        out.close()
    wav.close()