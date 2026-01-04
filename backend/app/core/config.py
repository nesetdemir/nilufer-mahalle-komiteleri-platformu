from pydantic_settings import BaseSettings
from typing import Optional, List
import json


class Settings(BaseSettings):
    # Uygulama
    APP_NAME: str = "Nilüfer Mahalle Komiteleri Platformu"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    
    # Veritabanı
    DATABASE_URL: str
    
    # Güvenlik
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS - JSON string olarak parse edilir
    CORS_ORIGINS: str = '["http://localhost:3000"]'
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    @property
    def cors_origins_list(self) -> List[str]:
        """CORS origins'i liste olarak döndürür."""
        try:
            return json.loads(self.CORS_ORIGINS)
        except (json.JSONDecodeError, TypeError):
            return ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

