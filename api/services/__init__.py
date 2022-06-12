from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .line import main as main_line

app = FastAPI()


domain_reg = r"https://george\.com|http://localhost:*"

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=domain_reg,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_line())
