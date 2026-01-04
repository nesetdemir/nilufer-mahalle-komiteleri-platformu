from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_access_token
from app.modules.auth.repository import UserRepository
from app.modules.auth.schemas import UserResponse
from app.core.exceptions import UnauthorizedError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> UserResponse:
    """Mevcut kullanıcıyı token'dan alır."""
    credentials_exception = UnauthorizedError("Kimlik doğrulama başarısız")
    
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
    
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    
    repository = UserRepository()
    user = repository.get_by_username(db, username)
    if user is None:
        raise credentials_exception
    
    if not user.is_active:
        raise UnauthorizedError("Kullanıcı hesabı aktif değil")
    
    return UserResponse.model_validate(user)


async def get_current_active_user(
    current_user: UserResponse = Depends(get_current_user)
) -> UserResponse:
    """Aktif kullanıcıyı döndürür."""
    if not current_user.is_active:
        raise UnauthorizedError("Kullanıcı hesabı aktif değil")
    return current_user

