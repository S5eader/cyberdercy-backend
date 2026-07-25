from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Club(Base):
    __tablename__ = "clubs"
    
    players = relationship(
    "Player",
    back_populates="club"
)

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    city = Column(
        String,
        nullable=False
    )

    stadium = Column(
        String,
        nullable=False
    )
    
    founded_year = Column(
    Integer,
    nullable=True
)

    budget = Column(
        Integer,
        default=10000000
    )

    reputation = Column(
        Integer,
        default=50
    )