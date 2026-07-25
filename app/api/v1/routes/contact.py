from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageResponse

router = APIRouter(
    prefix="/contact",
    tags=["Contact"]
)


@router.post(
    "/",
    response_model=MessageResponse
)
def create_message(
    message: MessageCreate,
    db: Session = Depends(get_db)
):
    new_message = Message(
    name=message.name,
    email=message.email,
    subject=message.subject,
    message=message.message
)

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message
