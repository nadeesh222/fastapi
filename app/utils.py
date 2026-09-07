from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app import models, schemas


def get_items(database: Session, search: str = ""):
    query = select(models.Item).order_by(models.Item.id.desc())

    if search:
        word = f"%{search}%"
        query = query.where(
            or_(
                models.Item.name.ilike(word)
            )
        )

    return database.scalars(query).all()


def get_item(database: Session, item_id: int):
    return database.get(models.Item, item_id)


def create_item(database: Session, item: schemas.ItemCreate):
    new_item = models.Item(**item.model_dump())
    database.add(new_item)
    database.commit()
    database.refresh(new_item)
    return new_item


def update_item(database: Session, existing_item, item: schemas.ItemCreate):
    existing_item.name = item.name
    existing_item.price = item.price
    existing_item.quantity = item.quantity
    database.commit()
    database.refresh(existing_item)
    return existing_item


def delete_item(database: Session, item):
    database.delete(item)
    database.commit()