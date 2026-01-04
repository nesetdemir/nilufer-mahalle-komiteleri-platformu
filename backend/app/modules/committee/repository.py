from sqlalchemy.orm import Session
from typing import List, Optional
from app.modules.committee.models import Committee, CommitteeMember


class CommitteeRepository:
    """Komite veritabanı işlemleri."""

    @staticmethod
    def get_by_id(db: Session, committee_id: int) -> Optional[Committee]:
        """ID ile komite getirir."""
        return db.query(Committee).filter(Committee.id == committee_id).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Committee]:
        """Tüm komiteleri getirir."""
        return db.query(Committee).offset(skip).limit(limit).all()

    @staticmethod
    def get_by_neighborhood(db: Session, neighborhood: str) -> List[Committee]:
        """Mahalle bazlı komiteleri getirir."""
        return db.query(Committee).filter(Committee.neighborhood == neighborhood).all()

    @staticmethod
    def create(db: Session, committee_data: dict) -> Committee:
        """Yeni komite oluşturur."""
        db_committee = Committee(**committee_data)
        db.add(db_committee)
        db.commit()
        db.refresh(db_committee)
        return db_committee

    @staticmethod
    def update(db: Session, committee: Committee, committee_data: dict) -> Committee:
        """Komite bilgilerini günceller."""
        for key, value in committee_data.items():
            setattr(committee, key, value)
        db.commit()
        db.refresh(committee)
        return committee

    @staticmethod
    def delete(db: Session, committee: Committee) -> None:
        """Komiteyi siler."""
        db.delete(committee)
        db.commit()


class CommitteeMemberRepository:
    """Komite üyesi veritabanı işlemleri."""

    @staticmethod
    def get_by_committee_and_user(
        db: Session, committee_id: int, user_id: int
    ) -> Optional[CommitteeMember]:
        """Komite ve kullanıcı ID'sine göre üye getirir."""
        return (
            db.query(CommitteeMember)
            .filter(
                CommitteeMember.committee_id == committee_id,
                CommitteeMember.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def get_by_committee(db: Session, committee_id: int) -> List[CommitteeMember]:
        """Komiteye ait tüm üyeleri getirir."""
        return (
            db.query(CommitteeMember)
            .filter(CommitteeMember.committee_id == committee_id)
            .all()
        )

    @staticmethod
    def create(db: Session, member_data: dict) -> CommitteeMember:
        """Yeni komite üyesi ekler."""
        db_member = CommitteeMember(**member_data)
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member

    @staticmethod
    def delete(db: Session, member: CommitteeMember) -> None:
        """Komite üyesini siler."""
        db.delete(member)
        db.commit()
