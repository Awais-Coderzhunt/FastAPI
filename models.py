from sqlalchemy import Column, Integer, String

from database import Base


# Yeh class database table "users" ko represent karti hai
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
