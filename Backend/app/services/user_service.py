from app.db.mongodb import user_collection
from datetime import datetime
from app.core.security import hash_password

async def create_user_service(user_data: dict):
    # add extra fields
    user_data["is_active"] = True
    user_data["created_at"] = datetime.utcnow()
    user_data["password"] = hash_password(user_data["password"])
    result = await user_collection.insert_one(user_data)
    return {
        "id": str(result.inserted_id),
        "message": "User created successfully"
    }


async def get_all_users_service():
    users = []
    async for user in user_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
        user.pop("password", None)
    return users
