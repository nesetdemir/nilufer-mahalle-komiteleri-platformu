# Contributing Guide

Bu doküman, projeye katkı sunmak isteyen herkes için hazırlanmıştır. Amacımız; katkı sürecini **adil**, **şeffaf**, **düzenli** ve **öğretici** hale getirmektir.

Bu projede katkı sunmak bir ayrıcalık değil, **sorumluluktur**.

---

## 1. Kimler Katkı Sunabilir?

- Yazılımcılar (backend / frontend / devops)
- Tasarımcılar
- Dokümantasyon yazarları
- Test ve geri bildirim sağlayanlar

Yeni başlıyor olman **engel değildir**. Kurallara uyman yeterlidir.

---

## 2. Katkı Türleri

Projeye şu yollarla katkı sunabilirsin:

- 🧩 Yeni özellik geliştirme (Feature)
- 🐞 Hata düzeltme (Bugfix)
- 📝 Dokümantasyon iyileştirme
- 🧹 Kod temizliği / refactor
- 💡 Öneri ve geri bildirim

Her katkı **issue ile başlar**.

---

## 3. Issue Olmadan Katkı Yapılmaz

> **Issue yoksa iş yoktur.**

Bir konu üzerinde çalışmadan önce:

1. Açık issue’ları kontrol et
2. Uygun bir issue yoksa **yeni issue aç**
3. Issue onaylanmadan koda başlama

Bu kural, emeğin boşa gitmemesi içindir.

---

## 4. Issue Seçme ve Atama

- Kendine atanmamış issue üzerinde çalışmaya başlama
- Bir issue = bir kişi (istisnalar hariç)
- Büyük issue’lar parçalara bölünür

Yeni başlayanlar için `good first issue` etiketli işler önerilir.

---

## 5. Branch Stratejisi

- `main` → her zaman stabil
- `feature/issue-<no>-kisa-aciklama`

Örnek:
```bash
git checkout -b feature/issue-12-login-endpoint
```

> `main` branch’e **direkt commit atılmaz**.

---

## 6. Commit Mesaj Kuralları

Commit mesajları **açık ve kısa** olmalıdır.

Örnek:
```text
feat: add token based authentication
fix: prevent unauthorized access to endpoint
docs: update setup instructions
```

- feat → yeni özellik
- fix → hata düzeltme
- docs → dokümantasyon

---

## 7. Pull Request (PR) Süreci

PR açmadan önce:
- Kod çalışıyor olmalı
- Issue ile ilişkilendirilmiş olmalı

PR açarken:
- Issue numarasını belirt
- Ne yaptığını net yaz
- Gerekirse ekran görüntüsü ekle

### PR İnceleme Kuralları
- En az 1 onay olmadan merge edilmez
- Geri bildirimler dikkate alınır
- Tartışmalar issue veya PR üzerinden yapılır

---

## 8. Kod Kalitesi ve Stil

- Okunabilirlik önceliklidir
- Karmaşık çözümlerden kaçınılır
- Aynı problemi çözen mevcut yapı varsa tekrar edilmez

> Temiz kod, hızlı koddan değerlidir.

---

## 9. Test ve Doğrulama

- Yeni özellik → mümkünse test eklenmeli
- Mevcut testler bozulmamalı
- En azından manuel test yapılmalı

---

## 10. Dokümantasyon Sorumluluğu

Kod yazdıysan, gerekiyorsa dokümantasyon da yazarsın.

- Yeni endpoint → açıklama
- Yeni konfigürasyon → README güncellemesi

---

## 11. İletişim ve Davranış

- Saygılı ve açık iletişim
- Kişiye değil probleme odaklanma
- Yapıcı eleştiri

Bu proje bir topluluktur.

---

## 12. Kabul Edilmeyen Katkılar

- Issue dışı yapılan işler
- Kurallara aykırı PR’lar
- Kapsamı aşan değişiklikler

Bu katkılar reddedilebilir.

---

## 13. Son Söz

Bu rehber kısıtlamak için değil, **herkesin emeğini korumak** için vardır.

> Küçük ama doğru katkılar, büyük projeler doğurur.

Katkın için teşekkürler.
