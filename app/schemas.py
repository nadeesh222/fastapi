from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    name: str
    price: float
    quantity: int


class ItemResponse(ItemCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)