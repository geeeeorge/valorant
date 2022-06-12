import os

from fastapi import APIRouter, BackgroundTasks, Request
from linebot import WebhookParser

from ...adapter.controllers.healthz import HealthzController
from ...adapter.controllers.line_api_controller import LineApiController

# parser = WebhookParser(channel_secret=os.environ.get("LINEBOT_CHANNEL_SECRET"))


def get_route(
    healthz_controller: HealthzController,
    line_api_controller: LineApiController,
) -> APIRouter:
    router = APIRouter(
        prefix="/api/line/v1",
        tags=["line"],
        responses={404: {"description": "Not found"}}
    )

    @router.get("/health")
    async def health_check() -> dict:
        return healthz_controller.get()

    @router.post("/message")
    async def post_message(text: str):
        line_api_controller.send_push_message(os.environ.get("USER_ID"), text)

    # @router.post("/callback")
    # async def callback(request: Request, background_tasks: BackgroundTasks):
    #    events = parser.parse(
    #        (await request.body()).decode("utf-8"),
    #        request.headers.get("X-Line-Signature", "")
    #    )
    #
    #    background_tasks.add_task(handle_events, events=events)
    #
    #    return "ok"

    # async def handle_events(events):
    #    for event in events:
    #        try:
    #            await line_api.reply_message_async(
    #                event.reply_token,
    #                TextSendMessage(event.message.text))
    #        except Exception:
    #            pass

    return router
