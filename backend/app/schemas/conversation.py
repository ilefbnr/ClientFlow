
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


ConversationChannel = Literal[
    "email",
    "whatsapp",
    "messenger",
    "phone"
]

ConversationStatus = Literal["open", "closed"]


class ConversationCreate(BaseModel):
    channel: ConversationChannel
    status: ConversationStatus = "open"
    customer_id: int


class ConversationUpdate(BaseModel):
    channel: ConversationChannel | None = None
    status: ConversationStatus | None = None
    customer_id: int | None = None


class ConversationResponse(BaseModel):
    id: int
    channel: str
    status: str
    customer_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
