# Backend - Nilüfer Mahalle Komiteleri Platformu

FastAPI tabanlı backend uygulaması.

## Yapı

```
backend/
├── app/
│   ├── modules/          # Domain bazlı modüller
│   │   ├── auth/         # Kimlik doğrulama
│   │   ├── committee/    # Komite yönetimi
│   │   └── decision/     # Karar alma
│   ├── core/             # Ortak altyapı
│   ├── api.py            # Router aggregation
│   └── main.py           # FastAPI app
├── migrations/           # Alembic migrations
├── tests/                # Test dosyaları
├── alembic.ini           # Alembic yapılandırması
└── requirements.txt      # Python bağımlılıkları
```

## Kurulum

### Gereksinimler
- Python 3.11+
- PostgreSQL 15+

### Adımlar

1. Sanal ortam oluştur:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Bağımlılıkları yükle:
```bash
pip install -r requirements.txt
```

3. Ortam değişkenlerini ayarla:
```bash
cp .env.example .env
# .env dosyasını düzenle
```

4. Veritabanı migration'larını çalıştır:
```bash
alembic upgrade head
```

5. Uygulamayı başlat:
```bash
uvicorn app.main:app --reload
```

## API Dokümantasyonu

Uygulama çalıştıktan sonra:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Test

```bash
pytest
```

## Modüller

### Auth
Kullanıcı kimlik doğrulama ve yetkilendirme.

### Committee
Komite yönetimi, üye yönetimi ve erişim kontrolü.

### Decision
Karar alma süreçleri, oylama ve iş akışı yönetimi.
