from sqlalchemy.orm import Session
from datetime import datetime
from app.modules.decision.repository import DecisionRepository, DecisionVoteRepository
from app.modules.decision.models import DecisionStatus
from app.core.exceptions import ValidationError


class DecisionWorkflow:
    """Karar iş akışı yönetimi."""

    @staticmethod
    def can_transition(
        current_status: DecisionStatus, new_status: DecisionStatus
    ) -> bool:
        """Durum geçişi geçerli mi?"""
        valid_transitions = {
            DecisionStatus.DRAFT: [DecisionStatus.PENDING, DecisionStatus.DRAFT],
            DecisionStatus.PENDING: [
                DecisionStatus.APPROVED,
                DecisionStatus.REJECTED,
                DecisionStatus.DRAFT,
            ],
            DecisionStatus.APPROVED: [DecisionStatus.IMPLEMENTED],
            DecisionStatus.REJECTED: [DecisionStatus.DRAFT],
            DecisionStatus.IMPLEMENTED: [],
        }

        allowed_statuses = valid_transitions.get(current_status, [])
        return new_status in allowed_statuses

    @staticmethod
    def transition_decision(
        db: Session, decision_id: int, new_status: DecisionStatus, user_id: int
    ):
        """Karar durumunu geçirir."""
        repository = DecisionRepository()
        decision = repository.get_by_id(db, decision_id)

        if not decision:
            raise ValidationError("Karar bulunamadı")

        if not DecisionWorkflow.can_transition(decision.status, new_status):
            raise ValidationError(
                f"{decision.status.value} durumundan {new_status.value} durumuna geçiş yapılamaz"
            )

        update_data = {"status": new_status}

        if new_status == DecisionStatus.APPROVED:
            update_data["approved_at"] = datetime.utcnow()

        repository.update(db, decision, update_data)

    @staticmethod
    def check_voting_complete(db: Session, decision_id: int) -> bool:
        """Oylama tamamlandı mı?"""
        vote_repository = DecisionVoteRepository()
        votes = vote_repository.get_by_decision(db, decision_id)

        # Basit kontrol: En az 3 oy var mı?
        # Gerçek uygulamada komite üye sayısına göre hesaplanmalı
        return len(votes) >= 3

    @staticmethod
    def auto_approve_if_ready(db: Session, decision_id: int):
        """Oylama tamamlandıysa otomatik onayla."""
        repository = DecisionRepository()
        decision = repository.get_by_id(db, decision_id)

        if not decision:
            return

        if decision.status != DecisionStatus.PENDING:
            return

        if DecisionWorkflow.check_voting_complete(db, decision_id):
            # Oyları say
            vote_repository = DecisionVoteRepository()
            votes = vote_repository.get_by_decision(db, decision_id)

            approve_count = sum(1 for v in votes if v.vote == "approve")
            reject_count = sum(1 for v in votes if v.vote == "reject")

            if approve_count > reject_count:
                DecisionWorkflow.transition_decision(
                    db, decision_id, DecisionStatus.APPROVED, decision.created_by
                )
