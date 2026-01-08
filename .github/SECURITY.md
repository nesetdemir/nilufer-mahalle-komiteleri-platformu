# Güvenlik Politikası

## Desteklenen Versiyonlar

Aşağıdaki versiyonlar güvenlik güncellemeleri ile desteklenmektedir:

| Versiyon | Destekleniyor          |
| -------- | ---------------------- |
| 0.1.x    | :white_check_mark:     |
| < 0.1    | :x:                    |

## Güvenlik Açığı Bildirimi

Güvenlik açığı bulduysanız, lütfen **özel olarak** bildirin. GitHub Issues üzerinden **açık bir şekilde** güvenlik açığı bildirmeyin.

### Bildirim Süreci

1. **E-posta ile bildirin**: [güvenlik e-posta adresiniz] (veya GitHub Security Advisory kullanın)
2. **Açıklayın**: Açığın ne olduğunu, nasıl tekrarlanabileceğini ve potansiyel etkisini açıklayın
3. **Bekleyin**: 48 saat içinde yanıt alacaksınız
4. **Takip edin**: Açığın düzeltilmesi ve yayınlanması sürecini takip edin

### Bildirim İçeriği

Lütfen şunları içeren bir bildirim gönderin:

- Açığın açıklaması
- Etkilenen versiyonlar
- Tekrarlama adımları (varsa)
- Potansiyel etki değerlendirmesi
- Önerilen çözüm (varsa)

## Güvenlik Güncellemeleri

Güvenlik açıkları tespit edildiğinde:

1. Açık kapatılır veya azaltılır
2. Güvenlik yaması hazırlanır
3. Yeni versiyon yayınlanır
4. Güvenlik danışma notu (Security Advisory) yayınlanır

## Güvenlik En İyi Uygulamaları

### Geliştiriciler İçin

- **Asla** hassas bilgileri (şifreler, API anahtarları, token'lar) kodda hardcode etmeyin
- `.env` dosyalarını asla commit etmeyin
- Güvenlik güncellemelerini düzenli olarak kontrol edin
- Bağımlılıkları güncel tutun
- Güçlü şifreler ve SECRET_KEY'ler kullanın

### Kullanıcılar İçin

- Production ortamında varsayılan şifreleri **mutlaka** değiştirin
- `SECRET_KEY`'i güçlü ve rastgele bir değerle değiştirin
- Düzenli olarak güvenlik güncellemelerini uygulayın
- HTTPS kullanın
- Veritabanı erişim bilgilerini güvenli tutun

## Güvenlik Kontrol Listesi

Production'a geçmeden önce:

- [ ] Tüm varsayılan şifreler değiştirildi
- [ ] `SECRET_KEY` güçlü ve rastgele bir değer
- [ ] `.env` dosyası `.gitignore`'da
- [ ] Veritabanı erişim bilgileri güvenli
- [ ] HTTPS etkin
- [ ] CORS yapılandırması doğru
- [ ] Tüm bağımlılıklar güncel
- [ ] Güvenlik açığı taraması yapıldı

## Güvenlik Özellikleri

Bu proje şu güvenlik özelliklerini içerir:

- JWT tabanlı kimlik doğrulama
- Şifre hash'leme (bcrypt)
- Rol bazlı erişim kontrolü (RBAC)
- CORS yapılandırması
- SQL injection koruması (SQLAlchemy ORM)
- XSS koruması (Next.js built-in)

## Bağımlılık Güvenliği

Proje, güvenlik açıklarını tespit etmek için:

- Dependabot kullanır (otomatik güvenlik güncellemeleri)
- Düzenli güvenlik taramaları yapar
- Güvenlik açığı bildirimlerini takip eder

## İletişim

Güvenlik konuları için: [GitHub Security Advisory](https://github.com/nesetdemir/nilufer-mahalle-komiteleri-platformu/security/advisories) kullanın.

## Teşekkürler

Güvenlik açığı bildiren ve projeyi daha güvenli hale getiren herkese teşekkür ederiz.
