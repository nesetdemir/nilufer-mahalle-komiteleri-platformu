from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CommitteeBase(BaseModel):
    """Temel komite şeması."""
    name: str
    neighborhood: str
    description: Optional[str] = None


class CommitteeCreate(CommitteeBase):
    """Komite oluşturma şeması."""
    pass


class CommitteeUpdate(BaseModel):
    """Komite güncelleme şeması."""
    name: Optional[str] = None
    neighborhood: Optional[str] = None
    description: Optional[str] = None


class CommitteeResponse(CommitteeBase):
    """Komite yanıt şeması."""
    id: int
    created_by: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class CommitteeMemberBase(BaseModel):
    """Temel komite üyesi şeması."""
    role: str = "member"


class CommitteeMemberCreate(CommitteeMemberBase):
    """Komite üyesi ekleme şeması."""
    user_id: int


class CommitteeMemberResponse(CommitteeMemberBase):
    """Komite üyesi yanıt şeması."""
    id: int
    committee_id: int
    user_id: int
    joined_at: datetime
    
    class Config:
        from_attributes = True

