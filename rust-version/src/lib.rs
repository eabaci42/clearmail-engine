//! Clearmail Engine Kural Motoru
//!
//! Bu kütüphane, e-postaları işleyen ve kurallara göre sınıflandıran
//! yüksek performanslı bir kural motorudur.

mod engine;
mod models;
mod matchers;
mod actions;
pub mod ffi;

use std::sync::Arc;
use std::collections::HashMap;

pub use engine::RuleEngine;
pub use models::{Rule, Condition, Action, Message, MatchResult};

/// Kütüphane sonucu tipi
pub type Result<T> = std::result::Result<T, Error>;

/// Kütüphane hata türleri
#[derive(Debug, thiserror::Error)]
pub enum Error {
    #[error("Kural hatası: {0}")]
    RuleError(String),
    
    #[error("Eşleştirme hatası: {0}")]
    MatchError(String),
    
    #[error("Eylem hatası: {0}")]
    ActionError(String),
    
    #[error("Serileştirme hatası: {0}")]
    SerializationError(String),
    
    #[error("FFI hatası: {0}")]
    FFIError(String),
    
    #[error("Bilinmeyen hata: {0}")]
    Unknown(String),
}

/// Kural motoru oluştur
///
/// # Örnek
///
/// ```
/// use clearmail_rule_engine::{create_rule_engine, Rule, Condition, Action};
///
/// let engine = create_rule_engine();
/// ```
pub fn create_rule_engine() -> RuleEngine {
    RuleEngine::new()
}

/// Bir e-postayı işle ve eşleşen kuralları uygula
///
/// # Parametreler
///
/// * `message` - İşlenecek e-posta
/// * `rules` - Uygulanacak kurallar
///
/// # Dönüş
///
/// Uygulanan eylemlerin listesi
///
/// # Örnek
///
/// ```
/// use clearmail_rule_engine::{process_message, Rule, Message};
///
/// let message = Message::new();
/// let rules = vec![Rule::new("test")];
/// let results = process_message(&message, &rules);
/// ```
pub fn process_message(message: &models::Message, rules: &[models::Rule]) -> Vec<models::MatchResult> {
    let engine = RuleEngine::new();
    
    for rule in rules {
        engine.add_rule(rule.clone());
    }
    
    engine.process_message(message)
}

/// Kütüphane sürümünü al
///
/// # Dönüş
///
/// Kütüphane sürümü
pub fn version() -> &'static str {
    env!("CARGO_PKG_VERSION")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_version() {
        assert!(!version().is_empty());
    }

    #[test]
    fn test_create_engine() {
        let engine = create_rule_engine();
        assert_eq!(engine.rules_count(), 0);
    }
}