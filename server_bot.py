""" A basic http server. """

import argparse
from http.server import HTTPServer

from ai_replica.utils.system import kill_processes, get_python_exec_name
from server.request_handler import RequestHandler

from ai_replica.engine.reconstruct_mind import reconstruct
from server.read_config import config


DEFAULT_ADDRESS = "localhost"
DEFAULT_PORT = 8000


def run_server(
    server_class=HTTPServer,
    handler_class=RequestHandler,
    addr=DEFAULT_ADDRESS,
    port=DEFAULT_PORT,
):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Server listening on {addr}:{port} ...")
    httpd.serve_forever()


def stop_server(python_version):
    python_name = get_python_exec_name(python_version=python_version)
    ident = f"{python_name} server_bot.py"
    kill_processes(expected_command_line_part=ident, sleep_sec=10)
    print("Stopped the basic server")


# parses command line arguments
def parse_arguments():
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
    # TODO: move reconstruction into a more suitable place. Probably, it makes sense to run reconstruction as a separate script before starting the server.
    # E.g. python train_bot.py. And when server is run, already trained model is loaded and consumed by clients.
    # In a gereral case, training the model can take a lot of time, so makses sense to do it separately, as a preliminary step.
    print("Reconstruction started.")
    reconstruct()
    print("Reconstruction completed.")

    args = parse_arguments()
    address = args.address if args.address != None else config["server"]["address"]
    port = args.port if args.port != None else config["server"]["port"]
    run_server(addr=address, port=port)


if __name__ == "__main__":
    run()
