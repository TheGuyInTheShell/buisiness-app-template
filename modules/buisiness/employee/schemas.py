from typing import List, Literal
from datetime import datetime
from pydantic import BaseModel, field_validator
from core.schemas import Pagination

class RQEmployee(BaseModel):
    name: str
    role: Literal["waiter", "chef", "manager"]
    phone: str
    hire_date: datetime

    @field_validator("phone")
    def validate_phone(cls, v: str):
        if not v.isdigit():
            raise ValueError("Phone must be a number")
        if len(v) != 10:
                raise ValueError("Phone must be 10 digits")
        return v
    

class RSEmployee(RQEmployee):
    uid: str

class RSEmployeeList(Pagination):
    data: list[RSEmployee] | List = []