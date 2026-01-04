from fastapi import HTTPException, status


class BaseAPIException(HTTPException):
    """Temel API exception sınıfı."""

    def __init__(self, status_code: int, detail: str):
        super().__init__(status_code=status_code, detail=detail)


class NotFoundError(BaseAPIException):
    """Kayıt bulunamadı hatası."""

    def __init__(self, resource: str = "Kayıt"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"{resource} bulunamadı"
        )


class ValidationError(BaseAPIException):
    """Doğrulama hatası."""

    def __init__(self, detail: str = "Geçersiz veri"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class UnauthorizedError(BaseAPIException):
    """Yetkilendirme hatası."""

    def __init__(self, detail: str = "Yetkilendirme gerekli"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class ForbiddenError(BaseAPIException):
    """Erişim reddedildi hatası."""

    def __init__(self, detail: str = "Bu işlem için yetkiniz yok"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


class ConflictError(BaseAPIException):
    """Çakışma hatası."""

    def __init__(self, detail: str = "Kayıt zaten mevcut"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)
