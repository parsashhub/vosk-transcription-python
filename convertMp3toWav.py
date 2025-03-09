import os
from pydub import AudioSegment


def convert_mp3_to_wav(mp3_file_path, output_dir="./output"):
    """
    Converts a single MP3 file to WAV format.

    Parameters:
        mp3_file_path (str): The full path to the MP3 file to be converted.

    Returns:
        str: The path to the converted WAV file.
    """
    if not mp3_file_path.endswith('.mp3'):
        raise ValueError("The input file must have a .mp3 extension.")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        print("converting mp3 to wav...")
        # Extract directory and generate WAV file name
        directory = os.path.dirname(mp3_file_path)
        wav_filename = os.path.basename(mp3_file_path).replace(".mp3", ".wav")
        wav_path = os.path.join(output_dir, wav_filename)

        # Load the MP3 file and convert to WAV
        audio = AudioSegment.from_mp3(mp3_file_path)
        # Convert to the correct format for Vosk:
        # - Mono (1 channel)
        # - 16-bit PCM
        # - Sample rate of 16000 Hz (or 8000 Hz)
        audio = audio.set_channels(1)  # Convert to mono
        audio = audio.set_frame_rate(16000)  # Set sample rate to 16000 Hz
        audio = audio.set_sample_width(2)  # Set sample width to 2 bytes (16-bit)

        audio.export(wav_path, format="wav")

        print(f"Converted {os.path.basename(mp3_file_path)} to {wav_filename}")
        return wav_path
    except Exception as e:
        raise RuntimeError(f"An error occurred while converting {mp3_file_path}: {e}")
