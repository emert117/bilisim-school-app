import os
import json


def load_config() -> dict:
  path = os.path.join(".", "config.json")

  with open(path, "r", encoding = "UTF-8") as config:
    return json.loads(config.read())