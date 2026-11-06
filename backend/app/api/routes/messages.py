
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.message import MessageCreate, MessageResponse
from app.services import message_service
from app.services.message_service import ConversationNotFoundError


router = APIRouter()


@router.post(
    "/conversations/{conversation_id}/messages",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED
)
def create_message(
    conversation_id: int,
    data: MessageCreate,
    db: Session = Depends(get_db)
):
    try:
        return message_service.create_message(db, conversation_id, data)
    except ConversationNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Conversation not found"
        )


@router.get(
    "/conversations/{conversation_id}/messages",
    response_model=list[MessageResponse]
)
def get_messages(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    # Verify that the conversation exists.
    from app.services.conversation_service import get_conversation_by_id

    conversation = get_conversation_by_id(db, conversation_id)

    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return message_service.get_messages(db, conversation_id)


@router.get("/{message_id}", response_model=MessageResponse)
def get_message(
    message_id: int,
    db: Session = Depends(get_db)
):
    message = message_service.get_message_by_id(db, message_id)

    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")

    return message


@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(
    message_id: int,
    db: Session = Depends(get_db)
):
    deleted = message_service.delete_message(db, message_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Message not found")

    return None
