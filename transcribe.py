import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
import assemblyai as aai

#from pytube import YouTube
#url = "https://www.youtube.com/watch?v=_ZvnD73m40o&t=334s"
duration = 30
sample_rate= 44100
output_dir = "recordings"
os.makedirs(output_dir, exist_ok=True)
existing_files = os.listdir(output_dir)
next_file_number = len(existing_files) + 1
output_filename = os.path.join(output_dir, f"{next_file_number}st_rec.wav")

# Record audio
print(f"Recording audio for {duration} seconds...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()  # Wait for recording to complete
print("Recording finished.")

# Save the recorded audio as a WAV file
wav.write(output_filename, sample_rate, audio_data)

print(f"Audio saved as {output_filename}")

aai.settings.api_key = "xxxxxxxxxxxfill your api herexxxxxxxxxxxxx"
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(output_filename)
#transcript2 = transcriber.transcribe(url)
print(transcript.text)
