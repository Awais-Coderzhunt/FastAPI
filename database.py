from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database file (banega project folder ke andar: app.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# check_same_thread=False sirf SQLite ke liye zaruri hai
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Har request ke liye fresh DB session deta hai, phir close kar deta hai
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
