import speech_recognition as speechAI




class SpeechAI(object):
    def __init__(self,threshold=0.30,lex=False,phrase="hello"):
        self.phrase = phrase
        self.lex = lex
        self.threshold = threshold

    def recognize(self,recognize,audio):
        spoken = None
        transcript=""
        try:
            if(self.lex==False):
                min_conf = 1
                spoken = recognize.recognize_google(audio,language = "en-IN",show_all=True)
                print(spoken)
                if spoken != []:
                    for i in spoken['alternative']:
                        if 'confidence' not in list(i.keys()):
                            transcript = spoken['alternative'][0]['transcript']
                            print("YOU SAID " + i['transcript'])
                            return transcript
                        elif i['confidence'] <= min_conf and i['confidence'] >= self.threshold:
                            min_conf = i['confidence']
                    for i in spoken['alternative']:
                        if i['confidence'] == min_conf:
                            transcript = i['transcript']
                            print("YOU SAID "+ i['transcript'])
                            break
                else:
                    print("Recongnizer: Nothing Spoken")
                    return ""
            else:
                min_conf = 1
                spoken = recognize.recognize_google(audio,language = "en-IN",show_all=True)
                print(spoken)
                outcomes = []
                if spoken != []:
                    for i in spoken['alternative']:
                        if 'confidence' not in list(i.keys()):
                            transcript = spoken['alternative'][0]['transcript']
                            print("YOU SAID "+i['transcript'])
                            return transcript
                        elif i['confidence']<=min_conf and i['confidence']>=self.threshold:
                            min_conf = i['confidence']
                    for i in spoken['alternative']:
                        if i['confidence']==min_conf:
                            outcomes.append(i['transcript'])
                    outcomes.sort()
                    print(outcomes)
                    transcript = outcomes[0]
                    print("YOU SAID " + transcript)
                else:
                    print("Recongnizer: Nothing Spoken")
                    return ""

        except speechAI.UnknownValueError:
            print("Recongnizer: UnknownValueError")
            return None
        except speechAI.RequestError as e:
            print("Recongnizer: Could not request results from Google Speech Recognition service; {0}".format(e))
            return None
        return transcript

    def ears(self):
        micro_source = speechAI.Microphone()
        record = speechAI.Recognizer()
        with micro_source as source:
            record.adjust_for_ambient_noise(source,duration=2)
            record.dynamic_energy_threshold = True
            print("Recognizer: I am all Ears!")
            audio = record.listen(source)
            print("Recognizer: Finished listening")
        return record,audio

if __name__=="__main__":
    #F = faceAI.faceAI(camera=0)
    S = SpeechAI(0.30,phrase="okay mirror")
    while True:
            record,audio = S.ears()
            S.recognize(record,audio)
