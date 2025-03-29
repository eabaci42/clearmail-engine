# Clearmail Engine - Python Versiyonu

Bu dizin, Clearmail Engine projesinin orijinal Python tabanlı versiyonunu içerir. Proje, Go ve Rust kullanılarak yeniden yazılmakta olup, bu dizin referans olarak korunmaktadır.

## Özellikler

- Exchange mail sunucularıyla entegre çalışma
- Kural tabanlı e-posta organizasyonu
- Otomatik klasörleme ve etiketleme
- RESTful API desteği
- Zamanlanmış görevler ve otomatik düzenleme
- Ayrıntılı loglama ve raporlama
- Özelleştirilebilir kural motoru

## Sistem Gereksinimleri

- Python 3.9+
- Exchange Server 2016+ veya Office 365
- Ubuntu 22.04 LTS+ (veya diğer Linux dağıtımları)
- 2GB RAM minimum (4GB önerilen)
- 50MB disk alanı

## Kurulum

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/entegrex/clearmail-engine.git
cd clearmail-engine/python-version
```

### 2. Sanal Ortam Oluşturun

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# veya
venv\Scripts\activate     # Windows
```

### 3. Bağımlılıkları Yükleyin

```bash
cd backend
pip install -r requirements.txt
```

### 4. Yapılandırma

1. `.env.example` dosyasını `.env` olarak kopyalayın:

```bash
cp .env.example .env
```

2. `.env` dosyasını düzenleyerek Exchange kimlik bilgilerinizi ekleyin
3. Gerekirse `config.yaml` dosyasını düzenleyin

## Kullanım

### API Sunucusunu Başlatma

```bash
python main.py --api
```

API sunucusu varsayılan olarak `http://0.0.0.0:8000` adresinde çalışacaktır.

### Tek Seferlik İşleme

```bash
python main.py --process
```

### Daemon Modunda Çalıştırma

```bash
python main.py --daemon
```

### Özel Bir Klasörü İşleme

```bash
python main.py --process --folder "Inbox"
```

## API Endpointleri

- `GET /`: API bilgisi
- `GET /status`: Sistem durumu
- `GET /folders`: Tüm klasörleri listele
- `GET /messages/{folder_name}`: Belirli bir klasördeki mesajları listele
- `POST /process/inbox`: Gelen kutusunu işle
- `POST /process/folder/{folder_name}`: Belirli bir klasörü işle
- `POST /process/all`: Tüm izlenen klasörleri işle

Ayrıntılı API dokümantasyonu için: `http://sunucu:port/docs`