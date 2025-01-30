from typing import List

from pydantic import BaseModel
from core.schemas import Pagination


class RQMenu(BaseModel):
    name: str
    type_menu: str
    file_route: str
    active: bool = True


class RSMenu(BaseModel):
    uid: str
    name: str
    type_menu: str
    file_route: str
    active: bool

class RSMenuList(Pagination):
    data: list[RSMenu] | List = []