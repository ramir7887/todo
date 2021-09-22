import datetime
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    pass

class User(BaseModel):
    id: Optional[int] = None
    name: str
    username: str
    email: str
    password: Optional[str] = None
    created_on: Optional[datetime.datetime] = None
    updated_on: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True


