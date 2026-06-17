
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate, userLogin

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/register", response_model=UserCreate)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        hashed_password=user.password,  # In production, hash the password!
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(user: userLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    if db_user.hashed_password != user.hashed_password:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    return {"message": "Login successful", "username": db_user.username}
