# Sistem Mimarisi

## Genel Bakış

Nilüfer Mahalle Komiteleri Platformu, modern web uygulaması mimarisi prensiplerine göre tasarlanmıştır.

## Mimari Katmanlar

### 1. Frontend (Next.js)
- **Teknoloji**: Next.js 14+ (App Router)
- **Dil**: TypeScript
- **State Management**: React Context / Zustand (ileride)
- **HTTP Client**: Fetch API / Axios

### 2. Backend (FastAPI)
- **Teknoloji**: FastAPI
- **Dil**: Python 3.11+
- **ORM**: SQLAlchemy
- **Migration**: Alembic
- **Authentication**: JWT

### 3. Veritabanı
- **Teknoloji**: PostgreSQL 15+
- **Bağlantı**: SQLAlchemy ORM

## Modüler Yapı

### Domain-Driven Design (DDD) Yaklaşımı

Backend, domain bazlı modüler yapıya sahiptir:

- **auth**: Kimlik doğrulama ve yetkilendirme
- **committee**: Komite yönetimi
- **decision**: Karar alma süreçleri

Her modül şu bileşenlere sahiptir:
- `router.py`: API endpoint'leri
- `service.py`: İş mantığı
- `schemas.py`: Pydantic modelleri
- `models.py`: SQLAlchemy modelleri
- `repository.py`: Veritabanı erişim katmanı

## Güvenlik

- JWT tabanlı kimlik doğrulama
- Rol bazlı erişim kontrolü (RBAC)
- API rate limiting (ileride)
- CORS yapılandırması

## Deployment

- Docker ve Docker Compose ile containerization
- Ayrı servisler: frontend, backend, postgres
- Volume'ler ile veri kalıcılığı

## Gelecek Geliştirmeler

- Redis cache katmanı
- Message queue (Celery/RabbitMQ)
- Monitoring ve logging (Prometheus, Grafana)
- CI/CD pipeline
