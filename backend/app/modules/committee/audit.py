from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base


class CommitteeAuditLog(Base):
    """Komite denetim kayıtları."""

    __tablename__ = "committee_audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    committee_id = Column(Integer, ForeignKey("committees.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    action = Column(String, nullable=False)  # create, update, delete, add_member, etc.
    details = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


def log_committee_action(
    db, committee_id: int, user_id: int, action: str, details: str = None
):
    """Komite işlemini loglar."""
    audit_log = CommitteeAuditLog(
        committee_id=committee_id, user_id=user_id, action=action, details=details
    )
    db.add(audit_log)
    db.commit()
