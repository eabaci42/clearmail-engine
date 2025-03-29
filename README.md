# Clearmail Engine

Clearmail Engine, karmaşık e-posta kutularını düzenleyen, sınıflandıran ve otomatize eden akıllı bir e-posta yönetim çözümüdür. Exchange ile sorunsuz entegrasyon sağlar ve güçlü bir kural motoruyla gelen e-postaları otomatik olarak organize eder.

**Geliştirici:** Entegrex Yazılım Bilişim ve İletişim Teknolojileri

## Teknoloji Yol Haritası

- **v0.1.x:** Python tabanlı versiyon (Mevcut)
- **v0.2.x:** Go tabanlı ana API sunucusu ve servis katmanı 
- **v0.3.x:** Rust tabanlı performans kritik modüller
- **v1.0.0:** Mikroservis mimarisi, performans iyileştirmeleri ve tam özellik seti

## Özellikler

- 📧 Exchange mail sunucularıyla derin entegrasyon
- 🔍 Gelişmiş kural tabanlı e-posta filtreleme ve organizasyon
- 📁 Otomatik klasörleme ve etiketleme
- 🌐 RESTful API desteği
- ⏱️ Zamanlanmış görevler ve daemon modu
- 📊 Ayrıntılı loglama ve raporlama
- 🛠️ Özelleştirilebilir kural motoru

## Mimari

Clearmail Engine, aşağıdaki modüllerden oluşur:

- **API Sunucusu:** Go ile yazılmış, yüksek performanslı API
- **Exchange Servisi:** Exchange sunucuları ile iletişim kuran modül
- **Kural Motoru:** E-postaları işleyen ve kurallara göre organize eden Rust tabanlı sistem
- **Depolama Katmanı:** Yapılandırma, kurallar ve durumu yöneten servis

## Sistem Gereksinimleri

- Exchange Server 2016+ veya Office 365
- Ubuntu 22.04 LTS+ (veya diğer Linux dağıtımları)
- 2GB RAM minimum (4GB önerilen)
- 50MB disk alanı

## Kullanım

### API Sunucusunu Başlatma

```bash
./clearmail-engine --api
```

### Tek Seferlik İşleme

```bash
./clearmail-engine --process
```

### Daemon Modunda Çalıştırma

```bash
./clearmail-engine --daemon
```

### Özel Bir Klasörü İşleme

```bash
./clearmail-engine --process --folder "Inbox"
```

## Katkıda Bulunma

Projeye katkıda bulunmak için lütfen CONTRIBUTING.md dosyasını inceleyin.

## Lisans

Tüm hakları saklıdır. Entegrex Yazılım Bilişim ve İletişim Teknolojileri.