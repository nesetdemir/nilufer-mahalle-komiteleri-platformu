from sqlalchemy.orm import Session
from typing import Optional
from datetime import timedelta
from app.modules.auth.repository import UserRepository
from app.modules.auth.schemas import UserCreate, UserResponse
from app.core.security import verify_password, get_password_hash, create_access_token
from app.core.config import settings
from app.core.exceptions import UnauthorizedError, ConflictError, NotFoundError


class AuthService:
    """Kimlik doğrulama servisi."""
    
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository()
    
    def authenticate_user(self, username: str, password: str) -> Optional[UserResponse]:
        """Kullanıcı kimlik doğrulaması yapar."""
        user = self.repository.get_by_username(self.db, username)
        if not user:
            return None
        
        if not verify_password(password, user.hashed_password):
            return None
        
        if not user.is_active:
            raise UnauthorizedError("Kullanıcı hesabı aktif değil")
        
        return UserResponse.model_validate(user)
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        """Yeni kullanıcı oluşturur."""
        # Kullanıcı adı kontrolü
        if self.repository.get_by_username(self.db, user_data.username):
            raise ConflictError("Bu kullanıcı adı zaten kullanılıyor")
        
        # Email kontrolü
        if self.repository.get_by_email(self.db, user_data.email):
            raise ConflictError("Bu email adresi zaten kullanılıyor")
        
        # Şifreyi hash'le
        hashed_password = get_password_hash(user_data.password)
        
        # Kullanıcı oluştur
        user_dict = user_data.model_dump(exclude={"password"})
        user_dict["hashed_password"] = hashed_password
        
        user = self.repository.create(self.db, user_dict)
        return UserResponse.model_validate(user)
    
    def create_access_token_for_user(self, user: UserResponse) -> str:
        """Kullanıcı için access token oluşturur."""
        token_data = {
            "sub": user.username,
            "user_id": user.id,
            "role": user.role
        }
        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        return create_access_token(data=token_data, expires_delta=expires_delta)
    
    def get_user_by_id(self, user_id: int) -> UserResponse:
        """ID ile kullanıcı getirir."""
        user = self.repository.get_by_id(self.db, user_id)
        if not user:
            raise NotFoundError("Kullanıcı")
        return UserResponse.model_validate(user)

