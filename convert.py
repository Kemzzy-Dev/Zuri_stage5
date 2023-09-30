import moviepy.editor as mp
import requests


def extract_audio(video_path):
    try:
        video_clip = mp.VideoFileClip(video_path)
        audio_clip = video_clip.audio
        
        file_parts = video_path.split(".")
        # Extract the word 
        audio_name = file_parts[0]

        audio_clip.write_audiofile(f'{audio_name}.mp3', codec='mp3')
        print('Audio extracted and saved successfully as MP3.')
    except Exception as e:
        print('Error:', str(e))

    return f"{audio_name}.mp3"

def getTranscribedAudio(audio):

    url = "https://whisper-speech-to-text1.p.rapidapi.com/speech-to-text"

    files = { "file": f"open({audio}, 'rb')" }
    headers = {
        "X-RapidAPI-Key": "7ef5e278bdmsh8f17098632358abp17f011jsn295d1fc4c6f6",
        "X-RapidAPI-Host": "whisper-speech-to-text1.p.rapidapi.com"
    }

    response = requests.post(url, files=files, headers=headers)

    return response.text
