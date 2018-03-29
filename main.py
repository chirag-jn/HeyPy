# user = "b2aca159-86a0-4afa-9b22-4b720ee1957f"
# passwd = "vTSl6VKjZMPA"

from wit import Wit

client =  Wit('3TCXNWEKWBFFOJBO344GLXMAMTWMJZBW')

from test2 import parse
from scanTheWords import RecognizeSpeech

# resp = None
# with open('output.wav', 'rb') as f:
# 	resp = client.speech(f,None, {'Content-Type': 'audio/wav'})
# print(str(resp))

cmd = RecognizeSpeech('output.wav',5)
print(cmd)
parse(cmd)
