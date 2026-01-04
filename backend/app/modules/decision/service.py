from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.modules.decision.repository import DecisionRepository, DecisionVoteRepository
from app.modules.decision.schemas import DecisionCreate, DecisionUpdate, DecisionResponse
from app.modules.decision.models import DecisionStatus
from app.core.exceptions import NotFoundError, ValidationError


class DecisionService:
    """Karar iş mantığı servisi."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = DecisionRepository()
        self.vote_repository = DecisionVoteRepository()
    
    def get_decision(self, decision_id: int) -> DecisionResponse:
        """Karar getirir."""
        decision = self.repository.get_by_id(self.db, decision_id)
        if not decision:
            raise NotFoundError("Karar")
        return DecisionResponse.model_validate(decision)
    
    def get_all_decisions(self, skip: int = 0, limit: int = 100) -> List[DecisionResponse]:
        """Tüm kararları getirir."""
        decisions = self.repository.get_all(self.db, skip=skip, limit=limit)
        return [DecisionResponse.model_validate(d) for d in decisions]
    
    def get_decisions_by_committee(self, committee_id: int) -> List[DecisionResponse]:
        """Komiteye ait kararları getirir."""
        decisions = self.repository.get_by_committee(self.db, committee_id)
        return [DecisionResponse.model_validate(d) for d in decisions]
    
    def create_decision(
        self,
        decision_data: DecisionCreate,
        created_by: int
    ) -> DecisionResponse:
        """Yeni karar oluşturur."""
        decision_dict = decision_data.model_dump()
        decision_dict["created_by"] = created_by
        decision_dict["status"] = DecisionStatus.DRAFT
        
        decision = self.repository.create(self.db, decision_dict)
        return DecisionResponse.model_validate(decision)
    
    def update_decision(
        self,
        decision_id: int,
        decision_data: DecisionUpdate
    ) -> DecisionResponse:
        """Karar bilgilerini günceller."""
        decision = self.repository.get_by_id(self.db, decision_id)
        if not decision:
            raise NotFoundError("Karar")
        
        update_data = decision_data.model_dump(exclude_unset=True)
        
        # Status değişikliği kontrolü
        if "status" in update_data:
            new_status = update_data["status"]
            if new_status == DecisionStatus.APPROVED and decision.status != DecisionStatus.APPROVED:
                update_data["approved_at"] = datetime.utcnow()
        
        updated_decision = self.repository.update(self.db, decision, update_data)
        return DecisionResponse.model_validate(updated_decision)
    
    def delete_decision(self, decision_id: int) -> None:
        """Kararı siler."""
        decision = self.repository.get_by_id(self.db, decision_id)
        if not decision:
            raise NotFoundError("Karar")
        self.repository.delete(self.db, decision)
    
    def submit_vote(self, decision_id: int, user_id: int, vote: str, comment: str = None) -> None:
        """Karara oy verir."""
        # Karar kontrolü
        decision = self.repository.get_by_id(self.db, decision_id)
        if not decision:
            raise NotFoundError("Karar")
        
        # Oy değeri kontrolü
        valid_votes = ["approve", "reject", "abstain"]
        if vote not in valid_votes:
            raise ValidationError(f"Geçersiz oy değeri. Geçerli değerler: {', '.join(valid_votes)}")
        
        # Daha önce oy verilmiş mi kontrolü
        existing_vote = self.vote_repository.get_by_decision_and_user(
            self.db, decision_id, user_id
        )
        
        vote_data = {
            "decision_id": decision_id,
            "user_id": user_id,
            "vote": vote,
            "comment": comment
        }
        
        if existing_vote:
            # Mevcut oyu güncelle
            self.vote_repository.update(self.db, existing_vote, vote_data)
        else:
            # Yeni oy ekle
            self.vote_repository.create(self.db, vote_data)

