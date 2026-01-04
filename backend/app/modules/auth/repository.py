from sqlalchemy.orm import Session
from typing import Optional
from app.modules.auth.models import User


class UserRepository:
    """Kullanıcı veritabanı işlemleri."""
    
    @staticmethod
    def get_by_id(db: Session, user_id: int) -> Optional[User]:
        """ID ile kullanıcı getirir."""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_by_username(db: Session, username: str) -> Optional[User]:
        """Kullanıcı adı ile kullanıcı getirir."""
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        """Email ile kullanıcı getirir."""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def create(db: Session, user_data: dict) -> User:
        """Yeni kullanıcı oluşturur."""
        db_user = User(**user_data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def update(db: Session, user: User, user_data: dict) -> User:
        """Kullanıcı bilgilerini günceller."""
        for key, value in user_data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def delete(db: Session, user: User) -> None:
        """Kullanıcıyı siler."""
        db.delete(user)
        db.commit()

