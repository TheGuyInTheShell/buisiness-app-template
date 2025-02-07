from typing import List

from pydantic import BaseModel


"""
name = Column(String)
    description = Column(Text)
    price = Column(String)
    category = Column(String)
    is_available = Column(Boolean)
"""
from core.schemas import Pagination


class RQMenuItem(BaseModel):
    name: str
    description: str
    prrice: str
    category: str
    is_available: bool


class RSMenuItem(RQMenuItem):
    uid: str

class RSMenuItemList(Pagination):
    data: list[RSMenuItem] | List = []