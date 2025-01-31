from sqlalchemy import Column, String, Date, Text
from core.database.base import BaseAsync

class Expense(BaseAsync):
    __tablename__ = 'expenses'
    
    category = Column(String)
    amount = Column(String)
    description = Column(Text)
    date = Column(Date)
