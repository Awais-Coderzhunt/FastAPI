from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="My FastAPI Project",
    description="A starter FastAPI application",
    version="0.1.0",
)


# Simple in-memory data store for the example
items: dict[int, "Item"] = {}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI 🚀"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "item": items.get(item_id)}


@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    items[item_id] = item
    return {"item_id": item_id, "item": item}
