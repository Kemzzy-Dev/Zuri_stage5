import requests
from deepgram import Deepgram
import json
import subprocess
from dotenv import load_dotenv
import os


def extract_audio(video_path):
    try:
        file_parts = video_path.split("/")
        file_parts2 = file_parts[1].split(".")
        # Extract the word 
        audio_name = file_parts2[0]

        audio_path = f'audio/{audio_name}.wav'

        subprocess.run(['ffmpeg', '-i', video_path, '-q:a', '0', '-map', 'a', audio_path])    
        print('Audio extracted and saved successfully as wav.')
    except Exception as e:
        print('Error:', str(e))

    return audio_path

def getTranscribedAudio(audio_file):

    api_key = os.getenv('DEEPGRAM_API_KEY')
    PATH_TO_FILE = audio_file

        # Initializes the Deepgram SDK
    deepgram = Deepgram(api_key)
    try:
        # Open the audio file
        with open(PATH_TO_FILE, 'rb') as audio:
            # ...or replace mimetype as appropriate
            source = {'buffer': audio, 'mimetype': 'audio/wav'}
            response = deepgram.transcription.sync_prerecorded(source, {'punctuate': True})
            # Access the transcript
            transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
        
        return transcript

    except Exception as e:
        print('Error: ', str(e))

    
