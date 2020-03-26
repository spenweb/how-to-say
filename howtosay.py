#!/usr/bin/env python3
from gtts import gTTS
import pygame
from io import BytesIO
import subprocess
import time

pygame.init()

""" Based off of https://github.com/pndurette/gTTS/issues/26#issuecomment-552242214
"""
def say(text):
  tts = gTTS(text=text, lang='en')
  fp = BytesIO()
  tts.write_to_fp(fp)
  fp.seek(0)
  pygame.mixer.init()
  pygame.mixer.music.load(fp)
  time.sleep(1)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

def main():
  clipboard = subprocess.check_output(["pbpaste"], text=True)
  print(clipboard)
  say("how to say " + clipboard)

if __name__ == "__main__":
  main()