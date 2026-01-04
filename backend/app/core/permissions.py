from typing import List
from fastapi import HTTPException, status


class Permission:
    """İzin sabitleri."""

    READ_COMMITTEE = "read:committee"
    WRITE_COMMITTEE = "write:committee"
    READ_DECISION = "read:decision"
    WRITE_DECISION = "write:decision"
    ADMIN = "admin"


class Role:
    """Rol sabitleri."""

    USER = "user"
    COMMITTEE_MEMBER = "committee_member"
    COMMITTEE_ADMIN = "committee_admin"
    SUPER_ADMIN = "super_admin"


def get_user_permissions(role: str) -> List[str]:
    """Rol bazlı izinleri döndürür."""
    role_permissions = {
        Role.USER: [Permission.READ_COMMITTEE, Permission.READ_DECISION],
        Role.COMMITTEE_MEMBER: [
            Permission.READ_COMMITTEE,
            Permission.READ_DECISION,
            Permission.WRITE_DECISION,
        ],
        Role.COMMITTEE_ADMIN: [
            Permission.READ_COMMITTEE,
            Permission.WRITE_COMMITTEE,
            Permission.READ_DECISION,
            Permission.WRITE_DECISION,
        ],
        Role.SUPER_ADMIN: [
            Permission.READ_COMMITTEE,
            Permission.WRITE_COMMITTEE,
            Permission.READ_DECISION,
            Permission.WRITE_DECISION,
            Permission.ADMIN,
        ],
    }
    return role_permissions.get(role, [])


def check_permission(user_permissions: List[str], required_permission: str) -> bool:
    """Kullanıcının gerekli izne sahip olup olmadığını kontrol eder."""
    return (
        required_permission in user_permissions or Permission.ADMIN in user_permissions
    )


def require_permission(required_permission: str):
    """İzin kontrolü için decorator/dependency."""

    def permission_checker(current_user: dict):
        user_permissions = get_user_permissions(current_user.get("role", Role.USER))
        if not check_permission(user_permissions, required_permission):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Yetersiz yetki"
            )
        return current_user

    return permission_checker
