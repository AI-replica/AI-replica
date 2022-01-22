""" A basic http server. """

import argparse
from http.server import HTTPServer
from server.request_handler import RequestHandler

from ai_replica.engine.reconstruct_mind import reconstruct
from server.read_config import config


DEFAULT_ADDRESS = "localhost"
DEFAULT_PORT = 8000

def run_server(
  server_class = HTTPServer, 
  handler_class = RequestHandler, 
  addr = DEFAULT_ADDRESS, 
  port = DEFAULT_PORT,
):
  server_address = (addr, port)
  httpd = server_class(server_address, handler_class)

  print(f"Starting httpd server on {addr}:{port}")
  httpd.serve_forever()

# parses command line arguments
def parse_arguments():
  parser = argparse.ArgumentParser(description = "Run a simple HTTP server")
  parser.add_argument(
    "-a",
    "--address",
    help = "Specify the IP address on which the server listens",
  )
  parser.add_argument(
    "-p",
    "--port",
    type = int,
    help = "Specify the port on which the server listens",
  )

  args = parser.parse_args()

  return args

def run():
  print("Reconstruction started.")
  reconstruct()
  print("Reconstruction completed.")

  args = parse_arguments()
  address = args.address if args.address != None else config["server"]["address"]
  port = args.port if args.port != None else config["server"]["port"]
  run_server(addr = address, port = port)

run()
