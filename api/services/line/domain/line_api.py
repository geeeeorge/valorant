from linebot import LineBotApi
from linebot.models import TextSendMessage
import os


class LineFacade:
    """LineBotApiを操作するFacade
    """

    def __init__(self, channel_access_token: str) -> None:
        self.line_bot_api = LineBotApi(channel_access_token)

    def get_user_id(self) -> str:
        profile = self.line_bot_api.get_profile()
        return profile.user_id

    def send_push_message(self, use_id: str, texts: list[str]) -> None:
        # TextSendMessageの型に変換
        messages = [TextSendMessage(text) for text in texts]
        self.line_bot_api.push_message(use_id, messages)


class GetUserIDAdapter:
    pass


class GetUserIDService:
    pass


class SendPushMessageAdapter:
    pass


class SendPushMessageService:
    pass
