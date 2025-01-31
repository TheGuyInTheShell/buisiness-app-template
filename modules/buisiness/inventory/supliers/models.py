from sqlalchemy import Column, String
from core.database.base import BaseAsync

class Supplier(BaseAsync):
    __tablename__ = 'suppliers'
    name = Column(String)
    contact = Column(String)