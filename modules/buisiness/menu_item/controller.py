from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_db

from .models import MenuItems as Menu
from .schemas import RQMenuItem, RSMenuItem, RSMenuTimeList

# prefix /menu
router = APIRouter()
tag = 'menu'

@router.get("/id/{id}", response_model=RSMenuItem, status_code=200, tags=[tag])
async def get_Permission(id: str, db: AsyncSession = Depends(get_async_db)) -> RSMenuItem:
    try:
        result = await Menu.find_one(db, id)
        return result
    except Exception as e:
        print(e)
        raise e


@router.get("/", response_model=RSMenuTimeList, status_code=200, tags=[tag])
async def get_Permissions(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSMenuTimeList:
    try:
        result = await Menu.find_some(db, pag, ord, status)
        result = map(
            lambda x: RSMenuItem(
                uid=x.uid,
                active=x.active,
                file_route=x.file_route,
                name=x.name,
                type_menu=x.type_menu,
            ),
            result,
        )
        return RSMenuTimeList(
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


@router.post("/", response_model=RSMenuItem, status_code=201, tags=[tag])
async def create_Permission(
    menu: RQMenuItem, db: AsyncSession = Depends(get_async_db)
) -> RSMenuItem:
    try:
        result = await Menu(**menu.model_dump()).save(db)
        return result
    except Exception as e:
        print(e)
        raise e


@router.delete("/id/{id}", status_code=204, tags=[tag])
async def delete_Permission(id: str, db: AsyncSession = Depends(get_async_db)) -> None:
    try:
        await Menu.delete(db, id)
    except Exception as e:
        print(e)
        raise e


@router.put("/id/{id}", response_model=RSMenuItem, status_code=200, tags=[tag])
async def update_Permission(
    id: str, menu: RQMenuItem, db: AsyncSession = Depends(get_async_db)
) -> RSMenuItem:
    try:
        result = await Menu.update(db, id, menu.model_dump())
        return result
    except Exception as e:
        print(e)
        raise e
