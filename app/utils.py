from app import schemas
from app.data import items


def get_items(search: str = ""):
    if not search:
        return items

    search_text = search.lower()
    return [
        item
        for item in items
        if search_text in item["name"].lower()
    ]


def get_item(item_id: int):
    return next(
        (item for item in items if item["id"] == item_id),
        None,
    )


def create_item(item: schemas.ItemCreate):
    new_id = max((item["id"] for item in items), default=0) + 1
    new_item = {
        "id": new_id,
        **item.model_dump(),
    }
    items.append(new_item)
    return new_item


def update_item(existing_item: dict, item: schemas.ItemCreate):
    existing_item.update(item.model_dump())
    return existing_item


def delete_item(item: dict):
    items.remove(item)
