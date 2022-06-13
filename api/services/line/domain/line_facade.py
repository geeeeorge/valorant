import os

from aiolinebot import AioLineBotApi
from dotenv import load_dotenv
from linebot.models import TextSendMessage

from .send_push_message_adapter import SendPushMessageAdapter


class LineFacade:
    """LineBotApiを操作するFacade
    """

    def __init__(self) -> None:
        load_dotenv()
        self.line_bot_api = AioLineBotApi(os.environ.get("LINE_CHANNEL_ACCESS_TOKEN"))

    def send_push_message(self, adapter: SendPushMessageAdapter) -> None:
        # TextSendMessageの型に変換
        messages = [TextSendMessage(text) for text in adapter.texts]
        self.line_bot_api.push_message(adapter.user_id, messages)
