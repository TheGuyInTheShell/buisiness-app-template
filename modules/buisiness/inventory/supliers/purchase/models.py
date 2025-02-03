from sqlalchemy import Column, String, Date, ForeignKey
from core.database.base import BaseAsync


class Purchase(BaseAsync):
    __tablename__ = 'purchases'
    supplier_id = Column(String, ForeignKey('suppliers.uid'))
    purchase_date = Column(Date)
    total_amount = Column(String)