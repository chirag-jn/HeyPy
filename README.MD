HeyPy

Idea :

-An app which provides you python code for the pseudo code you speak.
-Provides users a handy tool for writing hundreds of lines of code in just few minutes.
-Programmed with easy and informal voice commands.

Technology Stack :

-Python 
-Watson Speech to Text - IBM
-Wit.ai

How is our product helpful?

Reduces time wasted on debugging syntax errors
Speeds up the process of coding
Saves time for searching code on StackOverflow, Codota

Future Plans :

-Use Natural Language Processing for more accuracy in converting speech to text.
-Provide code implementations in other programming languages
-Code optimization and suggest more efficient algorithms of pseudo-code to users
-Simultaneous error checking and prompts.

Implementation :

-Voice from microphone converted to text using Watson Speech To Text.
-Errors removed from text using Wit.Ai
-Parsed operators and numbers to mathematical terms 
-Converted pseudo code to python code

Setup :

```bash
  git clone https://github.com/chirag-jn/ByldHackv13/
  cd ByldHackv13
  sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
  sudo apt-get install ffmpeg libav-tools
  sudo pip3 install pyaudio
  python3 -m pip install -r requirements.txt
  python3 main.py
```


