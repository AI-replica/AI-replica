""" A basic http server. Processes requests from UI chat. """

import argparse
import os
from ai_replica.utils.system import kill_processes, get_python_exec_name
from server.utils.read_config import config
import server.data_access.data_access as data_access
from server.app import app
from server.utils.remove_speech_files import remove_outdated_speech_files_on_schedule


def stop_server(python_version=None):
    python_name = get_python_exec_name(python_version=python_version)
    ident = f"{python_name} server_bot.py"
    kill_processes(expected_command_line_part=ident, sleep_sec=10)
    print("Stopped the basic server")


def parse_arguments():
    """Parses command line arguments."""
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-a",
        "--address",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="Specify the port on which the server listens",
    )

    args = parser.parse_args()

    return args


def run():
    data_access.ensure_tables_exist()
    args = parse_arguments()
    address = args.address if args.address != None else config["server"]["address"]
    port = args.port if args.port != None else config["server"]["port"]

    remove_outdated_speech_files_on_schedule()
    print("Outdated speech files remover started.")

    server_mode = os.environ.get("SERVER_MODE")
    print("SERVER_MODE", server_mode)
    dev = True if server_mode == "development" else False
    debug = True if server_mode == "development" else False

    app.run(host=address, port=port, access_log=True, dev=dev, debug=debug)
    print("Server started.")


if __name__ == "__main__":
    run()
