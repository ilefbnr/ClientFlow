from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


TicketStatus = Literal["open", "in_progress", "resolved", "closed"]
TicketPriority = Literal["low", "medium", "high", "urgent"]


class TicketCreate(BaseModel):
    title: str
    description: str | None = None
    status: TicketStatus = "open"
    priority: TicketPriority = "medium"
    customer_id: int


class TicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TicketStatus | None = None
    priority: TicketPriority | None = None
    customer_id: int | None = None


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: str
    customer_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)