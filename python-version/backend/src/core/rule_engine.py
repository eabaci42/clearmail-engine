"""
Clearmail Engine - Kural Motoru

Bu modül, e-posta kurallarını tanımlamak ve uygulamak için kullanılır.
"""

import re
import logging
from typing import Dict, List, Any, Callable, Optional, Pattern
from email.message import Message

from ..utils.logging_utils import get_logger

logger = get_logger(__name__)


class Rule:
    """E-posta kuralı sınıfı. Her kural, bir veya daha fazla koşul ve eylemden oluşur."""

    def __init__(self, name: str, description: str = ""):
        """
        Kural başlatma.

        Args:
            name: Kural adı
            description: Kural açıklaması
        """
        self.name = name
        self.description = description
        self.conditions = []
        self.actions = []
        self.is_active = True
        self.priority = 0

    def add_condition(self, field: str, operator: str, value: str, case_sensitive: bool = False):
        """
        Kurala bir koşul ekle.

        Args:
            field: Kontrol edilecek e-posta alanı (subject, from, to, body, vb.)
            operator: İşleç (contains, equals, matches, vb.)
            value: Karşılaştırılacak değer
            case_sensitive: Büyük/küçük harf duyarlı mı?
        """
        self.conditions.append({
            "field": field,
            "operator": operator,
            "value": value,
            "case_sensitive": case_sensitive
        })
        return self

    def add_action(self, action_type: str, params: Dict[str, Any] = None):
        """
        Kurala bir eylem ekle.

        Args:
            action_type: Eylem türü (move, copy, delete, tag, vb.)
            params: Eylem parametreleri
        """
        if params is None:
            params = {}
        self.actions.append({
            "type": action_type,
            "params": params
        })
        return self

    def match(self, message: Dict[str, Any]) -> bool:
        """
        Mesajın bu kuralın koşullarına uyup uymadığını kontrol et.

        Args:
            message: Kontrol edilecek e-posta mesajı

        Returns:
            True eğer mesaj kurala uyuyorsa, False değilse
        """
        if not self.is_active or not self.conditions:
            return False

        for condition in self.conditions:
            field = condition["field"]
            operator = condition["operator"]
            expected_value = condition["value"]
            case_sensitive = condition["case_sensitive"]

            if field not in message:
                logger.debug(f"Field '{field}' not found in message")
                return False

            actual_value = message[field]
            if actual_value is None:
                logger.debug(f"Field '{field}' is None in message")
                return False

            if not isinstance(actual_value, str):
                actual_value = str(actual_value)

            if not self._check_condition(actual_value, operator, expected_value, case_sensitive):
                return False

        return True

    def _check_condition(self, actual: str, operator: str, expected: str, case_sensitive: bool) -> bool:
        """Bir koşulun doğru olup olmadığını kontrol et."""
        if not case_sensitive:
            actual = actual.lower()
            expected = expected.lower()

        if operator == "contains":
            return expected in actual
        elif operator == "not_contains":
            return expected not in actual
        elif operator == "equals":
            return actual == expected
        elif operator == "not_equals":
            return actual != expected
        elif operator == "starts_with":
            return actual.startswith(expected)
        elif operator == "ends_with":
            return actual.endswith(expected)
        elif operator == "matches":
            flags = 0 if case_sensitive else re.IGNORECASE
            pattern = re.compile(expected, flags)
            return bool(pattern.search(actual))
        elif operator == "is_empty":
            return not actual
        elif operator == "is_not_empty":
            return bool(actual)
        else:
            logger.warning(f"Unknown operator: {operator}")
            return False

    def __repr__(self):
        return f"Rule(name='{self.name}', conditions={len(self.conditions)}, actions={len(self.actions)})"


class RuleEngine:
    """Kural motoru, kuralları tanımlamayı ve uygulamayı sağlar."""

    def __init__(self):
        self.rules = []
        self.action_handlers = {}
        self._register_default_action_handlers()

    def add_rule(self, rule: Rule) -> 'RuleEngine':
        """Kurala bir kural ekle."""
        self.rules.append(rule)
        # Önceliğe göre kuralları sırala
        self.rules.sort(key=lambda r: r.priority, reverse=True)
        return self

    def register_action_handler(self, action_type: str, handler: Callable) -> 'RuleEngine':
        """Yeni bir eylem işleyicisi kaydet."""
        self.action_handlers[action_type] = handler
        return self

    def process_message(self, message: Dict[str, Any], context: Dict[str, Any] = None) -> List[Dict]:
        """
        Bir mesajı tüm kurallara göre işle.

        Args:
            message: İşlenecek e-posta mesajı
            context: İşleme bağlamı (opsiyonel)

        Returns:
            Uygulanan eylemlerin listesi
        """
        if context is None:
            context = {}

        applied_actions = []
        
        for rule in self.rules:
            if not rule.is_active:
                continue
                
            try:
                if rule.match(message):
                    logger.info(f"Rule '{rule.name}' matched message with subject: {message.get('subject', 'No Subject')}")
                    
                    for action in rule.actions:
                        action_type = action["type"]
                        params = action["params"]
                        
                        if action_type in self.action_handlers:
                            handler = self.action_handlers[action_type]
                            result = handler(message, params, context)
                            
                            applied_actions.append({
                                "rule": rule.name,
                                "action": action_type,
                                "result": result
                            })
                            
                            logger.info(f"Action '{action_type}' applied from rule '{rule.name}'")
                        else:
                            logger.warning(f"No handler for action type '{action_type}'")
            except Exception as e:
                logger.error(f"Error processing rule '{rule.name}': {e}")
                
        return applied_actions

    def _register_default_action_handlers(self):
        """Varsayılan eylem işleyicilerini kaydet."""
        self.register_action_handler("move", self._action_move)
        self.register_action_handler("copy", self._action_copy)
        self.register_action_handler("delete", self._action_delete)
        self.register_action_handler("mark_as_read", self._action_mark_as_read)
        self.register_action_handler("mark_as_unread", self._action_mark_as_unread)
        self.register_action_handler("flag", self._action_flag)
        self.register_action_handler("tag", self._action_tag)
        self.register_action_handler("forward", self._action_forward)

    def _action_move(self, message, params, context):
        """Mesajı başka bir klasöre taşı."""
        target_folder = params.get("folder")
        if not target_folder:
            logger.error("Move action requires 'folder' parameter")
            return False
            
        logger.info(f"Moving message to folder: {target_folder}")
        # Gerçek taşıma işlemi Exchange service tarafından yapılacak
        return True

    def _action_copy(self, message, params, context):
        """Mesajı başka bir klasöre kopyala."""
        target_folder = params.get("folder")
        if not target_folder:
            logger.error("Copy action requires 'folder' parameter")
            return False
            
        logger.info(f"Copying message to folder: {target_folder}")
        # Gerçek kopyalama işlemi Exchange service tarafından yapılacak
        return True

    def _action_delete(self, message, params, context):
        """Mesajı sil."""
        permanent = params.get("permanent", False)
        logger.info(f"Deleting message (permanent={permanent})")
        # Gerçek silme işlemi Exchange service tarafından yapılacak
        return True

    def _action_mark_as_read(self, message, params, context):
        """Mesajı okundu olarak işaretle."""
        logger.info("Marking message as read")
        # Gerçek işaretleme işlemi Exchange service tarafından yapılacak
        return True

    def _action_mark_as_unread(self, message, params, context):
        """Mesajı okunmadı olarak işaretle."""
        logger.info("Marking message as unread")
        # Gerçek işaretleme işlemi Exchange service tarafından yapılacak
        return True

    def _action_flag(self, message, params, context):
        """Mesajı bayrakla."""
        flag_type = params.get("flag_type", "red")
        logger.info(f"Flagging message with {flag_type}")
        # Gerçek bayraklama işlemi Exchange service tarafından yapılacak
        return True

    def _action_tag(self, message, params, context):
        """Mesaja etiket ekle."""
        tags = params.get("tags", [])
        if not tags:
            logger.error("Tag action requires 'tags' parameter")
            return False
            
        logger.info(f"Tagging message with: {tags}")
        # Gerçek etiketleme işlemi Exchange service tarafından yapılacak
        return True

    def _action_forward(self, message, params, context):
        """Mesajı başka bir adrese ilet."""
        recipient = params.get("recipient")
        if not recipient:
            logger.error("Forward action requires 'recipient' parameter")
            return False
            
        logger.info(f"Forwarding message to: {recipient}")
        # Gerçek iletme işlemi Exchange service tarafından yapılacak
        return True