
from datetime import datetime
from pydantic import BaseModel, Field

class userCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(..., max_length=100)
    hashed_password: str = Field(min_length=6, max_length=255)

class userLogin(BaseModel):
    email: str = Field(min_length=3, max_length=50)
    hashed_password: str = Field(min_length=6, max_length=255)

    