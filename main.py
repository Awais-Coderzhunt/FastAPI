from typing import Annotated

from fastapi import FastAPI, Body

from userType import user

app = FastAPI()


@app.post("/users/")
async def create_user(user: Annotated[user, Body()]):
    return {"message": f"User {user.name} created successfully!"}


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
