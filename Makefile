# Clearmail Engine Makefile

.PHONY: all test build run clean deps

# Değişkenler
BINARY_NAME=clearmail-engine
GO_FILES=$(shell find . -name "*.go" -type f)
RUST_FILES=$(shell find rule-engine/ -name "*.rs" -type f)
COVERAGE_FILE=coverage.out

# Ana hedefler
all: deps build test

# Bağımlılıklar
deps:
	@echo "Bağımlılıklar yükleniyor..."
	@go mod download
	@cd rule-engine && cargo fetch

# Derleme
build: build-go build-rust

build-go:
	@echo "Go kodları derleniyor..."
	@go build -o $(BINARY_NAME) ./cmd/clearmail

build-rust:
	@echo "Rust rule-engine derleniyor..."
	@cd rule-engine && cargo build --release

# Çalıştırma
run:
	@echo "Clearmail Engine başlatılıyor..."
	@./$(BINARY_NAME) --api

# Testler
test: test-go test-rust

test-go:
	@echo "Go testleri çalıştırılıyor..."
	@go test -v ./...

test-rust:
	@echo "Rust testleri çalıştırılıyor..."
	@cd rule-engine && cargo test

# Kod kapsamı
coverage:
	@echo "Kod kapsamı raporu oluşturuluyor..."
	@go test -coverprofile=$(COVERAGE_FILE) ./...
	@go tool cover -html=$(COVERAGE_FILE)

# Linter
lint: lint-go lint-rust

lint-go:
	@echo "Go kodu linting..."
	@golangci-lint run

lint-rust:
	@echo "Rust kodu linting..."
	@cd rule-engine && cargo clippy

# Format
fmt: fmt-go fmt-rust

fmt-go:
	@echo "Go kodu formatlanıyor..."
	@gofmt -s -w $(GO_FILES)

fmt-rust:
	@echo "Rust kodu formatlanıyor..."
	@cd rule-engine && cargo fmt

# Temizleme
clean:
	@echo "Proje temizleniyor..."
	@rm -f $(BINARY_NAME)
	@rm -f $(COVERAGE_FILE)
	@cd rule-engine && cargo clean