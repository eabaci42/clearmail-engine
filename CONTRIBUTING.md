# Katkıda Bulunma Rehberi

Clearmail Engine projesine katkıda bulunmak istediğiniz için teşekkür ederiz! Bu belge, projeye nasıl katkıda bulunabileceğinizi açıklar.

## Başlamadan Önce

Lütfen aşağıdaki adımları izleyin:

1. Projeyi forklayın
2. Lokal kopyanızı oluşturun: `git clone https://github.com/KULLANICI_ADINIZ/clearmail-engine.git`
3. Ana repoyu upstream olarak ekleyin: `git remote add upstream https://github.com/entegrex/clearmail-engine.git`
4. Bir özellik dalı oluşturun: `git checkout -b feature/yeni-ozellik`

## Geliştirme Ortamı

### Go Modülleri

```bash
cd clearmail-engine
go mod download
```

### Rust Bileşenleri

```bash
cd rule-engine
cargo build
```

## Geliştirme İş Akışı

1. Kodunuzu yazın ve değişikliklerinizi yapın
2. Testlerinizi ekleyin
3. Kodunuzu formatlayın: `make fmt`
4. Linting kontrollerini yapın: `make lint`
5. Testleri çalıştırın: `make test`
6. Değişikliklerinizi commit edin ve dalınıza push edin
7. Ana repoya bir Pull Request açın

## Commit Mesajları

Lütfen commit mesajlarınızda aşağıdaki formatı kullanın:

```
<type>(<scope>): <subject>

<body>
```

Örnekler:

- `feat(api): Klasör oluşturma endpoint'i eklendi`
- `fix(rule-engine): Kural eşleştirme hatası düzeltildi`
- `docs(readme): Kurulum talimatları güncellendi`

## Değişiklikler ve Test

- Tüm değişiklikler için testler ekleyin
- Yeni özellikler için dokümantasyon güncelleyin
- Kapsamlı değişiklikler için ayrıca CHANGELOG.md'yi de güncelleyin

## Kod Standartları

### Go Kodu

- [Go Effective Go](https://golang.org/doc/effective_go.html) kurallarını takip edin
- Kodunuzu `gofmt` ile formatlayın
- Kodunuzu `golangci-lint` ile kontrol edin

### Rust Kodu

- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/) kurallarını takip edin
- Kodunuzu `cargo fmt` ile formatlayın
- Kodunuzu `cargo clippy` ile kontrol edin

## Pull Request Süreci

1. PR açıldıktan sonra CI/CD pipeline otomatik olarak çalışacaktır
2. En az bir code review gereklidir
3. Tüm testler geçmelidir
4. Dokümantasyon ve CHANGELOG.md güncellenmelidir

## Yardım ve İletişim

Sorularınız için GitHub Issues kullanabilirsiniz.