from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Player(Base):

    __tablename__ = "players"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String,
        nullable=False
    )


    age = Column(
        Integer,
        nullable=False
    )


    position = Column(
        String,
        nullable=False
    )


    overall = Column(
        Integer,
        nullable=False
    )


    potential = Column(
        Integer,
        nullable=False
    )


    value = Column(
        Integer,
        nullable=False
    )


    salary = Column(
        Integer,
        nullable=False
    )


    club_id = Column(
        Integer,
        ForeignKey("clubs.id")
    )


    club = relationship(
        "Club",
        back_populates="players"
    )
