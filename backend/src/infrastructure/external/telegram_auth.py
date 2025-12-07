import hmac
import hashlib
import urllib.parse
import json
from typing import Optional, Dict

from src.application.ports.telegram_auth_service import TelegramAuthService


class TelegramAuthServiceImpl(TelegramAuthService):
    """Реализация сервиса верификации Telegram WebApp initData."""
    
    def verify_init_data(self, init_data: str, bot_token: str) -> bool:
        """Верифицировать initData от Telegram WebApp через HMAC SHA256."""
        try:
            # Парсим init_data
            parsed_data = urllib.parse.parse_qs(init_data)
            
            # Извлекаем hash
            received_hash = parsed_data.get('hash', [None])[0]
            if not received_hash:
                return False
            
            # Удаляем hash из данных и формируем строку для проверки
            data_check_string = []
            for key in sorted(parsed_data.keys()):
                if key != 'hash':
                    data_check_string.append(f"{key}={parsed_data[key][0]}")
            
            data_check_string = '\n'.join(data_check_string)
            
            # Вычисляем секретный ключ
            secret_key = hmac.new(
                "WebAppData".encode(),
                bot_token.encode(),
                hashlib.sha256
            ).digest()
            
            # Вычисляем hash
            calculated_hash = hmac.new(
                secret_key,
                data_check_string.encode(),
                hashlib.sha256
            ).hexdigest()
            
            # Сравниваем
            return calculated_hash == received_hash
        except Exception:
            return False
    
    def parse_init_data(self, init_data: str) -> Optional[Dict]:
        """Парсить initData и извлечь данные пользователя."""
        try:
            parsed = urllib.parse.parse_qs(init_data)
            user_data = {}
            
            if 'user' in parsed:
                user_data = json.loads(parsed['user'][0])
            
            return user_data
        except Exception:
            return None


# Функции для обратной совместимости (deprecated, использовать TelegramAuthServiceImpl)
def verify_telegram_init_data(init_data: str, bot_token: str) -> bool:
    """Верифицировать initData от Telegram WebApp через HMAC SHA256 (deprecated)."""
    service = TelegramAuthServiceImpl()
    return service.verify_init_data(init_data, bot_token)


def parse_init_data(init_data: str) -> Optional[Dict]:
    """Парсить initData и извлечь данные пользователя (deprecated)."""
    service = TelegramAuthServiceImpl()
    return service.parse_init_data(init_data)


def get_user_id_from_init_data(init_data: str) -> Optional[int]:
    """Извлечь user_id из initData."""
    service = TelegramAuthServiceImpl()
    user_data = service.parse_init_data(init_data)
    if user_data and 'id' in user_data:
        return user_data['id']
    return None

