from typing import List

from pydantic import BaseModel
from core.schemas import Pagination

class RQDelivery(BaseModel):
    order_id: str
    delivery_person_id: str
    address: str
    delivery_time: str
    status: str

class RSDelivery(RQDelivery):
    uid: str

class RSCustomerList(Pagination):
    data: list[RSDelivery] | List = []