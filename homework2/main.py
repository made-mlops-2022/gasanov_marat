import dataclasses

from fastapi import FastAPI
import uvicorn
from human_model import HumanModel
from queries import query_predict, query_health

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post('/predict/')
async def get_predict(input_item: HumanModel):
    print(input_item)
    responce = query_predict(input_item)
    return responce


@app.get('/health/')
async def get_heath():
    return query_health()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
