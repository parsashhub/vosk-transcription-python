from vosk import Model
from convertMp4toWav import convert_mp4_to_wav
from transcribeTextFromWav import transcribe_wav_to_text

# Define directories and model path
model_path = "path to vosk model"
model = Model(model_path)

path = convert_mp4_to_wav(mp4_file_path="path to your file")

transcribe_wav_to_text(wav_file_path=path, model=model)
