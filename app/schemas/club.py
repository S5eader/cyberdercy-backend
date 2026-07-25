from pydantic import BaseModel


class ClubCreate(BaseModel):
    name: str
    city: str
    stadium: str
    founded_year: int | None = None
    budget: int
    reputation: int


class ClubResponse(BaseModel):
    id: int
    name: str
    city: str
    stadium: str
    founded_year: int | None
    budget: int
    reputation: int

    class Config:
        from_attributes = True
        
class PlayerInClub(BaseModel):
    id: int
    name: str
    position: str
    overall: int

    class Config:
        from_attributes = True


class ClubSquadResponse(BaseModel):
    id: int
    name: str
    players: list[PlayerInClub]

    class Config:
        from_attributes = True        
        