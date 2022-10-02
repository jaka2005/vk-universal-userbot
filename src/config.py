from configparser import ConfigParser


_config = ConfigParser()
_config.read("./config.ini")

TOKEN = _config["DEFAULT"]["token"]
USER_ID = int(_config["DEFAULT"]["user_id"])
