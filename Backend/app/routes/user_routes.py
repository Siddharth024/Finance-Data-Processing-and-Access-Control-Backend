from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.user_service import create_user_service, get_all_users_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_user(user: UserCreate):
    return await create_user_service(user.dict())


@router.get("/")
async def get_users():
    return await get_all_users_service()
