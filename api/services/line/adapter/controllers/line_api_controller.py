from ...application.line_api_usecase import LineApiUsecase


class LineApiController:
    def __init__(self, usecase: LineApiUsecase) -> None:
        self.usecase == usecase

    def send_push_message(self, user_id: str, texts: list[str]) -> None:
        self.usecase.send_push_message(user_id, texts)
