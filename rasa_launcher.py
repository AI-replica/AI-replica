"""Makes all the necessary preparations to launch Rasa, and launches it.
It relies on some linux-specific logic, and thus might not work in another OS.

How to use:
0. cd to the AI-replica dir
1. python3 rasa_launcher.py
2. After some time, the default browser will be opened, with the GUI to chat with the bot

To get help on the command line arguments, run:
python3 rasa_launcher.py -h

"""

import sys
import time
import argparse
from server.read_config import config


from ai_replica.utils.system import (
    execute_command,
    open_url_in_browser,
    is_expected_python_version, get_python_exec_name, install_replica_dependencies,
)
from rasa.utils import (
    start_rasa_actions_server,
    start_rasa_main_server,
    train_model,
    stop_a_rasa_server, install_rasa_dependencies,
)

from server_bot import stop_server as stop_basic_server


required_python = config["system"]["preferred_python_version"]
expected_launch_duration_sec = config["rasa"]["expected_launch_duration_sec"]


def print_notifications():
    if "linux" in sys.platform and is_expected_python_version(required_python):
        print("Detected the right OS and python version, which is nice.")
    else:
        print(f"Note: this script was tested in linux and Python {required_python}")
        print("It might work incorrectly in other environments.")

    print("Note: if you close this terminal, the server stuff will continue to run")


def restart_servers(rasa_path, work_dir, args):
    launch_bools = {
        "basic": args.basic,
        "main_rasa": args.main_rasa,
        "actions_rasa": args.actions_rasa,
    }

    if any(launch_bools.values()):
        print(f"Restarting only the specified servers: {launch_bools}")
    else:
        print("You didn't specify which server to restart, so I restart them all.")
        print("I'll also retrain the model.")
        launch_bools = dict.fromkeys(launch_bools, True)
        train_model(rasa_path, work_dir)

    if launch_bools["main_rasa"]:
        stop_a_rasa_server(rasa_path, server_name="main")
        start_rasa_main_server(rasa_path, work_dir)

    if launch_bools["actions_rasa"]:
        stop_a_rasa_server(rasa_path, server_name="actions")
        start_rasa_actions_server(rasa_path, work_dir)

    if launch_bools["basic"]:
        stop_basic_server(python_version=required_python)
        build_web_chat()
        python_name = get_python_exec_name(python_version=required_python)
        execute_command(python_name, "server_bot.py", run_in_another_terminal7=True)

def build_web_chat():
    python_name = get_python_exec_name(python_version=required_python)
    execute_command(python_name, "build_web_chat.py", run_in_another_terminal7=False)

def parse_arguments():
    # TODO: add an argument: just shut down all the servers etc, without launching anything

    description = "Makes all the necessary preparations to launch Rasa, and launches it"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-b",
        "--basic_restart",
        dest="basic",
        action="store_true",
        help="Restarts the BASIC server. If not specified, every server will be restarted",
    )
    parser.add_argument(
        "-a",
        "--actions_restart",
        dest="actions_rasa",
        action="store_true",
        help="Restarts the ACTIONS server of Rasa. If not specified, every server will be restarted",
    )
    parser.add_argument(
        "-m",
        "--main_restart",
        dest="main_rasa",
        action="store_true",
        help="Restarts the MAIN server of Rasa. If not specified, every server will be restarted",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    cmd_args = parse_arguments()
    print_notifications()

    install_replica_dependencies(required_python)
    exec_rasa, work_dir_rasa = install_rasa_dependencies(required_python)
    restart_servers(exec_rasa, work_dir_rasa, cmd_args)

    time.sleep(expected_launch_duration_sec)
    open_url_in_browser("http://localhost:8000/")
