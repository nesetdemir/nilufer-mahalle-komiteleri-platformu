from fastapi import APIRouter
from app.modules.auth.router import router as auth_router
from app.modules.committee.router import router as committee_router
from app.modules.decision.router import router as decision_router

# Ana API router
api_router = APIRouter()

# Modül router'larını ekle
api_router.include_router(auth_router)
api_router.include_router(committee_router)
api_router.include_router(decision_router)
