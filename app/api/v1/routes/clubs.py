from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.club import ClubSquadResponse
from app.services.club_service import get_club_squad
from app.database import get_db
from app.schemas.club import ClubCreate, ClubResponse
from app.services.club_service import create_club


router = APIRouter()


@router.post("/clubs/create", response_model=ClubResponse)
def create_new_club(
    club: ClubCreate,
    db: Session = Depends(get_db)
):

    return create_club(db, club)


@router.get(
    "/clubs/{club_id}/squad",
    response_model=ClubSquadResponse
)
def get_squad(
    club_id: int,
    db: Session = Depends(get_db)
):

    return get_club_squad(
        db,
        club_id
    )