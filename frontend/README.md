# Frontend - Nilüfer Mahalle Komiteleri Platformu

Next.js tabanlı frontend uygulaması.

## Yapı

```
frontend/
├── app/              # Next.js App Router
├── components/       # React bileşenleri
├── lib/              # Yardımcı fonksiyonlar
└── public/           # Statik dosyalar
```

## Kurulum

### Gereksinimler
- Node.js 18+
- npm veya yarn

### Adımlar

1. Bağımlılıkları yükle:
```bash
npm install
# veya
yarn install
```

2. Ortam değişkenlerini ayarla:
```bash
cp .env.example .env.local
# .env.local dosyasını düzenle
```

3. Geliştirme sunucusunu başlat:
```bash
npm run dev
# veya
yarn dev
```

Uygulama http://localhost:3000 adresinde çalışacaktır.

## Build

Production build için:
```bash
npm run build
npm start
```

## Teknolojiler

- Next.js 14 (App Router)
- TypeScript
- React 18
