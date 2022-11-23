import dataclasses

from fastapi import FastAPI
import uvicorn
from human_model import HumanModel
from queries import query_predict

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.post('/predict/')
async def get_predict(input_item: HumanModel):
    query_predict(input_item)
    return f'{input_item}'


@app.get('/heath/')
async def get_heath():
    return f'i am health'


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
