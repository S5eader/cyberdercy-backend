from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Manager(Base):
    __tablename__ = "managers"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    name = Column(
        String,
        nullable=False
    )

    reputation = Column(
        Integer,
        default=50
    )

    experience = Column(
        Integer,
        default=0
    )


    user = relationship(
    "User",
    back_populates="manager"
)