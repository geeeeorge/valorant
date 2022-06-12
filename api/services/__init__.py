import os

from aiolinebot import AioLineBotApi
from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, Request
from linebot import WebhookParser
from linebot.models import TextSendMessage

load_dotenv()

line_api = AioLineBotApi(os.environ.get("LINE_CHANNEL_ACCESS_TOKEN"))
parser = WebhookParser(channel_secret=os.environ.get("LINEBOT_CHANNEL_SECRET"))

app = FastAPI()


@app.get("/health")
def health_check():
    return {'status': 'OK'}


@app.post("/message")
async def post_message():
    # TextSendMessageの型に変換
    line_api.push_message(os.environ.get("USER_ID"), TextSendMessage('aaa'))


@app.post("/callback")
async def callback(request: Request, background_tasks: BackgroundTasks):
    events = parser.parse(
        (await request.body()).decode("utf-8"),
        request.headers.get("X-Line-Signature", "")
    )

    background_tasks.add_task(handle_events, events=events)

    return "ok"


async def handle_events(events):
    for event in events:
        try:
            await line_api.reply_message_async(
                event.reply_token,
                TextSendMessage(event.message.text))
        except Exception:
            pass
