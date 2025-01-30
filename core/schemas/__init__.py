# RQ -> request
# RS -> response
# IN -> internal
from typing import Any, Dict, Literal

from pydantic import BaseModel


class SearchParams(BaseModel):
    query: Dict[Literal["eq", "bt", "ne"], str] = {}

class Pagination(BaseModel):
    total: int = 0
    page: int = 0
    page_size: int = 0
    total_pages: int = 0
    has_next: bool = False
    has_prev: bool = False
    next_page: int = 0
    prev_page: int = 0
