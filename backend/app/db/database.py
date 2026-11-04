from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.models.conversation import Conversation
from app.models.message import Message

from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()