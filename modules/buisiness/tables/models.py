from sqlalchemy import String, Integer, Column
from core.database.base import BaseAsync

class Table(BaseAsync):
    __tablename__ = 'tables'

    table_number = Column(Integer)
    capacity = Column(Integer)
    status = Column(String)
