from app import app
from helpers import load_config

config = load_config()

from routes import *

HOST = config["host"]
PORT = config["port"]
DEBUG = config["debug"]

if __name__ == "__main__":
  app.run(
    host = HOST,
    port = PORT,
    debug = DEBUG)