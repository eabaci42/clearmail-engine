# Clearmail Engine - Rust Tabanlı Kural Motoru

Bu dizin, Clearmail Engine'in yüksek performanslı Rust tabanlı kural motorunu içerir. Bu bileşen, e-postaları işlemek ve kurallara göre organize etmek için kullanılır.

## Mimari

Rust kural motoru, aşağıdaki temel bileşenlerden oluşur:

- **Rule Engine Core:** Kural değerlendirme motoru
- **Pattern Matchers:** E-posta içeriğini eşleştirmek için algoritmalar
- **Actions:** Kurallara uygun e-postalar için uygulanacak eylemler
- **FFI Layer:** Go ile iletişim için Foreign Function Interface

## Dizin Yapısı

```
rust-version/
├── src/
│   ├── lib.rs                  # Kütüphane giriş noktası
│   ├── engine/                 # Kural motoru çekirdeği
│   ├── matchers/               # Eşleştirme algoritmaları
│   ├── actions/                # Eylem uygulamaları
│   ├── models/                 # Veri modelleri
│   └── ffi/                    # Go entegrasyonu için FFI
├── benches/                    # Benchmark testleri
├── tests/                      # Entegrasyon testleri
└── examples/                   # Kullanım örnekleri
```

## Temel Özellikler

- **Yüksek Performans:** Milisaniyeler içinde kural değerlendirme
- **Paralel İşleme:** Çoklu thread ile paralel kural değerlendirme
- **Bellek Verimliliği:** Düşük bellek ayak izi
- **Esnek Kural Dili:** Güçlü bir kural tanımlama dili
- **Pattern Matching:** Regex, glob, substring ve başka gelişmiş eşleştirme mekanizmaları

## Kullanım

### Gereksinimler

- Rust 1.65 veya üzeri
- Cargo 1.65 veya üzeri

### Derleme

```bash
cd rust-version
cargo build --release
```

### Testleri Çalıştırma

```bash
cargo test
```

### Benchmark

```bash
cargo bench
```

## FFI Entegrasyonu

Rust kural motoru, Go koduna bir C ABI uyumlu arayüz sağlar. Bu arayüz, aşağıdaki temel fonksiyonları içerir:

- `rule_engine_create`: Yeni bir kural motoru oluşturur
- `rule_engine_add_rule`: Motora yeni bir kural ekler
- `rule_engine_process_message`: Bir e-postayı kurallara göre işler
- `rule_engine_destroy`: Kural motorunu temizler

## Performans

Rust kural motoru, aşağıdaki performans hedeflerini karşılamak üzere tasarlanmıştır:

- Kural başına değerlendirme süresi: <1ms
- 1000 kurallık bir sette toplam değerlendirme: <10ms
- E-posta başına bellek kullanımı: <1MB
- Maksimum paralel işleme

## Katkıda Bulunma

Katkıda bulunmak için ana proje dizinindeki CONTRIBUTING.md dosyasını inceleyin.

## İleriki Planlar

- SIMD optimizasyonları
- Jit-compiled regex matching
- Daha karmaşık koşul ve eylem türleri
- Kullanıcı tanımlı fonksiyonlar
- Yapay zeka destekli kural önerileri