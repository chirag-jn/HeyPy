def startrec():
	import pyaudio
	import wave

	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "output.wav"

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
	                channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

def watson_run(usr, passd):
	import requests
	import os
	import json
	startrec()
	url = "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?timestamps=false&max_alternatives=0"
	headers = {"Content-Type": "audio/wav"}
	# payload = {'data-binary':"@~/Downloads/watson/audio-file.flac"}
	# r = requests.post("https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?timestamps=true&max_alternatives=3", data={'header': "Content-Type: audio/flac", 'data-binary': '~/Downloads/watson/audio-file.flac'}, auth=("b2aca159-86a0-4afa-9b22-4b720ee1957f", "vTSl6VKjZMPA"))
	user = usr
	passwd = passd
	audio_file = os.path.abspath('') + '/output.wav'
	audio = open(audio_file, 'rb')
	r = requests.post(url, data=audio, headers=headers, auth=(user, passwd))
	# print(r.text)
	trans = json.loads(r.text)
	returned = trans["results"][0]['alternatives'][0]['transcript']
	return returned