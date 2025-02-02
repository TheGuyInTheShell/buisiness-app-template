from typing import Literal, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_async_db
from core.services.generic_controller import get_some
from .models import Employee
from .schemas import RQEmployee, RSEmployee, RSEmployeeList

router = APIRouter(tags = ['employees'])

@router.get("id/{id}", response_model=RSEmployee)
async def get_employee(id: str, db: AsyncSession = Depends(get_async_db)):
    try:
        return await Employee.find_one(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=RSEmployeeList)
async def get_employees(
    pag: Optional[int] = 1,
    ord: Literal["asc", "desc"] = "asc",
    status: Literal["deleted", "exists", "all"] = "exists",
    db: AsyncSession = Depends(get_async_db),
):
    try:
        result = await get_some(
            Employee,
            RSEmployee,
            RSEmployeeList,
            db,
            query={
                "pag": pag,
                "ord": ord,
                "status": status,
            }
        )
        return result 
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/", response_model=RSEmployee, status_code=201)
async def create_employee(
    employee: RQEmployee, 
    db: AsyncSession = Depends(get_async_db)
):
    try:
        return await Employee(**employee.model_dump()).save(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("id/{id}", response_model=RSEmployee)
async def update_employee(
    id: str,
    employee: RQEmployee,
    db: AsyncSession = Depends(get_async_db)
):
    try:
        return await Employee.update(db, id, employee.model_dump())
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("id/{id}", status_code=204)
async def delete_employee(
    id: str, 
    db: AsyncSession = Depends(get_async_db)
):
    try:
        await Employee.delete(db, id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))