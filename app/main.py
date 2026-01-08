from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.core.config import settings
from app.core.logger import setup_logger

logger = setup_logger()

app = FastAPI(title=settings.APP_NAME)

@app.get("/health")
def health_check():
    logger.info("Health check called")
    return {"status": "ok", "env": settings.ENV}

app.include_router(chat_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.ENV == "local",
    )
