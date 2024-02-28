import torch
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from torch.utils.data import Dataset, DataLoader
import torch.multiprocessing as mp
from math import ceil

# load model  
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# set device
device = "cpu"

# load model  
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Define dataset to chunk audio
class AudioDataset(Dataset):

    def __init__(self, audio_file, chunk_len=10):  
        self.audio_file = audio_file
        self.chunk_len = chunk_len * 16000 # chunk length in samples
        
    def __getitem__(self, idx):
        start = idx * self.chunk_len
        stop = start + self.chunk_len
        chunk = self.audio_file[start:stop]
        return chunk

    def __len__(self):
        return ceil(len(self.audio_file) / self.chunk_len)

# Transcribe function for each chunk
def transcribe_chunk(chunk):
    input = processor(chunk, sampling_rate=16_000, return_tensors="pt") 
    logits = model(input.input_values).logits
    transcription = processor.batch_decode(logits.argmax(dim=-1))
    return transcription

# Multiprocess transcribe all chunks    
def transcribe(audio_file, output_file):
    
    ds = AudioDataset(audio_file)
    loader = DataLoader(ds, batch_size=1)

    pool = mp.Pool(mp.cpu_count())
    results = pool.map(transcribe_chunk, loader)

    with open(output_file, 'w') as f:
        f.write(" ".join(results))

# Usage
transcribe('data/audio_16khz/The-Science-of-StorytellingThe-Storytelling-of-Science---Brian-Knutson.wav', 'data/transcribed/The-Science-of-Storytelling---Brian-Knutson.txt')

# display transcription on mobile app UI
# highlight key terms, offer playback  
# connect administrator portal for transcript review

# TODO: 
# - optimize model for classroom audio
# - add text-to-speech 
# - simplify UX based on user testing
# - add gamification elements 
# - distribute on app stores