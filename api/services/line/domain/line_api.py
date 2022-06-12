import os

from aiolinebot import AioLineBotApi
from dotenv import load_dotenv
from linebot.models import TextMessage, TextSendMessage


class LineFacade:
    """LineBotApiを操作するFacade
    """

    def __init__(self) -> None:
        load_dotenv()
        self.line_bot_api = AioLineBotApi(os.environ.get("LINE_CHANNEL_ACCESS_TOKEN"))

    def get_user_id(self) -> str:
        profile = self.line_bot_api.get_profile()
        return profile.user_id

    def send_push_message(self, adapter: SendPushMessageAdapter) -> None:
        # TextSendMessageの型に変換
        messages = [TextSendMessage(text) for text in adapter.texts]
        self.line_bot_api.push_message(adapter.user_id, messages)

    def reply_message_async(self, user_id: str, texts: list[str]) -> None:
        messages = [TextMessage(text) for text in texts]
        self.line_bot_api.reply_message_async(user_id, messages)


class GetUserIDAdapter:
    pass


class GetUserIDService:
    pass


class SendPushMessageAdapter:
    user_id: str
    texts: list[str]
    line_facade: LineFacade = LineFacade()

    def requests(self, user_id: str, texts: list[str]) -> None:
        self.user_id = user_id
        self.texts = texts
        self.line_facade.send_push_message(self)


class SendPushMessageService:

    def __call__(self, user_id: str, texts: list[str]) -> None:
        SendPushMessageAdapter.requests(user_id, texts)
