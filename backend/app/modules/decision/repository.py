from sqlalchemy.orm import Session
from typing import List, Optional
from app.modules.decision.models import Decision, DecisionVote, DecisionStatus


class DecisionRepository:
    """Karar veritabanı işlemleri."""
    
    @staticmethod
    def get_by_id(db: Session, decision_id: int) -> Optional[Decision]:
        """ID ile karar getirir."""
        return db.query(Decision).filter(Decision.id == decision_id).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Decision]:
        """Tüm kararları getirir."""
        return db.query(Decision).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_committee(db: Session, committee_id: int) -> List[Decision]:
        """Komiteye ait kararları getirir."""
        return db.query(Decision).filter(Decision.committee_id == committee_id).all()
    
    @staticmethod
    def get_by_status(db: Session, status: DecisionStatus) -> List[Decision]:
        """Duruma göre kararları getirir."""
        return db.query(Decision).filter(Decision.status == status).all()
    
    @staticmethod
    def create(db: Session, decision_data: dict) -> Decision:
        """Yeni karar oluşturur."""
        db_decision = Decision(**decision_data)
        db.add(db_decision)
        db.commit()
        db.refresh(db_decision)
        return db_decision
    
    @staticmethod
    def update(db: Session, decision: Decision, decision_data: dict) -> Decision:
        """Karar bilgilerini günceller."""
        for key, value in decision_data.items():
            setattr(decision, key, value)
        db.commit()
        db.refresh(decision)
        return decision
    
    @staticmethod
    def delete(db: Session, decision: Decision) -> None:
        """Kararı siler."""
        db.delete(decision)
        db.commit()


class DecisionVoteRepository:
    """Karar oyu veritabanı işlemleri."""
    
    @staticmethod
    def get_by_decision_and_user(
        db: Session,
        decision_id: int,
        user_id: int
    ) -> Optional[DecisionVote]:
        """Karar ve kullanıcı ID'sine göre oy getirir."""
        return db.query(DecisionVote).filter(
            DecisionVote.decision_id == decision_id,
            DecisionVote.user_id == user_id
        ).first()
    
    @staticmethod
    def get_by_decision(db: Session, decision_id: int) -> List[DecisionVote]:
        """Karara ait tüm oyları getirir."""
        return db.query(DecisionVote).filter(
            DecisionVote.decision_id == decision_id
        ).all()
    
    @staticmethod
    def create(db: Session, vote_data: dict) -> DecisionVote:
        """Yeni oy ekler."""
        db_vote = DecisionVote(**vote_data)
        db.add(db_vote)
        db.commit()
        db.refresh(db_vote)
        return db_vote
    
    @staticmethod
    def update(db: Session, vote: DecisionVote, vote_data: dict) -> DecisionVote:
        """Oy bilgilerini günceller."""
        for key, value in vote_data.items():
            setattr(vote, key, value)
        db.commit()
        db.refresh(vote)
        return vote
    
    @staticmethod
    def delete(db: Session, vote: DecisionVote) -> None:
        """Oyu siler."""
        db.delete(vote)
        db.commit()

