from fastapi import APIRouter, Depends
from app.dependencies.auth import authorize
from app.services.dashboard_service import (
    get_dashboard_summary_service,
    get_category_breakdown_service,
    get_recent_transactions_service
)
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
async def get_dashboard(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    user=Depends(authorize(["admin", "analyst"]))
):
    summary = await get_dashboard_summary_service()
    categories = await get_category_breakdown_service()
    recent = await get_recent_transactions_service()

    return {
        "summary": summary,
        "category_breakdown": categories,
        "recent_transactions": recent
    }
