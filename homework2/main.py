import dataclasses
import sys

from fastapi import FastAPI
import uvicorn
from human_model import HumanModel
from queries import query_predict, query_health
import logging

app = FastAPI()

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post('/predict/')
async def get_predict(input_item: HumanModel):
    logger.info(input_item)
    response = query_predict(input_item)
    return response


@app.get('/health/')
async def get_heath():
    return query_health()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
