from ..domain.line_api import SendPushMessageService


class LineApiUsecase:
    def __init__(self) -> None:
        pass

    def send_push_message(self, user_id: str, texts: list[str]) -> None:
        SendPushMessageService()(user_id, texts)
