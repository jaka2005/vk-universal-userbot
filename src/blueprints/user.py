from vkbottle.user import Blueprint, Message
from vkbottle import BaseMiddleware

from src import wiki_parser
from src.config import config


class UserCommand(BaseMiddleware[Message]):
    async def pre(self):
        if self.event.from_id != config.init.user_id:
            self.stop("it's not from registered user")

    async def post(self):
        if self.handlers:
            await bp.api.messages.delete(
                self.event.get_message_id(),
                peer_id=self.event.peer_id,
                delete_for_all=True
            )


bp = Blueprint("for user command")
bp.labeler.message_view.register_middleware(UserCommand)


@bp.on.message(text=("/вики <item>", "/wiki <item>"))
async def send_wiki_definition(msg: Message, item: str):
    await msg.reply(wiki_parser.get_definition(
        wiki_parser.term_to_wiki_url(item)
    ))


@bp.on.message(text="! <item>")
async def solve_expression(msg: Message, item: str):
    try:
        res = eval(item)
        await msg.reply(f"res: {res.__class__.__name__} = {res}")

    except Exception as e:
        await msg.reply(f"{e.__class__.__name__}: {e}")


@bp.on.message(func=lambda msg: any(
    word in msg.text.lower() for word in config.preferences.swear_words
))
async def dirty_censoring(msg: Message):
    text = msg.text
    
    indexes = []
    for index, letter in enumerate(text):
        if letter.isupper():
            indexes.append(index)
    
    text = text.lower()
    for word in config.preferences.swear_words:
        text = text.replace(word, word[0] + "*" * (len(word) - 2) + word[-1])
    
    chars = list(text)
    for index in indexes:
        chars[index] = chars[index].upper()

    await msg.answer("".join(chars))
