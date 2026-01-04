from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from app.core.database import Base


class DecisionStatus(str, enum.Enum):
    """Karar durumu enum."""

    DRAFT = "draft"
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    IMPLEMENTED = "implemented"


class Decision(Base):
    """Karar modeli."""

    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=False)
    committee_id = Column(Integer, ForeignKey("committees.id"), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(DecisionStatus), default=DecisionStatus.DRAFT, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    approved_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    committee = relationship("Committee", foreign_keys=[committee_id])
    creator = relationship("User", foreign_keys=[created_by])


class DecisionVote(Base):
    """Karar oyu modeli."""

    __tablename__ = "decision_votes"

    id = Column(Integer, primary_key=True, index=True)
    decision_id = Column(Integer, ForeignKey("decisions.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    vote = Column(String, nullable=False)  # approve, reject, abstain
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    decision = relationship("Decision", foreign_keys=[decision_id])
    user = relationship("User", foreign_keys=[user_id])
