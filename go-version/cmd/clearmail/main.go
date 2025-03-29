package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"os/signal"
	"syscall"
)

// Version, derleme zamanında -ldflags ile belirtilebilir
var Version = "0.2.0-dev"

func main() {
	// Komut satırı bayrakları
	apiMode := flag.Bool("api", false, "API sunucusu olarak çalıştır")
	daemonMode := flag.Bool("daemon", false, "Daemon olarak çalıştır")
	processMode := flag.Bool("process", false, "Tek seferlik işleme modu")
	configFile := flag.String("config", "", "Yapılandırma dosyası yolu (varsayılan: config.yaml)")
	folder := flag.String("folder", "", "İşlenecek özel klasör (sadece process modu ile kullanılır)")
	showVersion := flag.Bool("version", false, "Sürüm bilgisini göster")

	flag.Parse()

	// Sürüm bilgisini göster
	if *showVersion {
		fmt.Printf("Clearmail Engine v%s\n", Version)
		return
	}

	// Varsayılan yapılandırma dosyası
	if *configFile == "" {
		*configFile = "config.yaml"
	}

	// En az bir modun seçilmiş olduğunu kontrol et
	if !*apiMode && !*daemonMode && !*processMode {
		log.Fatal("En az bir çalışma modu belirtilmelidir: --api, --daemon veya --process")
	}

	// Process modu ve özel klasör işleme
	if *processMode && *folder != "" {
		fmt.Printf("Özel klasör işleniyor: %s\n", *folder)
		// TODO: Özel klasör işleme fonksiyonunu çağır
		return
	}

	// Process modu
	if *processMode {
		fmt.Println("Tek seferlik işleme modu başlatılıyor...")
		// TODO: Tek seferlik işleme fonksiyonunu çağır
		return
	}

	// API modu
	if *apiMode {
		fmt.Println("API sunucusu başlatılıyor...")
		// TODO: API sunucusunu başlat
		startAPIServer()
		waitForSignal()
		return
	}

	// Daemon modu
	if *daemonMode {
		fmt.Println("Daemon modu başlatılıyor...")
		// TODO: Daemon modunu başlat
		startDaemon()
		waitForSignal()
		return
	}
}

// startAPIServer API sunucusunu başlatır
func startAPIServer() {
	// TODO: Gerçek API sunucu uygulaması
	fmt.Println("API sunucusu dinlemeye başladı: http://0.0.0.0:8000")
}

// startDaemon daemon modunu başlatır
func startDaemon() {
	// TODO: Gerçek daemon uygulaması
	fmt.Println("Daemon modu başladı, e-postalar düzenli olarak işlenecek")
}

// waitForSignal programın sonlandırılmasını bekler
func waitForSignal() {
	sigChan := make(chan os.Signal, 1)
	signal.Notify(sigChan, syscall.SIGINT, syscall.SIGTERM)
	sig := <-sigChan
	fmt.Printf("\nSinyal alındı (%s), uygulama kapatılıyor...\n", sig)
}