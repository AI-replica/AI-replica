''' 
This module converts text to speech! 
Note. It is not guaranteed that the data used to generate the speech will not leave the server as external api can be used.
Currently gTTS engine is used. https://gtts.readthedocs.io/en/latest/
TODO: use modules that provide text-to-speech capabilities without using external apis. E.g. https://pypi.org/project/pyttsx3/
'''

import os
from urllib.error import HTTPError
from gtts import gTTS, gTTSError
from server.read_config import config

STATIC_FILES_DIR = config['server']['static_files_dir']

def text_to_speech(text):
  language = 'en'
  try:
    speech = gTTS(text=text, lang=language, slow=False)
    if not os.path.exists(f"{STATIC_FILES_DIR}/generated"):
      os.mkdir(f"{STATIC_FILES_DIR}/generated")

    speech.save(f"{STATIC_FILES_DIR}/generated/text.mp3")
  except ConnectionError as error:
    print(f"[text_to_speech Error occured: {error}")
    pass
  except gTTSError as error:
    print(f"[text_to_speech Error occured: {error}")
    pass
  except HTTPError as error:
    print(f"[text_to_speech Error occured: {error}")
    pass
