from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI App")


# Simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


# Ek aur GET endpoint (naam ke saath)
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
