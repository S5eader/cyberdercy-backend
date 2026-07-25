from sqlalchemy.orm import Session

from app.models.player import Player
from app.schemas.player import PlayerCreate


def create_player(db: Session, player_data: PlayerCreate):

    player = Player(
        name=player_data.name,
        age=player_data.age,
        position=player_data.position,
        overall=player_data.overall,
        potential=player_data.potential,
        value=player_data.value,
        salary=player_data.salary,
        club_id=player_data.club_id
    )

    db.add(player)
    db.commit()
    db.refresh(player)

    return player