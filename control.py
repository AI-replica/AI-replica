"""
Contains useful commands to work with the bot and the server. Used by make tool.
It relies on some linux-specific logic, and thus might not work in another OS.
"""

import sys
import time
import argparse
from server.utils.read_config import config
from ai_replica.engine.reconstruct_mind import reconstruct
from ai_replica.utils.system import (
    execute_command,
    open_url_in_browser,
    is_expected_python_version,
    get_python_exec_name,
    install_replica_dependencies,
)
from rasa.utils import (
    start_rasa_actions_server,
    start_rasa_main_server,
    train_model,
    stop_a_rasa_server,
    install_rasa_dependencies,
    get_paths as get_rasa_paths,
)

rasa_required_python = config["system"]["rasa_preferred_python_version"]
expected_launch_duration_sec = config["rasa"]["expected_launch_duration_sec"]
web_chat_url = config["server"]["web_chat_url"]


def print_notifications():
    if "linux" in sys.platform and is_expected_python_version(rasa_required_python):
        print("Detected the right OS and python version, which is nice.")
    else:
        print(
            f"Note: this script was tested in linux and Python {rasa_required_python}"
        )
        print("It might work incorrectly in other environments.")
        print("Note: if you close this terminal, the server stuff will continue to run")


def start_rasa_server(rasa_path, work_dir):
    stop_a_rasa_server(rasa_path, server_name="main")
    start_rasa_main_server(rasa_path, work_dir)


def start_rasa_server_with_debug_logs(rasa_path, work_dir):
    stop_a_rasa_server(rasa_path, server_name="main")
    start_rasa_main_server(
        rasa_path,
        work_dir,
        "--debug",
    )


def start_rasa_actions_with_debug_logs(rasa_path, work_dir):
    stop_a_rasa_server(rasa_path, server_name="actions")
    start_rasa_actions_server(
        rasa_path,
        work_dir,
        "--debug",
    )


def restart_servers(rasa_path, work_dir, launch_bools):
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
        # Importing it here to avoid problems with requirements installation automation
        from server_bot import stop_server as stop_basic_server

        stop_basic_server()
        # build_web_chat()
        python_name = get_python_exec_name()
        execute_command(python_name, "server_bot.py", run_in_another_terminal7=True)


# Now the web chat requires Node.js. Also, the pre-built chat is included into the source files.
# def build_web_chat():
#     python_name = get_python_exec_name()
#     execute_command(python_name, "build_web_chat.py", run_in_another_terminal7=False)


def parse_arguments():
    description = "Makes all the necessary preparations to launch Rasa, and launches it"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("command", nargs="?", help="Command to execute")
    args = parser.parse_args()

    return args


def execute_control_command():
    cmd_args = parse_arguments()
    print_notifications()
    rasa_paths = get_rasa_paths()
    args = {
        "main_rasa": False,
        "actions_rasa": False,
        "basic": False,
    }

    command = cmd_args.command
    if command == None:
        print("Default command: currently no default command defined.")
    elif command == "install_dependencies":
        install_replica_dependencies(rasa_required_python)
        install_rasa_dependencies(rasa_required_python)
    elif command == "rasa_launcher":
        install_replica_dependencies(rasa_required_python)
        exec_rasa, work_dir_rasa = install_rasa_dependencies(rasa_required_python)
        restart_servers(exec_rasa, work_dir_rasa, args)

        time.sleep(expected_launch_duration_sec)
        open_url_in_browser(web_chat_url)
    elif command == "reconstruct_mind":
        print("Reconstruction started.")
        reconstruct()
        print("Reconstruction completed.")
    elif command == "start_rasa_server":
        start_rasa_server(
            rasa_paths["rasa_exec_path_abs"], rasa_paths["working_dir_abs"]
        )
    elif command == "start_rasa_server_with_debug_logs":
        start_rasa_server_with_debug_logs(
            rasa_paths["rasa_exec_path_abs"], rasa_paths["working_dir_abs"]
        )
    elif command == "start_rasa_actions":
        args["actions_rasa"] = True
        restart_servers(
            rasa_paths["rasa_exec_path_abs"], rasa_paths["working_dir_abs"], args
        )
    elif command == "start_rasa_actions_with_debug_logs":
        start_rasa_actions_with_debug_logs(
            rasa_paths["rasa_exec_path_abs"], rasa_paths["working_dir_abs"]
        )
    elif command == "start_server":
        args["basic"] = True
        restart_servers(
            rasa_paths["rasa_exec_path_abs"], rasa_paths["working_dir_abs"], args
        )
    elif command == "start_ui":
        open_url_in_browser(web_chat_url)
    elif command == "train_core_model":
        print("Training started.")
        reconstruct()
        print("Training completed.")
    elif command == "train_rasa_model":
        print("Training Rasa model...", rasa_paths)
        train_model(rasa_paths["rasa_exec_path_abs"], rasa_paths["working_dir_abs"])
        print("Training Rasa model completed.")
    else:
        print("Invalid command", cmd_args.command)


if __name__ == "__main__":
    execute_control_command()
