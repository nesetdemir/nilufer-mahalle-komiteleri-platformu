from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """Temel kullanıcı şeması."""

    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """Kullanıcı oluşturma şeması."""

    password: str


class UserUpdate(BaseModel):
    """Kullanıcı güncelleme şeması."""

    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


class UserResponse(UserBase):
    """Kullanıcı yanıt şeması."""

    id: int
    is_active: bool
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    """Token şeması."""

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Token veri şeması."""

    username: Optional[str] = None


class LoginRequest(BaseModel):
    """Giriş isteği şeması."""

    username: str
    password: str
