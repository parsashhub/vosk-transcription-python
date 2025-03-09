import os
from pydub import AudioSegment


def convert_mp4_to_wav(mp4_file_path, output_dir="./output"):
    """
    Converts a single MP4 file to a WAV file formatted for Vosk.

    Parameters:
        mp4_file_path (str): The full path to the MP4 file to be converted.
        output_dir (str): The directory where the WAV file will be saved.

    Returns:
        str: The path to the converted WAV file.
    """
    if not mp4_file_path.endswith(".mp4"):
        raise ValueError("The input file must have a .mp4 extension.")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    try:
        print("converting mp4 to wav...")
        # Extract the WAV filename
        wav_filename = os.path.basename(mp4_file_path).replace(".mp4", ".wav")
        wav_path = os.path.join(output_dir, wav_filename)

        # Load the MP4 file and extract audio
        audio = AudioSegment.from_file(mp4_file_path, format="mp4")

        # Convert to the correct format for Vosk:
        # - Mono (1 channel)
        # - 16-bit PCM
        # - Sample rate of 16000 Hz
        audio = audio.set_channels(1)  # Convert to mono
        audio = audio.set_frame_rate(16000)  # Set sample rate to 16000 Hz
        audio = audio.set_sample_width(2)  # Set sample width to 2 bytes (16-bit)

        # Export as WAV
        audio.export(wav_path, format="wav")
        print(f"Converted {os.path.basename(mp4_file_path)} to {wav_filename}")

        return wav_path
    except Exception as e:
        raise RuntimeError(f"An error occurred while converting {mp4_file_path}: {e}")
