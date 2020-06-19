#!/usr/bin/env python3
from gtts import gTTS
import pygame
from io import BytesIO
import subprocess
import time
from pathlib import Path
import os


database_file_name = ".howtosayDB.txt"


pygame.init()


def say(text):
    """ Based off of https://github.com/pndurette/gTTS/issues/26#issuecomment-552242214
    """
    tts = gTTS(text=text, lang="en") #TODO: Support language detection
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    time.sleep(1)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def save_to_database(clipboard: str, filename: str):
    home = str(Path.home())
    filename_with_path = os.path.join(home, filename)
    with open(filename_with_path, 'a+') as f:
        f.write(clipboard + "\n")


def main():
    clipboard = subprocess.check_output(["pbpaste"], text=True)
    print(clipboard)
    save_to_database(clipboard, database_file_name)
    say("how to say " + clipboard)


if __name__ == "__main__":
    main()