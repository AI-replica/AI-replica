""" A basic http server. Processes requests from UI chat. """

import argparse
from http.server import HTTPServer
from ai_replica.utils.system import kill_processes, get_python_exec_name
from server.request_handler import RequestHandler
from server.read_config import config
import server.data_access as data_access


def run_server(
    server_class=HTTPServer,
    handler_class=RequestHandler,
    addr=None,
    port=None
):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Server listening on {addr}:{port} ...")
    httpd.serve_forever()


def stop_server(python_version=None):
    python_name = get_python_exec_name(python_version=python_version)
    ident = f"{python_name} server_bot.py"
    kill_processes(expected_command_line_part=ident, sleep_sec=10)
    print("Stopped the basic server")


def parse_arguments():
    ''' Parses command line arguments. '''
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
    run_server(addr=address, port=port)


if __name__ == "__main__":
    run()
