from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime
from ..db import models
from ..db.database import get_db


class ListItemBase(BaseModel):
    color: str = '#FFFFFF'
    name: str

    class Config:
        orm_mode = True


class ListItem(ListItemBase):
    id: int
    created_on: datetime

    class Config:
        orm_mode = True


class ListItems(BaseModel):
    items: List[ListItem]

    class Config:
        orm_mode = True


router = APIRouter(
    prefix='/api/list_item',
    tags=['list_item'],
    # dependencies=[Depends()],
    responses={404: {'description': 'Not found'}},
)

@router.delete('/{item_id}')
async def delete_list_item(item_id: int, db: Session = Depends(get_db)):
    db.query(models.ListItem).filter(models.ListItem.id == item_id).delete()
    db.query(models.Task).filter(models.Task.list_item_id == item_id).delete()
    db.commit()

@router.post('/')
async def create_list_item(item: ListItemBase, db: Session = Depends(get_db)):
    new_item = models.ListItem(
        color=item.color, name=item.name
    )
    db.add(new_item)
    db.commit()
    return Response()


@router.get('/{item_id}', response_model=ListItem)
async def get_list_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.ListItem).filter(models.ListItem.id == item_id).first()
    if item:
        return item
    else:
        raise HTTPException(404)

@router.get('/', response_model=ListItems)
async def get_list_items(db: Session = Depends(get_db)):
    items = db.query(models.ListItem).all()
    return {'items': items}


