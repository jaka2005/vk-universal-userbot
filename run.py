from vkbottle.user import User

from src import blueprints, config

bot = User(config.TOKEN)

for bp in blueprints.blueprints:
    bp.load(bot)

print("Started!")
bot.run_forever()
