# import required modules
import torch
import torchaudio
from torchaudio import transforms
from torchaudio.datasets import LIBRISPEECH
from torchaudio.models import Wav2Vec2Model

# load pretrained Wav2Vec2 model for English speech 
model = torchaudio.models.Wav2Vec2Model()
model.eval()

# define audio transforms to prepare input 
transforms = torchaudio.transforms.MelSpectrogram(sample_rate=16000, n_mels=64)

# load sample classroom audio clip
classroom_clip, sr = torchaudio.load('data/audio/1 Introductions.mp4')

# transcribe audio clip using Wav2Vec2 model
with torch.inference_mode():
  input = transforms(classroom_clip).unsqueeze(0) # add batch dim
  logits = model(input).logits  
  predicted_ids = torch.argmax(logits, dim=-1)
  transcription = model.decode(predicted_ids[0])

print(transcription)

# display transcription on mobile app UI
# highlight key terms, offer playback  
# connect administrator portal for transcript review

# TODO: 
# - optimize model for classroom audio
# - add text-to-speech 
# - simplify UX based on user testing
# - add gamification elements 
# - distribute on app stores
'''
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset

device = "cpu"
torch_dtype = torch.float32

model_id = "openai/whisper-large-v3"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)

dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
sample = dataset[0]["audio"]

result = pipe(sample)
print(result["text"])'''