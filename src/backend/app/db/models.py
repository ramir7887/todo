from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
# Пользовательский импорт
from .database import Base

class ListItem(Base):
    __tablename__ = 'list_items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    color = Column(String(20))
    created_on = Column(DateTime(), default=datetime.utcnow)
    tasks = relationship("Task", back_populates="list_item")


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300))
    description = Column(String(300))
    active = Column(Boolean, default=False)
    created_on = Column(DateTime(), default=datetime.utcnow)
    list_item_id = Column(Integer, ForeignKey("list_items.id"))

    list_item = relationship("ListItem", back_populates="tasks")


