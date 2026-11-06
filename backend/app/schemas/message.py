
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


SenderType = Literal["customer", "business", "ai_agent"]


class MessageCreate(BaseModel):
    content: str
    sender_type: SenderType


class MessageResponse(BaseModel):
    id: int
    content: str
    sender_type: str
    conversation_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
