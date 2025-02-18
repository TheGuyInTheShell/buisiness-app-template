from typing import Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_async_db
from core.services.generic_controller import get_some

from .models import Reservation
from .schemas import RQReservations, RSReservations, RSReservationsList

# prefix /reservation
router = APIRouter()
tag = 'reservation'

@router.get("id/{id}", response_model=RSReservations, status_code=200, tags=[tag])
async def get_reservation(id: str, db: AsyncSession = Depends(get_async_db)) -> RSReservations:
    try:
        result = await Reservation.find_one(db, id)
        return result
    except Exception as e:
        print(e)
        raise e


@router.get("/", response_model=RSReservationsList, status_code=200, tags=[tag])
async def get_reservations(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
) -> RSReservationsList:
    try:
        result = await get_some(
            Reservation,
            RQReservations,
            RSReservationsList,
            db,
            query={
                "pag": pag,
                "ord": ord,
                "status": status,
            }
        )
        return result 
    except Exception as e:
        print(e)
        raise e


@router.post("/", response_model=RSReservations, status_code=201, tags=[tag])
async def create_reservation(
    data: RQReservations, db: AsyncSession = Depends(get_async_db)
) -> RSReservations:
    try:
        result = await Reservation(**data.model_dump()).save(db)
        return result
    except Exception as e:
        print(e)
        raise e


@router.delete("id/{id}", status_code=204, tags=[tag])
async def delete_reservation(id: str, db: AsyncSession = Depends(get_async_db)) -> None:
    try:
        await Reservation.delete(db, id)
    except Exception as e:
        print(e)
        raise e


@router.put("id/{id}", response_model=RSReservations, status_code=200, tags=[tag])
async def update_reservation(
    id: str, data: RQReservations, db: AsyncSession = Depends(get_async_db)
) -> RSReservations:
    try:
        result = await Reservation.update(db, id, data.model_dump())
        return result
    except Exception as e:
        print(e)
        raise e
