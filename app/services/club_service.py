from sqlalchemy.orm import Session

from app.models.club import Club
from app.schemas.club import ClubCreate
from app.models.club import Club


def get_club_squad(db, club_id):

    club = (
        db.query(Club)
        .filter(Club.id == club_id)
        .first()
    )

    return club


def create_club(db: Session, club_data: ClubCreate):

    club = Club(
        name=club_data.name,
        city=club_data.city,
        stadium=club_data.stadium,
        founded_year=club_data.founded_year,
        budget=club_data.budget,
        reputation=club_data.reputation
    )

    db.add(club)
    db.commit()
    db.refresh(club)

    return club