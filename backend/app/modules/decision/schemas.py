from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.modules.decision.models import DecisionStatus


class DecisionBase(BaseModel):
    """Temel karar şeması."""
    title: str
    description: str
    committee_id: int


class DecisionCreate(DecisionBase):
    """Karar oluşturma şeması."""
    pass


class DecisionUpdate(BaseModel):
    """Karar güncelleme şeması."""
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[DecisionStatus] = None


class DecisionResponse(DecisionBase):
    """Karar yanıt şeması."""
    id: int
    created_by: int
    status: DecisionStatus
    created_at: datetime
    updated_at: Optional[datetime] = None
    approved_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class DecisionVoteBase(BaseModel):
    """Temel oy şeması."""
    vote: str  # approve, reject, abstain
    comment: Optional[str] = None


class DecisionVoteCreate(DecisionVoteBase):
    """Oy oluşturma şeması."""
    pass


class DecisionVoteResponse(DecisionVoteBase):
    """Oy yanıt şeması."""
    id: int
    decision_id: int
    user_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

