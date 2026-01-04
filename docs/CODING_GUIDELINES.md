# Coding Guidelines

Bu doküman, projede **ortak bir dil**, **tutarlı bir kod stili** ve **yüksek okunabilirlik** sağlamak için hazırlanmıştır.

Amaç; kodun kimin tarafından yazıldığının önemsiz olduğu, herkes tarafından rahatça okunup geliştirilebildiği bir yapı oluşturmaktır.

> Bu kurallar bireysel tercihler değil, proje standartlarıdır.

---

## 1. Genel İlkeler

- Kod, makine için değil **insan için** yazılır
- Açık ve okunur kod, kısa ama anlaşılmaz koddan üstündür
- Aynı problemin tek bir doğru adı vardır
- Format tartışılmaz, araçlar tarafından belirlenir

---

## 2. Ortak Domain Dili

Projede kullanılan temel kavramlar şunlardır:

- **Neighborhood** → Mahalle
- **Committee** → Komite
- **Member** → Üye
- **Decision** → Karar
- **Announcement** → Duyuru

### Kurallar
- Kodda bu isimler **aynen** kullanılır
- Eş anlamlı veya alternatif isimlendirme yapılmaz
- Türkçe–İngilizce karışık kullanım yapılmaz

❌ `district`, `area`

✅ `neighborhood`

---

## 3. Frontend (React) Kuralları

### 3.1 Dosya ve Bileşen İsimlendirme

- React component → `PascalCase`
- Hook → `useSomething`
- Yardımcı fonksiyon → `camelCase`

Örnek:
```jsx
function DecisionList() {}
function useAuth() {}
```

---

### 3.2 Bileşen Sorumluluğu

- Bir bileşen **tek bir işi** yapmalıdır
- Büyük bileşenler alt bileşenlere bölünmelidir

❌ `DecisionPageWithListAndFormAndModal`

✅ `DecisionPage`
- `DecisionList`
- `DecisionForm`

---

### 3.3 State ve Effect Kullanımı

- Gereksiz `useEffect` kullanılmaz
- State minimumda tutulur
- Derived state tercih edilir

---

### 3.4 Frontend Araçları

- **Prettier** → format
- **ESLint** → kalite ve hatalar

Bu araçların uyarıları kişisel yorum değil, proje kuralıdır.

---

## 4. Backend (Python API) Kuralları

### 4.1 İsimlendirme

- Fonksiyon → `snake_case`
- Class → `PascalCase`
- Değişken → anlamlı ve açık

Örnek:
```python
def publish_announcement():
    pass
```

---

### 4.2 Fonksiyon Tasarımı

- Fonksiyonlar küçük olmalıdır
- Tek sorumluluk ilkesi uygulanır

❌
```python
def save_and_notify_and_log():
    pass
```

✅
```python
def save_decision():
    pass

def notify_members():
    pass
```

---

### 4.3 API Tasarımı

- REST prensipleri uygulanır
- URL’ler çoğul ve sade olur

❌ `/getDecisionList`

✅ `/decisions`

---

### 4.4 Backend Araçları

- **Black** → format
- **Ruff** → lint ve kalite

Bu araçlar tüm backend kodu için zorunludur.

---

## 5. Yorum Satırları (Comments)

### Ne Zaman Yorum Yazılır?

- Kod **neden** böyle yazıldıysa

### Ne Zaman Yazılmaz?

- Kod zaten ne yaptığını anlatıyorsa

❌
```python
# check if user is admin
if user.role == 'admin':
    pass
```

✅
```python
if user.is_admin():
    pass
```

---

## 6. Pull Request Kalite Kriterleri

Bir PR ancak şu şartlarla kabul edilir:

- Lint ve formatter geçiyor
- Naming kurallarına uyuyor
- Tek bir issue’yu çözüyor
- Okunabilir ve küçük

---

## 7. “Done” Tanımı

Bir iş **tamamlanmış** sayılırsa:

- Kod çalışıyor
- Lint / format temiz
- Gerekliyse dokümantasyon güncel

---

## 8. Review Dili

- Eleştiri kişiye değil koda yapılır
- Yapıcı ve açıklayıcı dil kullanılır

❌ “Bu yanlış”

✅ “Burada şu yaklaşımı düşünmek ister misin?”

---

## 9. Son Söz

Bu doküman:
- Tartışmayı azaltmak
- Yeni gelenleri hızlandırmak
- Kod kalitesini korumak

için vardır.

> Temiz kod bir hedef değil, alışkanlıktır.