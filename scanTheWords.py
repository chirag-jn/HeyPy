import requests
import json
from Recorder import record_audio, read_audio

API_ENDPOINT = 'https://api.wit.ai/speech'
wit_access_token = '3TCXNWEKWBFFOJBO344GLXMAMTWMJZBW'

def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    
    record_audio(num_seconds, AUDIO_FILENAME)
    audio = read_audio(AUDIO_FILENAME)
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    data = json.loads(resp.content)
    text = data['_text']
    return text