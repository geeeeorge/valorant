import os

from fastapi import Request
from linebot import WebhookParser

from ...application.line_api_usecase import LineApiUsecase
from ..exceptions import OverFiveTextError


class LineApiController:
    def __init__(self, usecase: LineApiUsecase) -> None:
        self.__usecase = usecase

    async def get_user_id(self, request: Request):
        parser = WebhookParser(channel_secret=os.environ.get("LINEBOT_CHANNEL_SECRET"))
        events = parser.parse(
            (await request.body()).decode("utf-8"),
            request.headers.get("X-Line-Signature", "")
        )
        return events[0].source.user_id

    def send_push_message(self, user_id: str, texts: list[str]) -> None:
        if len(texts) > 5:
            raise OverFiveTextError
        self.__usecase.send_push_message(user_id, texts)
