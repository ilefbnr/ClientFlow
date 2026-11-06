
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.conversation import (
    ConversationCreate,
    ConversationUpdate,
    ConversationResponse
)
from app.services import conversation_service
from app.services.conversation_service import CustomerNotFoundError


router = APIRouter()


@router.post(
    "/",
    response_model=ConversationResponse,
    status_code=status.HTTP_201_CREATED
)
def create_conversation(
    data: ConversationCreate,
    db: Session = Depends(get_db)
):
    try:
        return conversation_service.create_conversation(db, data)
    except CustomerNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )


@router.get("/", response_model=list[ConversationResponse])
def get_conversations(db: Session = Depends(get_db)):
    return conversation_service.get_conversations(db)


@router.get("/{conversation_id}", response_model=ConversationResponse)
def get_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    conversation = conversation_service.get_conversation_by_id(
        db, conversation_id
    )

    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return conversation


@router.put("/{conversation_id}", response_model=ConversationResponse)
def update_conversation(
    conversation_id: int,
    data: ConversationUpdate,
    db: Session = Depends(get_db)
):
    try:
        conversation = conversation_service.update_conversation(
            db, conversation_id, data
        )
    except CustomerNotFoundError:
        raise HTTPException(status_code=404, detail="Customer not found")

    if conversation is None:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return conversation


@router.delete(
    "/{conversation_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_conversation(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    deleted = conversation_service.delete_conversation(
        db, conversation_id
    )

    if not deleted:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return None
