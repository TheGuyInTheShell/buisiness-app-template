from typing import List

from pydantic import BaseModel
from core.schemas import Pagination

class RQCustomer(BaseModel):
    name: str
    phone: str
    email: str
    address: str

class RSCustomer(RQCustomer):
    uid: str

class RSCustomerList(Pagination):
    data: list[RSCustomer] | List = []