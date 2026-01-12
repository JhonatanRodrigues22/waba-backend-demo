import logging

from fastapi import FastAPI
from app.api.routes.webhooks import router as webhooks_router

# logging básico (depois a gente refina)
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="WABA Backend Demo", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(webhooks_router)
