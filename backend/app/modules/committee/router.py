from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.modules.committee.service import CommitteeService
from app.modules.committee.schemas import (
    CommitteeCreate, 
    CommitteeUpdate, 
    CommitteeResponse
)
from app.modules.auth.dependencies import get_current_active_user
from app.modules.auth.schemas import UserResponse
from app.modules.committee.policies import (
    CommitteePolicy,
    require_can_update_committee,
    require_can_delete_committee
)

router = APIRouter(prefix="/committees", tags=["committees"])


@router.get("", response_model=List[CommitteeResponse])
async def get_committees(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    neighborhood: str = Query(None),
    db: Session = Depends(get_db)
):
    """Komite listesini getirir."""
    service = CommitteeService(db)
    if neighborhood:
        return service.get_committees_by_neighborhood(neighborhood)
    return service.get_all_committees(skip=skip, limit=limit)


@router.get("/{committee_id}", response_model=CommitteeResponse)
async def get_committee(
    committee_id: int,
    db: Session = Depends(get_db)
):
    """Komite detayını getirir."""
    service = CommitteeService(db)
    return service.get_committee(committee_id)


@router.post("", response_model=CommitteeResponse, status_code=status.HTTP_201_CREATED)
async def create_committee(
    committee_data: CommitteeCreate,
    current_user: UserResponse = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Yeni komite oluşturur."""
    if not CommitteePolicy.can_create_committee(current_user):
        from app.core.exceptions import ForbiddenError
        raise ForbiddenError("Komite oluşturma yetkiniz yok")
    
    service = CommitteeService(db)
    return service.create_committee(committee_data, current_user.id)


@router.put("/{committee_id}", response_model=CommitteeResponse)
async def update_committee(
    committee_id: int,
    committee_data: CommitteeUpdate,
    current_user: UserResponse = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Komite bilgilerini günceller."""
    require_can_update_committee(current_user, committee_id, db)
    
    service = CommitteeService(db)
    return service.update_committee(committee_id, committee_data)


@router.delete("/{committee_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_committee(
    committee_id: int,
    current_user: UserResponse = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Komiteyi siler."""
    require_can_delete_committee(current_user, committee_id, db)
    
    service = CommitteeService(db)
    service.delete_committee(committee_id)

