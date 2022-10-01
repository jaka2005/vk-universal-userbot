from configparser import ConfigParser


config = ConfigParser()
config.read("./config.ini")

TOKEN = config["DEFAULT"]["token"]
USER_ID = int(config["DEFAULT"]["user_id"])
