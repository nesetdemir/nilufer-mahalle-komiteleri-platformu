# Mahalle Komiteleri Dijital Platformu

Bu repo, mahalle komitelerinin karar alma, duyuru yapma ve katılım süreçlerini **şeffaf**, **izlenebilir** ve **dijital** hale getirmek amacıyla geliştirilen açık kaynaklı bir yazılım platformunu içerir.

Bu proje bir ürün olduğu kadar, bir **topluluk çalışmasıdır**.

---

## 🎯 Projenin Amacı

Mahalle komiteleri genellikle:
- Kararları dağınık biçimde alır
- Duyuruları herkese eşit ulaştıramaz
- Süreçleri geriye dönük izleyemez

Bu platform ile:
- Alınan kararlar kayıt altına alınır
- Duyurular merkezi olarak yayınlanır
- Katılım ve şeffaflık artar
- Herkes aynı bilgiye erişir

---

## 🧩 Neler Sunar?

- Kullanıcı, rol ve mahalle bazlı yapı
- Token tabanlı kimlik doğrulama
- Modüler ve genişletilebilir mimari
- Docker ile kolay kurulum
- Açık kaynak geliştirme modeli

> Not: Proje aktif geliştirme aşamasındadır ve henüz üretim ortamı için hazır değildir.

---

## 🏗️ Proje Yapısı

```text
root/
├── backend/        # Sunucu tarafı (iş kuralları, API)
├── frontend/       # Kullanıcı arayüzü
├── docker/         # Geliştirme ortamı
├── docs/           # Dokümantasyonlar
├── .github/        # Issue, PR ve proje şablonları
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── README.md
```

---

## 🚀 Hızlı Başlangıç

### Gereksinimler
- Docker
- Docker Compose

### Kurulum

```bash
git clone https://github.com/ORG/REPO.git
cd REPO
docker-compose up
```

Kurulum sonrası:
- Backend varsayılan olarak `http://localhost:8000`
- Frontend varsayılan olarak `http://localhost:3000`

---

## 🧠 Nasıl Geliştiriyoruz?

Bu proje **sprint**, **issue** ve **release** temelli ilerler.

- Her iş bir issue’dur
- Issue’lar sprint’lere alınır
- Sprint sonunda release çıkar

### Versiyonlama

- `v0.x.x` → Geliştirme aşaması
- `v1.0.0` → Stabil sürüm

İlk resmi sürüm: **v0.1.0 – Foundation Release**

---

## 🤝 Katkı Sunmak

Katkı sunmak istiyorsanız:

1. README’yi okuyun
2. Açık issue’lara göz atın
3. CONTRIBUTING.md dosyasını inceleyin
4. Uygun bir issue seçin
5. Pull Request açın

👉 Detaylar için: [CONTRIBUTING.md](./docs/CONTRIBUTING.md)

---

## 🧭 Davranış Kuralları

Bu projede herkes için geçerli davranış kuralları vardır.

👉 [CODE_OF_CONDUCT.md](./docs/CODE_OF_CONDUCT.md)

---

## 📌 Yol Haritası

- v0.1.0 → Temel altyapı
- v0.2.0 → Karar ve duyuru modülleri
- v0.3.0 → Katılım ve raporlama
- v1.0.0 → Stabil sürüm

---

## 📣 Geri Bildirim

- Hata bildirimleri için issue açabilirsiniz
- Önerileriniz değerlidir

Bu proje, geri bildirimlerle gelişir.

---

## 📄 Lisans

Bu proje açık kaynaklıdır. Lisans detayları için `LICENSE` dosyasına bakınız.
