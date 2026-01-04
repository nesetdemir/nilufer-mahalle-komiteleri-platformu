import logging
import sys
from logging.handlers import RotatingFileHandler
from app.core.config import settings


def setup_logging():
    """Logging yapılandırmasını kurar."""
    # Log formatı
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Root logger yapılandırması
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper()))

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(log_format, date_format)
    console_handler.setFormatter(console_formatter)

    # File handler (rotating)
    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=10485760, backupCount=5  # 10MB
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(log_format, date_format)
    file_handler.setFormatter(file_formatter)

    # Handler'ları ekle
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    return root_logger


# Logging'i başlat
logger = setup_logging()
