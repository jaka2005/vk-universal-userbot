'''just run it ¯\_(ツ)_/¯'''
from vkbottle.user import User

from src import blueprints
from src.config import config

bot = User(config.init.token)

for bp in blueprints.blueprints:
    bp.load(bot)

print("Started!")
bot.run_forever()
