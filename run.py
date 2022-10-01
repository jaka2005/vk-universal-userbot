from configparser import ConfigParser
from vkbottle.bot import Bot


config = ConfigParser().read("config.ini")
bot = Bot(config["token"])

print("Started!")
bot.run_forever()