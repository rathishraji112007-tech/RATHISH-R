from pydantic import BaseModel, Field


class HomeRequest(BaseModel):
    budget: float = Field(gt=0)
    room_type: str
    preferences: str = "Simple"


class PartyRequest(BaseModel):
    budget: float = Field(gt=0)
    guests: int = Field(gt=0)
    event_type: str


class JewelryRequest(BaseModel):
    budget: float = Field(gt=0)
    occasion: str
    style: str
