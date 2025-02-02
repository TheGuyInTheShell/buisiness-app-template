from sqlalchemy import (
    Column, ForeignKey, String, Integer
)
from core.database.base import BaseAsync

class Inventory(BaseAsync):
    __tablename__ = 'inventory'
    item_name = Column(String)
    quantity = Column(String)
    unit = Column(String)
    reorder_level = Column(String)
    supplier_id = Column(Integer, ForeignKey('suppliers.uid'))