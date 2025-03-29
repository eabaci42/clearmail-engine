# Clearmail Engine - Mimari Dökümantasyonu

## Genel Bakış

Clearmail Engine, modüler bir yapıya sahiptir ve mikroservis mimarisine geçiş yapabilecek şekilde tasarlanmıştır. Sistem, aşağıdaki ana bileşenlerden oluşur:

## Bileşenler

### 1. API Sunucusu (Go)

RESTful API sunucusu, dış dünya ile iletişimi sağlar. Aşağıdaki özelliklere sahiptir:

- Yüksek performanslı istek işleme
- Kimlik doğrulama ve yetkilendirme
- Rate limiting
- İstek loglama
- Swagger dokümantasyonu

### 2. Exchange Servisi (Go)

Exchange sunucuları ile iletişim kuran servis:

- SOAP/REST API üzerinden Exchange bağlantısı
- Mesaj ve klasör yönetimi
- Önbellek mekanizması
- Bağlantı havuzu

### 3. Kural Motoru (Rust)

E-postaları kurallara göre işleyen ve organize eden yüksek performanslı motor:

- Kural değerlendirme ve eşleştirme
- Eylem uygulama
- Hızlı desen eşleştirme
- Paralel işleme

### 4. Yapılandırma Servisi (Go)

Sistem yapılandırmasını yöneten servis:

- Yapılandırma okuma/yazma
- Kural yönetimi
- Dinamik yapılandırma güncellemeleri

### 5. Loglama ve İzleme (Go)

Sistem loglarını ve performans metriklerini yöneten bileşen:

- Yapılandırılabilir log seviyeleri
- Rotasyonlu log dosyaları
- Prometheus metrikleri
- Grafana entegrasyonu (opsiyonel)

## Veri Akışı

1. Kullanıcı API veya komut satırı aracılığıyla bir işlem başlatır
2. API Sunucusu isteği alır ve doğrular
3. İlgili servis (Exchange veya Kural Motoru) çağrılır
4. Exchange Servisi e-posta sunucusundan verileri alır
5. Kural Motoru e-postaları işler ve kurallara göre organize eder
6. Sonuçlar kullanıcıya döndürülür

## Ölçeklenebilirlik

Clearmail Engine, yatay ve dikey ölçeklenebilirlik için tasarlanmıştır:

- Bileşenler bağımsız olarak ölçeklendirilebilir
- Mikroservis mimarisi için hazır
- Stateless tasarım

## Güvenlik

- Tüm API istekleri için kimlik doğrulama
- HTTPS zorunluluğu
- Hassas bilgiler için şifreleme
- Sınırlı izinler ve rol tabanlı erişim