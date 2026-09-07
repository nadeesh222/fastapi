from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    price: float
    quantity: int


class ItemResponse(ItemCreate):
    id: int