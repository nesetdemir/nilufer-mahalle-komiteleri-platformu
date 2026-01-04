from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.modules.decision.service import DecisionService
from app.modules.decision.schemas import (
    DecisionCreate,
    DecisionUpdate,
    DecisionResponse,
    DecisionVoteCreate,
)
from app.modules.auth.dependencies import get_current_active_user
from app.modules.auth.schemas import UserResponse

router = APIRouter(prefix="/decisions", tags=["decisions"])


@router.get("", response_model=List[DecisionResponse])
async def get_decisions(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    committee_id: int = Query(None),
    db: Session = Depends(get_db),
):
    """Karar listesini getirir."""
    service = DecisionService(db)
    if committee_id:
        return service.get_decisions_by_committee(committee_id)
    return service.get_all_decisions(skip=skip, limit=limit)


@router.get("/{decision_id}", response_model=DecisionResponse)
async def get_decision(decision_id: int, db: Session = Depends(get_db)):
    """Karar detayını getirir."""
    service = DecisionService(db)
    return service.get_decision(decision_id)


@router.post("", response_model=DecisionResponse, status_code=status.HTTP_201_CREATED)
async def create_decision(
    decision_data: DecisionCreate,
    current_user: UserResponse = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Yeni karar oluşturur."""
    service = DecisionService(db)
    return service.create_decision(decision_data, current_user.id)


@router.put("/{decision_id}", response_model=DecisionResponse)
async def update_decision(
    decision_id: int,
    decision_data: DecisionUpdate,
    current_user: UserResponse = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Karar bilgilerini günceller."""
    service = DecisionService(db)
    return service.update_decision(decision_id, decision_data)


@router.delete("/{decision_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_decision(
    decision_id: int,
    current_user: UserResponse = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Kararı siler."""
    service = DecisionService(db)
    service.delete_decision(decision_id)


@router.post("/{decision_id}/vote", status_code=status.HTTP_200_OK)
async def vote_on_decision(
    decision_id: int,
    vote_data: DecisionVoteCreate,
    current_user: UserResponse = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    """Karara oy verir."""
    service = DecisionService(db)
    service.submit_vote(decision_id, current_user.id, vote_data.vote, vote_data.comment)
    return {"message": "Oy başarıyla kaydedildi"}
