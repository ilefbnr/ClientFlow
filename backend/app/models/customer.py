from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.database import Base
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, index=True)
    phone = Column(String(30), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    tickets = relationship("Ticket", back_populates="customer")
    conversations = relationship("Conversation", back_populates="customer")
