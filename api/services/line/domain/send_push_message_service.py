from .send_push_message_adapter import SendPushMessageAdapter


class SendPushMessageService:

    def __call__(self, user_id: str, texts: list[str]) -> None:
        SendPushMessageAdapter().requests(user_id, texts)
