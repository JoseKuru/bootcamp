import os
from typing import Text
import gtts
import vlc
import time


def text_to_speech(text): 

    recog = gtts.gTTS(text=text , lang='es')
    recog.save('archivo.mp3')
    p = vlc.MediaPlayer("archivo.mp3")
    p.play()
