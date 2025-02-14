from typing import List
from pydantic import BaseModel



"""
    __tablename__ = 'tables'

    table_number = Column(Integer)
    capacity = Column(Integer)
    status = Column(String)

"""

from core.schemas import Pagination



class RQTables(BaseModel):
    table_number: int
    capacity: int
    status: str

class RSTables(RQTables):
    uid: str

class RSTablesList(Pagination):
    data: list[RSTables] | List = []