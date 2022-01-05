""" A basic http server. """

import argparse 

from http.server import HTTPServer
from server.request_handler import RequestHandler

from ai_replica.engine.reconstruct_mind import reconstruct


DEFAULT_ADDRESS = "localhost"
DEFAULT_PORT = 8000

def run_server(server_class = HTTPServer, handler_class = RequestHandler, addr = DEFAULT_ADDRESS, port = DEFAULT_PORT):
  server_address = (addr, port)
  httpd = server_class(server_address, handler_class)

  print(f"Starting httpd server on {addr}:{port}")
  httpd.serve_forever()

def parse_arguments():
  parser = argparse.ArgumentParser(description = "Run a simple HTTP server")
  parser.add_argument(
    "-a",
    "--address",
    default = DEFAULT_ADDRESS,
    help = "Specify the IP address on which the server listens",
  )
  parser.add_argument(
    "-p",
    "--port",
    type = int,
    default = DEFAULT_PORT,
    help = "Specify the port on which the server listens",
  )

  args = parser.parse_args()

  return args

def run():
  print("Reconstruction started.")
  reconstruct()
  print("Reconstruction completed.")

  args = parse_arguments()
  run_server(addr = args.address, port = args.port)

run()
