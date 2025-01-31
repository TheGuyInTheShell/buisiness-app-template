from sqlalchemy import Column, String
from core.database.base import BaseAsync

class Customer(BaseAsync):
    __tablename__ = 'customers'
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)