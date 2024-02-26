# Note Buddy

Note Buddy is a real-time class transcription app to aid learning disabilities for visually impaired students. It uses speech recognition to generate live transcripts of classroom lectures.

## About

This project was built at ICP.HUB North America's Live AI Ideathon. It provides an initial prototype to demonstrate real-time speech-to-text transcription of classroom audio.

Key features:

- Real-time speech recognition using PyTorch and Wav2Vec2
- Highlighting of key terms in transcripts
- Playback of audio segments  
- Administrator portal to review transcripts
- Mobile app UI and UX designed for classrooms

## Getting Started

### Prerequisites

- Python 3.6+
- PyTorch 1.7+
- Other dependencies listed in `requirements.txt`

### Installation

```bash
git clone https://github.com/username/notebuddy.git
cd notebuddy
pip install -r requirements.txt
```

### Usage

```python
python transcribe.py --input classroom_sample.wav
```

This will run speech recognition on `classroom_sample.wav` and print the transcript.

See `transcribe.py` for example usage.

## Code Overview

- `transcribe.py`: Main script to run speech recognition 
- `model.py`: Functions to load pretrained Wav2Vec2 model
- `utils.py`: downloads audio files
- `sampleaudio.py`: processes audio files with 16000Hz sampling rate

## License

This project is unlicensed

## Acknowledgments

- [Facebook AI](https://github.com/pytorch/fairseq/tree/master/examples/wav2vec) for pretrained models
