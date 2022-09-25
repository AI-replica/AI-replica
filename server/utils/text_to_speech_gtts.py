""" 
This module converts text to speech! 
Note. It is not guaranteed that the data used to generate the speech will not leave the server as external api can be used.
Currently gTTS engine is used. https://gtts.readthedocs.io/en/latest/
TODO: use modules that provide text-to-speech capabilities without using external apis. E.g. https://pypi.org/project/pyttsx3/
"""

import os
from urllib.error import HTTPError
from gtts import gTTS, gTTSError
from server.utils.config import GENERATED_FILES_DIR


def text_to_speech(text: str, guid):
    language = "en"
    try:
        speech = gTTS(text=text, lang=language, slow=False)
        if not os.path.exists(GENERATED_FILES_DIR):
            os.mkdir(GENERATED_FILES_DIR)

        speech_file_path = os.path.join(GENERATED_FILES_DIR, f"{guid}.mp3")
        speech.save(speech_file_path)
    except ConnectionError as error:
        print(f"[text_to_speech Error occured: {error}")
        pass
    except gTTSError as error:
        print(f"[text_to_speech Error occured: {error}")
        pass
    except HTTPError as error:
        print(f"[text_to_speech Error occured: {error}")
        pass
