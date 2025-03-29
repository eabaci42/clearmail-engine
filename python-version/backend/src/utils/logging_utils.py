"""
Clearmail Engine - Loglama Yardımcı Fonksiyonları

Bu modül, Clearmail Engine için loglama yapılandırmasını ve fonksiyonlarını içerir.
"""

import os
import logging
import logging.handlers
from typing import Dict, Any, Optional


def setup_logging(config: Dict[str, Any]) -> None:
    """
    Loglama sistemini yapılandır.

    Args:
        config: Loglama yapılandırma ayarları
    """
    log_level = getattr(logging, config.get("level", "INFO").upper())
    log_format = config.get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_date_format = config.get("date_format", "%Y-%m-%d %H:%M:%S")
    
    # Ana handler'ı yapılandır
    handlers = []
    
    # Dosyaya loglama
    if config.get("file", {}).get("enabled", True):
        log_dir = config.get("file", {}).get("directory", "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        log_file = os.path.join(log_dir, config.get("file", {}).get("filename", "clearmail.log"))
        max_bytes = config.get("file", {}).get("max_bytes", 10485760)  # 10MB
        backup_count = config.get("file", {}).get("backup_count", 5)
        
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count
        )
        file_handler.setFormatter(logging.Formatter(log_format, log_date_format))
        handlers.append(file_handler)
    
    # Konsola loglama
    if config.get("console", {}).get("enabled", True):
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter(log_format, log_date_format))
        handlers.append(console_handler)
    
    # Kök logger'ı yapılandır
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    
    # Eski handler'ları temizle
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Yeni handler'ları ekle
    for handler in handlers:
        root_logger.addHandler(handler)
    
    # Üçüncü taraf kütüphanelerin log seviyelerini ayarla
    if "third_party" in config:
        for module, level in config["third_party"].items():
            logging.getLogger(module).setLevel(getattr(logging, level.upper()))


def get_logger(name: str) -> logging.Logger:
    """
    Belirtilen ad için bir logger örneği döndür.

    Args:
        name: Logger adı (genellikle __name__ kullanılır)

    Returns:
        Logger örneği
    """
    return logging.getLogger(name)


class LoggerAdapter(logging.LoggerAdapter):
    """
    Ekstra bağlam bilgisi eklemek için LoggerAdapter sınıfı.
    """
    
    def process(self, msg, kwargs):
        if 'extra' not in kwargs:
            kwargs['extra'] = self.extra
        return msg, kwargs


def get_context_logger(name: str, context: Dict[str, Any]) -> LoggerAdapter:
    """
    Bağlam bilgisi içeren bir logger döndür.

    Args:
        name: Logger adı
        context: Log mesajlarına eklenecek bağlam bilgisi

    Returns:
        LoggerAdapter örneği
    """
    logger = get_logger(name)
    return LoggerAdapter(logger, context)