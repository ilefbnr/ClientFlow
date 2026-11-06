
from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.customer import Customer
from app.schemas.conversation import (
    ConversationCreate,
    ConversationUpdate
)


class CustomerNotFoundError(Exception):
    pass


def create_conversation(db: Session, data: ConversationCreate):
    customer = db.query(Customer).filter(
        Customer.id == data.customer_id
    ).first()

    if customer is None:
        raise CustomerNotFoundError()

    conversation = Conversation(
        channel=data.channel,
        status=data.status,
        customer_id=data.customer_id
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def get_conversations(db: Session):
    return db.query(Conversation).all()


def get_conversation_by_id(db: Session, conversation_id: int):
    return db.query(Conversation).filter(
        Conversation.id == conversation_id
    ).first()


def update_conversation(
    db: Session,
    conversation_id: int,
    data: ConversationUpdate
):
    conversation = get_conversation_by_id(db, conversation_id)

    if conversation is None:
        return None

    update_data = data.model_dump(exclude_unset=True)

    if "customer_id" in update_data and update_data["customer_id"] is not None:
        customer = db.query(Customer).filter(
            Customer.id == update_data["customer_id"]
        ).first()

        if customer is None:
            raise CustomerNotFoundError()

    for field, value in update_data.items():
        setattr(conversation, field, value)

    db.commit()
    db.refresh(conversation)

    return conversation


def delete_conversation(db: Session, conversation_id: int):
    conversation = get_conversation_by_id(db, conversation_id)

    if conversation is None:
        return False

    db.delete(conversation)
    db.commit()

    return True
