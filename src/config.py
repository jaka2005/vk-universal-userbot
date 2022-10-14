from configparser import ConfigParser


_config = ConfigParser()
_config.read("./config.ini", encoding="utf-8")

TOKEN = _config["DEFAULT"]["token"]
USER_ID = int(_config["DEFAULT"]["user_id"])
SWEAR_WORDS = _config["DEFAULT"]["swear_words"].split("/")
