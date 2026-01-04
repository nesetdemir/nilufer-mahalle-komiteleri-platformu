from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.logging import logger
from app.api import api_router

# FastAPI uygulamasını oluştur
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API router'ı ekle
app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    """Uygulama başlangıcında çalışacak işlemler."""
    logger.info(f"{settings.APP_NAME} başlatılıyor...")
    logger.info(f"Versiyon: {settings.APP_VERSION}")


@app.on_event("shutdown")
async def shutdown_event():
    """Uygulama kapanışında çalışacak işlemler."""
    logger.info(f"{settings.APP_NAME} kapatılıyor...")


@app.get("/")
async def root():
    """Ana endpoint."""
    return {
        "message": f"Hoş geldiniz! {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Sağlık kontrolü endpoint'i."""
    return {"status": "healthy"}

