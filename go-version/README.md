# Clearmail Engine - Go Versiyonu

Bu dizin, Clearmail Engine'in Go tabanlı uygulamasını içerir. Bu versiyon, Python tabanlı öncülünden daha yüksek performans ve ölçeklenebilirlik sunmak üzere geliştirilmektedir.

## Mimari

Go versiyonu, aşağıdaki temel bileşenlerden oluşur:

- **API Sunucusu:** HTTP tabanlı REST API
- **Exchange Servisi:** Exchange sunucusu ile iletişim kurar
- **Yapılandırma Yönetimi:** Sistem yapılandırmasını yönetir
- **Rule Engine FFI:** Rust tabanlı kural motoru ile FFI arayüzü

## Dizin Yapısı

```
go-version/
├── cmd/
│   └── clearmail/              # Ana uygulama giriş noktası
├── api/
│   ├── handlers/               # API endpoint handler'ları
│   ├── middleware/             # API middleware'leri
│   └── server/                 # API sunucu yapılandırması
├── internal/
│   ├── config/                 # Yapılandırma yönetimi
│   ├── exchange/               # Exchange entegrasyonu
│   ├── models/                 # Veri modelleri
│   └── services/               # İş mantığı servisleri
├── pkg/
│   ├── logger/                 # Loglama yardımcıları
│   └── utils/                  # Ortak yardımcı fonksiyonlar
├── tests/                      # Entegrasyon testleri
└── scripts/                    # Yardımcı scriptler
```

## Kullanım

### Gereksinimler

- Go 1.18 veya üzeri
- Exchange Server 2016+ veya Office 365

### Derleme

```bash
cd go-version
go build -o clearmail-engine ./cmd/clearmail
```

### Çalıştırma

```bash
# API modunda çalıştırma
./clearmail-engine --api

# Tek seferlik işleme
./clearmail-engine --process

# Daemon modunda çalıştırma
./clearmail-engine --daemon
```

## Geliştirme

### Kod Formatı

```bash
go fmt ./...
```

### Testleri Çalıştırma

```bash
go test ./...
```

### Bağımlılıkları Güncelleme

```bash
go mod tidy
```

## API Dokümantasyonu

API dokümantasyonu, Swagger UI aracılığıyla `/swagger/index.html` adresinde sunulmaktadır.

## Katkıda Bulunma

Katkıda bulunmak için ana proje dizinindeki CONTRIBUTING.md dosyasını inceleyin.

## İleriki Planlar

- Microsoft Graph API tam entegrasyonu
- OAuth2 kimlik doğrulama
- WebSocket destek
- gRPC arayüzü