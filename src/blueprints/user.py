from vkbottle.user import Blueprint, Message
from vkbottle import ABCRule

from src import config, wiki_parser

class FromUserRule(ABCRule[Message]):
    def __init__(self, user_id: int):
        self.user_id = user_id

    async def check(self, msg: Message) -> bool:
        return msg.from_id == self.user_id

bp = Blueprint("for user command")
bp.labeler.auto_rules = [FromUserRule(config.USER_ID)]

@bp.on.message(text=["/вики <item>"])
async def send_wiki_definition(msg: Message, item: str):
    await msg.reply(wiki_parser.get_definition(
        wiki_parser.term_to_wiki_url(item)
    ))
    await bp.api.messages.delete(msg.get_message_id(), delete_for_all=1, peer_id=msg.chat_id)
    