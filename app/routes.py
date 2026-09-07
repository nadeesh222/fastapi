from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app import schemas, utils
from app.database import get_db


router = APIRouter(prefix="/items", tags=["Items"])


@router.get("", response_model=list[schemas.ItemResponse])
def list_items(search: str = "", database: Session = Depends(get_db)):
    return utils.get_items(database, search)


@router.get("/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, database: Session = Depends(get_db)):
    item = utils.get_item(database, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("", response_model=schemas.ItemResponse, status_code=201)
def create_item(
    item: schemas.ItemCreate,
    database: Session = Depends(get_db),
):
    return utils.create_item(database, item)


@router.put("/{item_id}", response_model=schemas.ItemResponse)
def update_item(
    item_id: int,
    item: schemas.ItemCreate,
    database: Session = Depends(get_db),
):
    existing_item = utils.get_item(database, item_id)
    if existing_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return utils.update_item(database, existing_item, item)


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, database: Session = Depends(get_db)):
    item = utils.get_item(database, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    utils.delete_item(database, item)
    return Response(status_code=204)