# Open Source Proje Rehberi

Bu doküman, **daha önce hiç open source veya büyük ölçekli yazılım projesinde çalışmamış kişiler** için hazırlanmıştır. Amaç; projenin **neden bu şekilde kurgulandığını**, **hangi parçanın ne işe yaradığını** ve **projede çalışırken hangi kurallara uyulması gerektiğini** net biçimde anlatmaktır.

Bu rehberi okuyan biri, projeye teknik ya da teknik olmayan katkı sunabilecek seviyeye gelmelidir.

---

## 1. Bu Proje Nedir?

Bu proje, mahalle komitelerinin dijital ortamda **şeffaf**, **katılımcı** ve **izlenebilir** şekilde çalışabilmesini sağlayan açık kaynaklı bir yazılım platformudur.

### Temel Amaçlar
- Kararların kayıt altına alınması
- Duyuru ve bilgilendirmelerin herkese açık yapılması
- Katılımın artırılması
- Şeffaflık ve hesap verebilirlik

Bu nedenle proje:
- Açık kaynaklıdır
- Herkesin inceleyip katkı sunabileceği şekilde geliştirilir
- Küçük adımlarla ama düzenli ilerler

---

## 2. Open Source Ne Demektir?

Open source (açık kaynak), projenin:
- Kodlarının herkese açık olması
- İsteyen herkesin inceleyebilmesi
- Katkı sunabilmesi
- Hataları bildirebilmesi

anlamına gelir.

### Bu Ne Anlama Gelmez?
- Herkes kafasına göre değişiklik yapamaz
- Kuralsız geliştirme olmaz
- İnceleme (review) olmadan kod eklenmez

Açık kaynak = **disiplin + şeffaflık**

---

## 3. Proje Yapısının Büyük Resmi

Projeyi bir bina gibi düşünebilirsin:

- Temel → Altyapı (backend, frontend, docker)
- Katlar → Özellikler (auth, kararlar, duyurular)
- Kapılar → API’ler
- Güvenlik → Yetkilendirme ve roller

Bu yapı parça parça, kontrollü şekilde inşa edilir.

---

## 4. Repo Yapısı (Basit Anlatım)

```text
root/
├── backend/        # Sunucu tarafı (veri, iş kuralları)
├── frontend/       # Kullanıcının gördüğü arayüz
├── docker/         # Herkesin aynı ortamda çalışması için
├── docs/           # Dokümantasyonlar
├── .github/        # Issue, PR ve proje kuralları
├── README.md       # Projeyi anlatan ana dosya
```

### Backend Ne İşe Yarar?
- Veritabanı ile konuşur
- Kuralları uygular
- Güvenliği sağlar

Örnek:
> “Bu kullanıcı bu kararı görmeye yetkili mi?”

### Frontend Ne İşe Yarar?
- Kullanıcı arayüzü
- Formlar, listeler, ekranlar

Örnek:
> “Mahalle duyurularını listele”

---

## 5. Issue Nedir? Neden Bu Kadar Önemli?

**Issue = Yapılacak işin resmi tanımıdır**

Bir iş:
- Issue yoksa → yapılmış sayılmaz
- Issue kapalıysa → tamamlanmıştır

### Issue Türleri
- Feature → Yeni özellik
- Bug → Hata
- Docs → Dokümantasyon
- Chore → Teknik düzenleme

### İyi Bir Issue Nasıl Olur?
- Ne yapılacağı nettir
- Nerede biteceği bellidir
- Kabul kriterleri vardır

Örnek:
> “Login sistemi yapılacak” ❌

> “Token bazlı login endpoint’i oluşturulacak, token olmadan erişim engellenecek” ✅

---

## 6. Sprint Nedir?

Sprint, **küçük ve yönetilebilir bir zaman dilimi** demektir.

Bu projede:
- 1 sprint = 1–2 hafta
- Sprint başında işler bellidir
- Sprint sonunda çıkan şey çalışır durumdadır

### Sprint Mantığı
> “Her şeyi yapalım” ❌
> “Bu sürede şunları bitirelim” ✅

---

## 7. Milestone Nedir?

Milestone = Büyük hedef

Örnek:
- MVP – Temel Altyapı
- Katılım Modülleri
- Şeffaflık ve Raporlama

Bir milestone içinde birden fazla sprint olabilir.

---

## 8. Release Nedir?

Release, projenin **dış dünyaya verdiği sözdür**.

> “Bu sürüm şu özellikleri içeriyor ve çalışıyor.”

### Version Numaraları

```text
v0.1.0 → Temel altyapı
v0.2.0 → Yeni modüller
v1.0.0 → Stabil sürüm
```

- 0.x → Geliştirme aşaması
- 1.0.0 → Üretime hazır

---

## 9. Pull Request (PR) Nedir?

PR = “Ben bir şey yaptım, lütfen inceleyin” demektir.

Kurallar:
- PR issuesuz olmaz
- PR incelemesiz merge edilmez
- Küçük PR makbuldür

### İyi PR Örneği
- Tek iş yapar
- Açıklaması nettir
- Issue numarası içerir

---

## 10. Katkı Sunarken Uyulması Gerekenler

### Yapılması Gerekenler
- Issue okumadan işe başlamamak
- Kurallara uymak
- Açık ve net iletişim

### Yapılmaması Gerekenler
- Main branch’e direkt commit
- Kapsam dışı iş eklemek
- "Ben yaptım oldu" yaklaşımı

---

## 11. Yeni Başlayanlar İçin Yol Haritası

1. README oku
2. Projeyi çalıştır
3. Açık issue’lara bak
4. Küçük bir issue seç
5. PR aç
6. Geri bildirim al

Bu süreç tekrar eder.

---

## 12. Son Söz

Bu proje bir yazılım projesinden fazlasıdır.

- Düzenlidir
- Şeffaftır
- Sabır ister
- Ekip işidir

> Küçük katkılar, büyük güven üretir.

Bu rehber, herkesin aynı dili konuşması için vardır.
