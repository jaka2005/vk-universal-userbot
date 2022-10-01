from vkbottle.user import Blueprint, Message
from vkbottle import ABCRule

from src import config, wiki_parser

class ItsMeRule(ABCRule[Message]):
    async def check(self, msg: Message) -> bool:
        return msg.from_id == config.USER_ID

bp = Blueprint("for user command")
bp.labeler.auto_rules = [ItsMeRule()]

@bp.on.message(text=["/wiki <item>"])
async def send_wiki_definition(msg: Message, item: str):
    await msg.reply(wiki_parser.get_definition(
        wiki_parser.term_to_wiki_url(item)
    ))
    await bp.api.messages.delete(msg.get_message_id(), delete_for_all=1, peer_id=msg.chat_id)
    