from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional
from datetime import datetime
from app.schemas.record import RecordCreate
from app.dependencies.auth import authorize
from app.services.record_service import (
    create_record_service as create_record,
    get_records_service as get_records,
    update_record_service as update_record_svc,
    delete_record_service as delete_record
)

router = APIRouter(prefix="/records", tags=["Records"])


# CREATE
@router.post("/")
async def create_record_route(
    record: RecordCreate,
    user=Depends(authorize(["admin"]))
):
    return await create_record(record.dict(), user["email"])


# GET
@router.get("/")
async def get_records_route(
    type: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    limit: int = 10,
    skip: int = 0,
    user=Depends(authorize(["admin", "analyst", "viewer"]))
):
    filters = {
        "type": type,
        "category": category,
        "start_date": start_date,
        "end_date": end_date
    }

    return await get_records(filters)


# UPDATE
@router.put("/{record_id}")
async def update_record(
    record_id: str,
    record: RecordCreate,
    user=Depends(authorize(["admin"]))
):
    result = await update_record_svc(record_id, record.dict())

    if not result:
        raise HTTPException(status_code=404, detail="Record not found")

    return result


# DELETE
@router.delete("/{record_id}")
async def delete_record_route(
    record_id: str,
    user=Depends(authorize(["admin"]))
):
    result = await delete_record(record_id)

    if not result:
        raise HTTPException(status_code=404, detail="Record not found")

    return result
