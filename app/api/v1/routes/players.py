from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.player import PlayerCreate, PlayerResponse
from app.services.player_service import create_player


router = APIRouter()


@router.post("/players/create", response_model=PlayerResponse)
def create_new_player(
    player: PlayerCreate,
    db: Session = Depends(get_db)
):

    return create_player(db, player)