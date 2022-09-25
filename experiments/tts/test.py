import subprocess
import sys
import os

# TODO: find a better way to run custom bot from Rasa's "bot" folder
# Need to append path to the "ai_repilca" folder to be able to make imports from the modules in that folder
ai_replica_dir_path = os.path.abspath(os.path.dirname(__file__) + "/../..")
sys.path.append(ai_replica_dir_path)

from ai_replica.utils.system import execute_command


execute_command(
    "../../venv/bin/tts",
    ["--text", "Hello. How are you doing?", "--out_path", "./speech.wav"],
    run_in_another_terminal7=False,
)

# subprocess.call(["tts", "--text", "Hello. How are you doing?", "--out_path", "./speech.mp3"])
