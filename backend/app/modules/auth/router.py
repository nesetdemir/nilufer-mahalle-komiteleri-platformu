from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.auth.service import AuthService
from app.modules.auth.schemas import LoginRequest, UserCreate, UserResponse, Token
from app.modules.auth.dependencies import get_current_active_user
from app.core.exceptions import UnauthorizedError

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token, status_code=status.HTTP_200_OK)
async def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    """Kullanıcı girişi."""
    service = AuthService(db)
    user = service.authenticate_user(login_data.username, login_data.password)
    
    if not user:
        raise UnauthorizedError("Geçersiz kullanıcı adı veya şifre")
    
    access_token = service.create_access_token_for_user(user)
    return Token(access_token=access_token, token_type="bearer")


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """Yeni kullanıcı kaydı."""
    service = AuthService(db)
    return service.create_user(user_data)


@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user: UserResponse = Depends(get_current_active_user)
):
    """Mevcut kullanıcı bilgilerini getirir."""
    return current_user

