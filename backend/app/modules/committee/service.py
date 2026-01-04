from sqlalchemy.orm import Session
from typing import List, Optional
from app.modules.committee.repository import CommitteeRepository, CommitteeMemberRepository
from app.modules.committee.schemas import CommitteeCreate, CommitteeUpdate, CommitteeResponse
from app.core.exceptions import NotFoundError, ConflictError


class CommitteeService:
    """Komite iş mantığı servisi."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = CommitteeRepository()
        self.member_repository = CommitteeMemberRepository()
    
    def get_committee(self, committee_id: int) -> CommitteeResponse:
        """Komite getirir."""
        committee = self.repository.get_by_id(self.db, committee_id)
        if not committee:
            raise NotFoundError("Komite")
        return CommitteeResponse.model_validate(committee)
    
    def get_all_committees(self, skip: int = 0, limit: int = 100) -> List[CommitteeResponse]:
        """Tüm komiteleri getirir."""
        committees = self.repository.get_all(self.db, skip=skip, limit=limit)
        return [CommitteeResponse.model_validate(c) for c in committees]
    
    def get_committees_by_neighborhood(self, neighborhood: str) -> List[CommitteeResponse]:
        """Mahalle bazlı komiteleri getirir."""
        committees = self.repository.get_by_neighborhood(self.db, neighborhood)
        return [CommitteeResponse.model_validate(c) for c in committees]
    
    def create_committee(
        self, 
        committee_data: CommitteeCreate, 
        created_by: int
    ) -> CommitteeResponse:
        """Yeni komite oluşturur."""
        committee_dict = committee_data.model_dump()
        committee_dict["created_by"] = created_by
        
        committee = self.repository.create(self.db, committee_dict)
        return CommitteeResponse.model_validate(committee)
    
    def update_committee(
        self, 
        committee_id: int, 
        committee_data: CommitteeUpdate
    ) -> CommitteeResponse:
        """Komite bilgilerini günceller."""
        committee = self.repository.get_by_id(self.db, committee_id)
        if not committee:
            raise NotFoundError("Komite")
        
        update_data = committee_data.model_dump(exclude_unset=True)
        updated_committee = self.repository.update(self.db, committee, update_data)
        return CommitteeResponse.model_validate(updated_committee)
    
    def delete_committee(self, committee_id: int) -> None:
        """Komiteyi siler."""
        committee = self.repository.get_by_id(self.db, committee_id)
        if not committee:
            raise NotFoundError("Komite")
        self.repository.delete(self.db, committee)
    
    def add_member(self, committee_id: int, user_id: int, role: str = "member") -> None:
        """Komiteye üye ekler."""
        # Komite kontrolü
        committee = self.repository.get_by_id(self.db, committee_id)
        if not committee:
            raise NotFoundError("Komite")
        
        # Üye zaten var mı kontrolü
        existing_member = self.member_repository.get_by_committee_and_user(
            self.db, committee_id, user_id
        )
        if existing_member:
            raise ConflictError("Kullanıcı zaten bu komitenin üyesi")
        
        # Üye ekle
        member_data = {
            "committee_id": committee_id,
            "user_id": user_id,
            "role": role
        }
        self.member_repository.create(self.db, member_data)

