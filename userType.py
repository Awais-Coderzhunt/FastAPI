
from pydantic import BaseModel

class user(BaseModel):
    name: str
    age: int

