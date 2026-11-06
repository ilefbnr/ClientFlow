
from sqlalchemy.orm import Session

from app.models.message import Message
from app.models.conversation import Conversation
from app.schemas.message import MessageCreate


class ConversationNotFoundError(Exception):
    pass


def create_message(
    db: Session,
    conversation_id: int,
    data: MessageCreate
):
    conversation = db.query(Conversation).filter(
        Conversation.id == conversation_id
    ).first()

    if conversation is None:
        raise ConversationNotFoundError()

    message = Message(
        content=data.content,
        sender_type=data.sender_type,
        conversation_id=conversation_id
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message


def get_messages(db: Session, conversation_id: int):
    return db.query(Message).filter(
        Message.conversation_id == conversation_id
    ).order_by(Message.created_at.asc(), Message.id.asc()).all()


def get_message_by_id(db: Session, message_id: int):
    return db.query(Message).filter(
        Message.id == message_id
    ).first()


def delete_message(db: Session, message_id: int):
    message = get_message_by_id(db, message_id)

    if message is None:
        return False

    db.delete(message)
    db.commit()

    return True
