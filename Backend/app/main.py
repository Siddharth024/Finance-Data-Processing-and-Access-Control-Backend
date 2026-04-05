from fastapi import FastAPI
from app.db.mongodb import client
import logging
from app.routes import user_routes
from app.routes import auth_routes
from app.routes import record_routes
from app.routes import dashboard_routes

app = FastAPI(title="Finance Backend Assignment API")
app.include_router(user_routes.router)
app.include_router(auth_routes.router)
app.include_router(record_routes.router)
app.include_router(dashboard_routes.router)

# setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup_db_client():
    try:
        # ping MongoDB
        await client.admin.command("ping")
        logger.info("✅ MongoDB connected successfully")
    except Exception as e:
        logger.error(f"❌ MongoDB connection failed: {e}")


@app.get("/")
def root():
    return {"message": "Finance API is running"}
