from pydantic import BaseModel, ConfigDict


class CustomerCreate(BaseModel):
    full_name: str
    email: str
    phone: str | None = None


class CustomerUpdate(BaseModel):
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None

class CustomerResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str | None
    created_at: object

    model_config = ConfigDict(from_attributes=True)