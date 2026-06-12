from pydantic import BaseModel


# Request body (POST/PUT) ke liye - user banate/update karte waqt
class UserCreate(BaseModel):
    name: str


# Response ke liye - jo data client ko wapas bhejte hain
class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # SQLAlchemy object se padhne ke liye
