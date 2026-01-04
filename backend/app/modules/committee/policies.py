from app.modules.committee.repository import (
    CommitteeRepository,
    CommitteeMemberRepository,
)
from app.modules.auth.schemas import UserResponse
from app.core.exceptions import ForbiddenError


class CommitteePolicy:
    """Komite erişim politikaları."""

    @staticmethod
    def can_create_committee(user: UserResponse) -> bool:
        """Kullanıcı komite oluşturabilir mi?"""
        # Şimdilik tüm aktif kullanıcılar komite oluşturabilir
        return user.is_active

    @staticmethod
    def can_update_committee(user: UserResponse, committee_id: int, db) -> bool:
        """Kullanıcı komiteyi güncelleyebilir mi?"""
        # Komite oluşturan veya admin rolüne sahip olanlar güncelleyebilir
        committee_repo = CommitteeRepository()
        committee = committee_repo.get_by_id(db, committee_id)

        if not committee:
            return False

        if committee.created_by == user.id:
            return True

        if user.role == "super_admin":
            return True

        # Komite admin'i kontrolü
        member_repo = CommitteeMemberRepository()
        member = member_repo.get_by_committee_and_user(db, committee_id, user.id)
        if member and member.role == "admin":
            return True

        return False

    @staticmethod
    def can_delete_committee(user: UserResponse, committee_id: int, db) -> bool:
        """Kullanıcı komiteyi silebilir mi?"""
        # Sadece komite oluşturan veya super admin silebilir
        committee_repo = CommitteeRepository()
        committee = committee_repo.get_by_id(db, committee_id)

        if not committee:
            return False

        if committee.created_by == user.id:
            return True

        if user.role == "super_admin":
            return True

        return False

    @staticmethod
    def require_can_update_committee(user: UserResponse, committee_id: int, db):
        """Komite güncelleme yetkisi kontrolü."""
        if not CommitteePolicy.can_update_committee(user, committee_id, db):
            raise ForbiddenError("Bu komiteyi güncelleme yetkiniz yok")

    @staticmethod
    def require_can_delete_committee(user: UserResponse, committee_id: int, db):
        """Komite silme yetkisi kontrolü."""
        if not CommitteePolicy.can_delete_committee(user, committee_id, db):
            raise ForbiddenError("Bu komiteyi silme yetkiniz yok")


# Modül seviyesinde export için wrapper fonksiyonlar
def require_can_update_committee(user: UserResponse, committee_id: int, db):
    """Komite güncelleme yetkisi kontrolü (modül seviyesi wrapper)."""
    CommitteePolicy.require_can_update_committee(user, committee_id, db)


def require_can_delete_committee(user: UserResponse, committee_id: int, db):
    """Komite silme yetkisi kontrolü (modül seviyesi wrapper)."""
    CommitteePolicy.require_can_delete_committee(user, committee_id, db)
