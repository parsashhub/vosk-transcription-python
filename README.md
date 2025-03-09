
# Vosk Transcription Python

This project uses the Vosk library for speech recognition and transcription in Python.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Install Required Packages](#install-required-packages)
  - [Install FFMPEG](#install-ffmpeg)
    - [Linux](#linux)
    - [macOS](#macos)
    - [Windows](#windows)
- [Usage](#usage)
- [License](#license)

## Introduction
Vosk Transcription Python is designed to provide easy-to-use tools for transcribing audio files using the Vosk speech recognition toolkit.

## Features
- Speech to text transcription
- Support for multiple languages
- Easy integration with Python projects

## Installation

To get started with this project, you need to have Python installed on your system. Follow the steps below to set up the project.

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Install Required Packages

You can install the required packages using the following command:

```bash
pip install pydub vosk
```

### Install FFMPEG

FFMPEG is required for audio processing. Follow the instructions below to install FFMPEG on your system.

#### Linux

For Debian-based distributions (like Ubuntu), you can install FFMPEG using:

```bash
sudo apt update
sudo apt install ffmpeg
```

For Red Hat-based distributions (like Fedora), you can install FFMPEG using:

```bash
sudo dnf install ffmpeg
```

#### macOS

You can install FFMPEG using Homebrew:

```bash
brew install ffmpeg
```

#### Windows

Download the latest static build of FFMPEG from the [FFmpeg website](https://ffmpeg.org/download.html) and follow these steps:

1. Extract the downloaded ZIP file to a folder (e.g., `C:\ffmpeg`).
2. Add the `bin` directory to your system PATH:
   - Open the Start menu, search for "Environment Variables," and select "Edit the system environment variables."
   - Click on "Environment Variables."
   - In the "System variables" section, select the "Path" variable and click "Edit."
   - Click "New" and add the path to the `bin` directory (e.g., `C:\ffmpeg\bin`).
   - Click "OK" to close all windows.

## Usage

Here is an example of how to use the Vosk Transcription Python project:

```python
from vosk import Model
from src.convertMp4toWav import convert_mp4_to_wav
from src.transcribeTextFromWav import transcribe_wav_to_text

# Define directories and model path
model_path = "path to vosk model"
model = Model(model_path)

path = convert_mp4_to_wav(mp4_file_path="path to your file")

transcribe_wav_to_text(wav_file_path=path, model=model)
```

## License

This project is licensed under the MIT License.