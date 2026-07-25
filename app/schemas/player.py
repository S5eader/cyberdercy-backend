from pydantic import BaseModel


class PlayerCreate(BaseModel):
    name: str
    age: int
    position: str
    overall: int
    potential: int
    value: int
    salary: int
    club_id: int | None = None


class PlayerResponse(BaseModel):
    id: int
    name: str
    age: int
    position: str
    overall: int
    potential: int
    value: int
    salary: int
    club_id: int | None

    class Config:
        from_attributes = True