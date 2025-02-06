

"""class Expense(BaseAsync):
    __tablename__ = 'expenses'
    
    category = Column(String)
    amount = Column(String)
    description = Column(Text)
    date = Column(Date)"""

from typing import List
from datetime import datetime
from pydantic import BaseModel, field_validator
from core.schemas import Pagination

class RQExpense(BaseModel):
    category: str
    amount: str
    description: str
    date: datetime

    @field_validator('amount')
    def validate_amount(cls, v: str):
        if not v.isdigit():
            raise ValueError('Amount must be a number')
        return v
    

class RSExpense(RQExpense):
    uid: str

class RSExpenseList(Pagination):
    data: list[RSExpense] | List = []