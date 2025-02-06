from typing import List

from pydantic import BaseModel


"""
name = Column(String)
    description = Column(Text)
    price = Column(String)
    category = Column(String)
    is_available = Column(Boolean)
"""


class RQMenuItem(BaseModel):
    name: str
    description: str
    prrice: str
    category: str
    is_available: bool


class RSMenuItem(RQMenuItem):
    uid: str

class RSMenuItemList(BaseModel):
    data: list[RSMenuItem] | List = []
    total: int = 0
    page: int = 0
    page_size: int = 0
    total_pages: int = 0
    has_next: bool = False
    has_prev: bool = False
    next_page: int = 0
    prev_page: int = 0