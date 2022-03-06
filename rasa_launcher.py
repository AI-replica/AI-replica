"""Makes all the necessary preparations to launch Rasa, and launches it.
It relies on some linux-specific logic, and thus might not work in another OS.

How to use:
0. cd to the AI-replica dir
1. python3 rasa_launcher.py
2. After some time, the default browser will be opened, with the GUI to chat with the bot
"""

import sys
import time

from ai_replica.utils.system import (
    create_env_if_not_exist,
    install_piped_requirements,
    execute_command,
    open_url_in_browser, is_expected_python_version,
)
from rasa.utils import (
    get_rasa_paths,
    start_rasa_actions_server,
    start_rasa_main_server,
    train_model,
)

required_python = "3.8"  # Rasa does not support later versions yet, as of Jan 2022
expected_launch_duration_sec = 30  # # to avoid opening the browser-UI too early

if __name__ == "__main__":
    if "linux" in sys.platform and is_expected_python_version(required_python):
        print("Detected the right OS and python version, which is nice.")
    else:
        print(f"""Note: this script was tested in linux and Python {required_python}.
        It might work incorrectly in other circumstances.""")
    print("Note: if you close this terminal, the server stuff will continue to run")

    venv_dir, working_dir, requirements, rasa_exec, pip_exec = get_rasa_paths()

    create_env_if_not_exist(venv_dir)
    install_piped_requirements(pip_exec, requirements)

    train_model(rasa_exec, working_dir)
    start_rasa_main_server(rasa_exec, working_dir)
    start_rasa_actions_server(rasa_exec, working_dir)

    execute_command("python3", "server_bot.py")
    time.sleep(expected_launch_duration_sec)
    open_url_in_browser("http://localhost:8000/")
