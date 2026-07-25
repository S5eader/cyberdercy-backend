from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.message import Message


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)



# GET ALL MESSAGES

@router.get("/messages")
def get_messages(
    db: Session = Depends(get_db)
):

    messages = db.query(Message)\
        .order_by(Message.id.desc())\
        .all()

    return messages





# DELETE MESSAGE

@router.delete("/messages/{message_id}")
def delete_message(
    message_id: int,
    db: Session = Depends(get_db)
):

    message = db.query(Message)\
        .filter(Message.id == message_id)\
        .first()


    if not message:

        raise HTTPException(
            status_code=404,
            detail="Message not found"
        )


    db.delete(message)

    db.commit()


    return {
        "message": "Deleted successfully"
    }





# MARK MESSAGE AS READ

@router.put("/messages/{message_id}/read")
def mark_read(
    message_id: int,
    db: Session = Depends(get_db)
):

    message = db.query(Message)\
        .filter(Message.id == message_id)\
        .first()


    if not message:

        raise HTTPException(
            status_code=404,
            detail="Message not found"
        )


    message.is_read = True


    db.commit()

    db.refresh(message)


    return {
        "message": "Marked as read",
        "data": message
    }