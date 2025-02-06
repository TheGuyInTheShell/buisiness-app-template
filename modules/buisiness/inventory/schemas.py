

"""
from sqlalchemy import (
    Column, ForeignKey, String
)
from core.database.base import BaseAsync

class Inventory(BaseAsync):
    __tablename__ = 'inventory'
    item_name = Column(String)
    quantity = Column(String)
    unit = Column(String)
    reorder_level = Column(String)
    supplier_id = Column(String, ForeignKey('suppliers.uid'))"""


from typing import List

from pydantic import BaseModel
from core.schemas import Pagination

class RQInventory(BaseModel):
    item_name: str
    quantity: str
    unit: str
    reorder_level: str
    supplier_id: str

class RSInventory(RQInventory):
    uid: str

class RSInventoryList(Pagination):
    data: list[RSInventory] | List = []