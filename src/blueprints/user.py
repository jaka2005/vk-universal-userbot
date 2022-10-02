from vkbottle.user import Blueprint, Message
from vkbottle import ABCRule, BaseMiddleware

from src import config, wiki_parser

class FromUserRule(ABCRule[Message]):
    def __init__(self, user_id: int):
        self.user_id = user_id

    async def check(self, msg: Message) -> bool:
        return msg.from_id == self.user_id

class UserCommand(BaseMiddleware[Message]):
    async def pre(self):
        if self.event.from_id != config.USER_ID:
            self.stop("it's not from registered user")

    async def post(self):
        if self.handlers:
            await bp.api.messages.delete(
                self.event.get_message_id(),
                peer_id=self.event.chat_id,
                delete_for_all=1
            )
        

bp = Blueprint("for user command")
bp.labeler.message_view.register_middleware(UserCommand)

@bp.on.message(text=["/вики <item>", "/wiki <item>"])
async def send_wiki_definition(msg: Message, item: str):
    await msg.reply(wiki_parser.get_definition(
        wiki_parser.term_to_wiki_url(item)
    ))

@bp.on.message(text=["> <item>"])
def solve_expression(msg: Message, item: str):
    ...
    