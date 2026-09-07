from fastapi import APIRouter, HTTPException, Response

from app import schemas, utils


router = APIRouter(prefix="/items", tags=["Items"])


@router.get("", response_model=list[schemas.ItemResponse])
def list_items(search: str = ""):
    return utils.get_items(search)


@router.get("/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int):
    item = utils.get_item(item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@router.post("", response_model=schemas.ItemResponse, status_code=201)
def create_item(item: schemas.ItemCreate):
    return utils.create_item(item)


@router.put("/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemCreate):
    existing_item = utils.get_item(item_id)

    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return utils.update_item(existing_item, item)


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int):
    item = utils.get_item(item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    utils.delete_item(item)
    return Response(status_code=204)