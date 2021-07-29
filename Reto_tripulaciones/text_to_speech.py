import os
from typing import Text
import gtts
import vlc
import time

with open('texto.txt', 'r') as file:
    text = file.read()

recog = gtts.gTTS(text=text , lang='es')
recog.save('prueba.mp3')

p = vlc.MediaPlayer("prueba.mp3")
p.play()

time.sleep(10)