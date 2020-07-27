from typing import Optional
import secrets

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Pasta(BaseModel):
    text: str
    language: str
    will_expire: Optional[bool] = True


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/{pasta_id}")
async def get_pasta(pasta_id: str):
    return {"pasta_id": pasta_id}


@app.put("/pasta")
def put_pasta(pasta: Pasta):
    pasta_id = secrets.token_hex(6)
    return {"pasta_id": pasta_id}
