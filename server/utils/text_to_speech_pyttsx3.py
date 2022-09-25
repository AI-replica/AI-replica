import os
import sys
import time
import pyttsx3
from server.utils.config import GENERATED_FILES_DIR


def text_to_speech(text: str, guid):
    try:
        engine = pyttsx3.init()
        # engine.say("I will speak this text")
        if not os.path.exists(GENERATED_FILES_DIR):
            os.mkdir(GENERATED_FILES_DIR)

        speech_file_path = os.path.join(GENERATED_FILES_DIR, f"{guid}.mp3")
        engine.save_to_file(text, speech_file_path)
        engine.runAndWait()
        while not os.path.exists(speech_file_path):
            time.sleep(1)
    except OSError as error:
        print(f"[text_to_speech Error occured: {error}", error.strerror)
    except:
        error = sys.exc_info()[0]
        print(f"[text_to_speech Error occured: {error}", error.message)
        pass
