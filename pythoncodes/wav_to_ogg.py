#!/usr/bin/python3
import sys
from pydub import AudioSegment

# Check if the correct number of arguments was provided
if len(sys.argv) != 3:
    print("Usage: ./convert_wav_to_ogg.py <input_file.wav> <output_file.ogg>")
    sys.exit(1)

# Assign the file names from the command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Convert WAV to OGG
audio = AudioSegment.from_wav(input_file)
audio.export(output_file, format='ogg')
print(f"Converted {input_file} to {output_file}")
