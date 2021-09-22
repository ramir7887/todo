from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import Response
from sqlalchemy.orm import Session
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# зависимости проекта
from ..db import models
from ..db.database import get_db

router = APIRouter(
    prefix='/api/task',
    tags=['task'],
    # dependencies=[Depends()],
    responses={404: {'description': 'Not found'}},
)

class TaskBase(BaseModel):
    name: str
    description: Optional[str] = ''
    active: bool = True
    list_item_id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: Optional[int]
    created_on: datetime

    class Config:
        orm_mode = True

class Tasks(BaseModel):
    items: List[Task]

    class Config:
        orm_mode = True

@router.delete('/{task_id}')
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db.query(models.Task).filter(models.Task.id == task_id).delete()
    db.commit()

@router.patch('/')
def update_task(task: Task, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).get(task.id)
    if db_task:
        db_task.id = task.id
        db_task.name = task.name
        db_task.description = task.description
        db_task.active = task.active
        db_task.list_item_id = task.list_item_id
        db.commit()
        return Response()
    else:
        raise HTTPException(404)


@router.get('/{item_id}', response_model=Tasks)
def get_tasks_by_list_id(item_id: int, db: Session = Depends(get_db)):
    tasks = db.query(models.Task).filter(models.Task.list_item_id == item_id).all()
    if tasks:
        return {'items': tasks}
    else:
        raise HTTPException(404)


@router.get('/')
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).order_by(models.Task.created_on).all()
    if tasks:
        return {'items': tasks}
    else:
        raise HTTPException(404, 'Задачи не найдены')


@router.post('/')
async def create_task(task: TaskBase, db: Session = Depends(get_db)):
    new_task = models.Task(
        name=task.name,
        description=task.description,
        list_item_id=task.list_item_id
    )
    db.add(new_task)
    db.commit()
    return Response()

