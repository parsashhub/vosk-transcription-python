import os
import wave
import json
from vosk import KaldiRecognizer


def transcribe_wav_to_text(wav_file_path, model, txt_file_path="./output/output.txt"):
    """
    Transcribes a single WAV file to a text file using the Vosk speech recognition model.

    Parameters:
        wav_file_path (str): The path to the input WAV file.
        txt_file_path (str): The path to the output text file.
        model (vosk.Model): The preloaded Vosk model for speech recognition.

    Returns:
        None
    """
    try:
        # Open the WAV file
        with wave.open(wav_file_path, "rb") as wf:
            # Check audio format
            if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000]:
                raise ValueError(f"Unsupported audio format for {wav_file_path}. Skipping.")

            print("transcribing...")
            # Initialize the recognizer
            recognizer = KaldiRecognizer(model, wf.getframerate())

            # Transcribe the audio
            transcription = ""
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    transcription += result.get("text", "") + " "

            # Get the final result
            final_result = json.loads(recognizer.FinalResult())
            transcription += final_result.get("text", "")

            # Write the transcription to a text file
            with open(txt_file_path, "w") as txt_file:
                txt_file.write(transcription.strip())

            print(f"Transcribed {wav_file_path} to {txt_file_path}")

    except ValueError as ve:
        print(ve)
    except Exception as e:
        raise RuntimeError(f"An error occurred while transcribing {wav_file_path}: {e}")
