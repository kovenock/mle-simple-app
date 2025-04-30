from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    value: int

@app.get("/hello")
async def read_hello():
    return {"message": "Hello, World!"}

@app.post("/")
async def return_item(item: Item):
    return item