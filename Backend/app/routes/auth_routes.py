from fastapi import APIRouter, HTTPException
from app.db.mongodb import user_collection
from app.core.security import create_access_token
from app.core.security import verify_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def login(email: str, password: str):
    user = await user_collection.find_one({"email": email})

    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "email": user["email"],
        "role": user["role"]
    })

    return {"access_token": token}
