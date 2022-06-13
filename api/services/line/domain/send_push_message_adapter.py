from .line_facade import LineFacade


class SendPushMessageAdapter:
    user_id: str
    texts: list[str]
    line_facade: LineFacade = LineFacade()

    def requests(self, user_id: str, texts: list[str]) -> None:
        self.user_id = user_id
        self.texts = texts
        self.line_facade.send_push_message(self)
