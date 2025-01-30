from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_db

from .models import Customer
from .schemas import RQCustomer, RSCustomer, RSCustomerList

# prefix /customers
router = APIRouter()
tag = 'customers'

@router.get("id/{id}", response_model=RSCustomer, status_code=200, tags=[tag])
async def get_Permission(id: str, db: AsyncSession = Depends(get_async_db)) -> RSCustomer:
    try:
        result = await Customer.find_one(db, id)
        return result
    except Exception as e:
        print(e)
        raise e


@router.get("/", response_model=RSCustomerList, status_code=200, tags=[tag])
async def get_Permissions(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSCustomerList:
    try:
        result = await Customer.find_some(db, pag, ord, status)
        keys = RSCustomer.model_fields.keys()
        result = map(
            lambda x: RSCustomer(
                **{key: getattr(x, key) for key in keys}
            ),
            result,
        )
        return RSCustomerList(
            data=list(result),
            total=0,
            page=0,
            page_size=0,
            total_pages=0,
            has_next=False,
            has_prev=False,
            next_page=0,
            prev_page=0,
        )
    except Exception as e:
        print(e)
        raise e


@router.post("/", response_model=RSCustomer, status_code=201, tags=[tag])
async def create_Permission(
    menu: RQCustomer, db: AsyncSession = Depends(get_async_db)
) -> RSCustomer:
    try:
        result = await Customer(**menu.model_dump()).save(db)
        return result
    except Exception as e:
        print(e)
        raise e


@router.delete("id/{id}", status_code=204, tags=[tag])
async def delete_Permission(id: str, db: AsyncSession = Depends(get_async_db)) -> None:
    try:
        await Customer.delete(db, id)
    except Exception as e:
        print(e)
        raise e


@router.put("id/{id}", response_model=RSCustomer, status_code=200, tags=[tag])
async def update_Permission(
    id: str, menu: RQCustomer, db: AsyncSession = Depends(get_async_db)
) -> RSCustomer:
    try:
        result = await Customer.update(db, id, menu.model_dump())
        return result
    except Exception as e:
        print(e)
        raise e

@router.get("/search", response_model=RSCustomerList, status_code=200, tags=[tag])
async def search_Permission(
    search: str,
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSCustomerList:
    try:
        result = await Customer.search(db, search, pag, ord, status)
        keys = RSCustomer.model_fields.keys()
        result = map(
            lambda x: RSCustomer(
                **{key: getattr(x, key) for key in keys}
            ),
            result,
        )
        return RSCustomerList(
            data=list(result),
            total=0,
            page=0,
            page_size=0,
            total_pages=0,
            has_next=False,
            has_prev=False,
            next_page=0,
            prev_page=0,
        )
    except Exception as e:
        print(e)
        raise e