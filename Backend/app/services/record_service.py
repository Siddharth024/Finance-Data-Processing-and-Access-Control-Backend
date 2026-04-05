from app.db.mongodb import record_collection
from datetime import datetime
from bson import ObjectId


# CREATE RECORD
async def create_record_service(record_data: dict, user_email: str):
    record_data["created_by"] = user_email
    record_data["created_at"] = datetime.utcnow()

    result = await record_collection.insert_one(record_data)

    return {
        "id": str(result.inserted_id),
        "message": "Record created successfully"
    }


# GET RECORDS
async def get_records_service(filters: dict, limit: int, skip: int):
    query = {}

    if filters.get("type"):
        query["type"] = filters["type"]

    if filters.get("category"):
        query["category"] = filters["category"]

    if filters.get("start_date") and filters.get("end_date"):
        query["date"] = {
            "$gte": filters["start_date"],
            "$lte": filters["end_date"]
        }

    records = []
    async for record in record_collection.find(query).skip(skip).limit(limit):
        record["_id"] = str(record["_id"])
        records.append(record)

    return await get_records_service(filters, limit, skip)


# UPDATE RECORD
async def update_record_service(record_id: str, update_data: dict):
    update_data["updated_at"] = datetime.utcnow()

    result = await record_collection.update_one(
        {"_id": ObjectId(record_id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        return None

    return {"message": "Record updated successfully"}


# DELETE RECORD
async def delete_record_service(record_id: str):
    result = await record_collection.delete_one(
        {"_id": ObjectId(record_id)}
    )

    if result.deleted_count == 0:
        return None

    return {"message": "Record deleted successfully"}
