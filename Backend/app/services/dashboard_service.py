from app.db.mongodb import record_collection


async def get_dashboard_summary_service(start_date=None, end_date=None):
    match_stage = {}

    if start_date and end_date:
        match_stage["date"] = {
            "$gte": start_date,
            "$lte": end_date
        }

    pipeline = [
        {"$match": match_stage} if match_stage else {},
        {
            "$group": {
                "_id": "$type",
                "total": {"$sum": "$amount"}
            }
        }
    ]

    # remove empty stage
    pipeline = [stage for stage in pipeline if stage]

    result = await record_collection.aggregate(pipeline).to_list(10)

    income = 0
    expense = 0

    for item in result:
        if item["_id"] == "income":
            income = item["total"]
        elif item["_id"] == "expense":
            expense = item["total"]

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }

async def get_category_breakdown_service():
    pipeline = [
        {
            "$group": {
                "_id": "$category",
                "total": {"$sum": "$amount"}
            }
        }
    ]

    result = await record_collection.aggregate(pipeline).to_list(100)

    return [
        {
            "category": item["_id"],
            "total": item["total"]
        }
        for item in result
    ]

async def get_recent_transactions_service():
    records = await record_collection.find().sort("date", -1).limit(5).to_list(5)

    for record in records:
        record["_id"] = str(record["_id"])

    return records
