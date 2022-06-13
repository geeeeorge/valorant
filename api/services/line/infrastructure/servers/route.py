import os

from fastapi import APIRouter, Request

from ...adapter.controllers.healthz import HealthzController
from ...adapter.controllers.line_api_controller import LineApiController


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
    async def post_message(texts: list[str]):
        line_api_controller.send_push_message(os.environ.get("USER_ID"), texts)

    @router.post("/callback")
    async def callback(request: Request):
        user_id = await line_api_controller.get_user_id(request)
        line_api_controller.send_push_message(user_id, ['現在準備中です'])

    return router
