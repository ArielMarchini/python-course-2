from gtts import gTTS
import os

tts = gTTS(text="first time i'm using a package in next.py course ", lang="en")
filename = "hello2.mp3"
tts.save(filename)
os.system(f"start {filename}")