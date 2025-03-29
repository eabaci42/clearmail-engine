# Clearmail Engine - Geliştirme Notları

Bu belge, Clearmail Engine projesinin geliştirme sürecinde dikkat edilmesi gereken teknik noktaları, mimariye ilişkin detayları ve kodlama uygulamalarını içerir.

## Go Kodlama Standartları

Clearmail Engine'in Go ile yazılmış bileşenleri için aşağıdaki kodlama standartlarına uyulmalıdır:

### Paket Yapısı

```
cmd/
  clearmail/        # Ana çalıştırılabilir
api/
  handlers/         # API handler'ları
  middleware/       # Middleware'ler
  routes/           # Route tanımları
  server/           # API sunucu yapılandırması
internal/
  exchange/         # Exchange servisi
  config/           # Yapılandırma
  models/           # Veri modelleri
  services/         # İş mantığı servisleri
  storage/          # Depolama katmanı
pkg/
  logger/           # Loglama paketi
  auth/             # Kimlik doğrulama
  utils/            # Yardımcı fonksiyonlar
```

### Hata Yönetimi

- Hataları wrap edin ve bağlam ekleyin (`fmt.Errorf("context: %w", err)`)
- Hatalar loglanmalı ve takip edilebilir olmalı
- API hatalarını standarize edin

### Loglama

- Structured logging kullanın
- Log seviyelerini doğru belirleyin (DEBUG, INFO, WARN, ERROR)
- Hassas bilgileri loglamayın

### Dependency Injection

- Bağımlılıkları constructor'a enjekte edin
- Interface'ler üzerinden iletişim kurun
- Kolay test edilebilirlik için mock'lanabilir tasarım

### Testler

- Table-driven testleri tercih edin
- Mock'lar için testify/mock veya gomock kullanın
- Benchmark testleri yazın

## Rust Kodlama Standartları

Clearmail Engine'in Rust ile yazılmış bileşenleri için aşağıdaki kodlama standartlarına uyulmalıdır:

### Proje Yapısı

```
rule-engine/
  src/
    lib.rs          # Kütüphane giriş noktası
    engine/         # Kural motoru çekirdeği
    models/         # Veri modelleri
    matchers/       # Eşleştirme algoritmaları
    actions/        # Eylem uygulamaları
    ffi/            # Go entegrasyonu için FFI
  benches/          # Benchmark testleri
  tests/            # Entegrasyon testleri
```

### Bellek Yönetimi

- Gereksiz klonlamaktan kaçının
- Referans kullanımını optimize edin
- Arena tahsisini düşünün (yüksek performanslı senaryolar için)

### Eşzamanlılık

- Tokio runtime kullanın
- Rayon ile paralel işleme
- Thread havuzu ve iş dağılımını optimize edin

### FFI ve Entegrasyon

- C ABI uyumlu arayüzler tanımlayın
- Hata ve bellek yönetimine dikkat edin
- Veri serileştirme için protobuf veya flatbuffers düşünün

### Performans Optimizasyonları

- SIMD kullanın (uygun olduğunda)
- Önbellek dostu veri yapıları tasarlayın
- Hot path optimizasyonu yapın

## Mikroservis Mimarisi

Clearmail Engine v0.4.x ve sonrası için mikroservis mimarisine geçişte aşağıdaki prensiplere uyulmalıdır:

### Servis Sınırları

- Her mikroservis tek bir iş sorumluluğuna sahip olmalı
- Bağımsız dağıtılabilir ve ölçeklendirilebilir olmalı
- Veritabanı ve kaynak izolasyonu sağlanmalı

### İletişim Modeli

- Senkron iletişim için gRPC tercih edin
- Asenkron iletişim için NATS veya Kafka kullanın
- API Gateway ile dış dünyaya açılın

### Veri Yönetimi

- Her servis kendi verisinden sorumlu olmalı
- Servisler arası veri duplikasyonu kabul edilebilir
- Eventual consistency modelini benimseyin

### Monitoring ve Observability

- Prometheus ile metrik toplama
- Jaeger/Zipkin ile distributed tracing
- Structured logging ve log aggregation

## Dağıtım ve DevOps

### Konteynerizasyon

- Çok aşamalı Docker build süreçleri kullanın
- Minimal imajlar oluşturun
- Güvenlik taraması yapın

### Kubernetes

- Helm chart'ları hazırlayın
- Resource limitleri belirleyin
- Horizontal Pod Autoscaler kullanın

### CI/CD Pipeline

- GitHub Actions veya GitLab CI kullanın
- Otomatik test ve dağıtım
- Semantic versiyonlama

## Güvenlik Düşünceleri

- JWT tabanlı kimlik doğrulama
- RBAC ile yetkilendirme
- TLS ile iletişim
- Hassas bilgilerin şifrelenmesi
- Input validasyonu ve sanitizasyonu

## Performans Hedefleri ve Ölçümler

- API yanıt süresi: p99 < 100ms
- Kural motoru değerlendirme: p99 < 10ms
- Kaynak kullanımı: < 200MB RAM / servis instance
- CPU kullanımı: < %30 (normal yükte)

Bu hedefleri düzenli olarak ölçün ve optimize edin.

## Mimariye İlişkin Özel Notlar

1. **Kural Motoru Tasarımı:**
   - Kural önceliklendirilmesi ve çakışma çözümü önemli
   - DSL tabanlı kural tanımı kullanıcı dostu olmalı
   - Kural derlemesi ve optimizasyonu düşünülmeli

2. **Exchange Entegrasyonu:**
   - Rate limiting ve throttling ele alınmalı
   - Bağlantı yönetimi ve hata durumlarına dikkat edilmeli
   - Delta senkronizasyon desteklenmeli

3. **API Tasarımı:**
   - REST ile hızlı başlayıp, GraphQL'e geçiş düşünülebilir
   - Versiyonlama stratejisi belirleyin
   - Dokümantasyon otomatize edilmeli

4. **Ölçeklenebilirlik:**
   - Stateless tasarım
   - Horizontal ölçeklendirme
   - Önbellek stratejisi
   - Yük dengeleme

Bu notlar, proje geliştikçe güncellenmelidir.