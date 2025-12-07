import sys
import pytest
from unittest.mock import Mock, patch, MagicMock

# Мокируем PIL и qrcode перед импортом
sys.modules['PIL'] = MagicMock()
sys.modules['PIL.Image'] = MagicMock()
sys.modules['PIL.ImageDraw'] = MagicMock()
sys.modules['PIL.ImageFont'] = MagicMock()
sys.modules['PIL.ImageEnhance'] = MagicMock()
sys.modules['qrcode'] = MagicMock()

from src.infrastructure.image.card_generator import CardGeneratorImpl


class TestCardGeneratorImpl:
    """Тесты для CardGeneratorImpl."""

    def test_generate_card_handles_font_load_error_with_specific_exception(self):
        """Тест обработки ошибки загрузки шрифта с конкретным типом исключения."""
        # Arrange
        generator = CardGeneratorImpl()
        
        # Act & Assert
        with patch('src.infrastructure.image.card_generator.ImageFont.truetype') as mock_truetype, \
             patch('src.infrastructure.image.card_generator.ImageFont.load_default') as mock_default, \
             patch('src.infrastructure.image.card_generator.logger') as mock_logger:
            
            # Мокируем ошибку OSError при загрузке шрифта
            mock_truetype.side_effect = OSError("Font file not found")
            
            # Мокируем остальные необходимые компоненты
            mock_font = MagicMock()
            mock_font.getbbox.return_value = (0, 0, 100, 20)  # left, top, right, bottom
            
            with patch('src.infrastructure.image.card_generator.Image.new'), \
                 patch('src.infrastructure.image.card_generator.ImageDraw.Draw'), \
                 patch('src.infrastructure.image.card_generator.io.BytesIO'), \
                 patch.object(mock_default, 'return_value', mock_font):
                
                result = generator.generate_card(
                    full_name="Иван Иванов",
                    company="ООО Тест",
                    position="Разработчик",
                    greeting_text="Поздравляем!",
                )
                
                # Проверяем, что использован fallback шрифт
                assert mock_default.call_count == 4  # 4 шрифта
                
                # Проверяем, что ошибка залогирована
                mock_logger.warning.assert_called_once()
                call_args = mock_logger.warning.call_args
                assert "Failed to load custom font" in call_args[0][0]
                assert 'error' in call_args[1]['extra']
                assert 'font_path' in call_args[1]['extra']

    def test_generate_card_handles_ioerror_with_specific_exception(self):
        """Тест обработки IOError при загрузке шрифта."""
        # Arrange
        generator = CardGeneratorImpl()
        
        # Act & Assert
        with patch('src.infrastructure.image.card_generator.ImageFont.truetype') as mock_truetype, \
             patch('src.infrastructure.image.card_generator.ImageFont.load_default') as mock_default, \
             patch('src.infrastructure.image.card_generator.logger') as mock_logger:
            
            # Мокируем ошибку IOError при загрузке шрифта
            mock_truetype.side_effect = IOError("Permission denied")
            
            mock_font = MagicMock()
            mock_font.getbbox.return_value = (0, 0, 100, 20)  # left, top, right, bottom
            
            with patch('src.infrastructure.image.card_generator.Image.new'), \
                 patch('src.infrastructure.image.card_generator.ImageDraw.Draw'), \
                 patch('src.infrastructure.image.card_generator.io.BytesIO'), \
                 patch.object(mock_default, 'return_value', mock_font):
                
                result = generator.generate_card(
                    full_name="Иван Иванов",
                    company="ООО Тест",
                    position="Разработчик",
                    greeting_text="Поздравляем!",
                )
                
                # Проверяем, что использован fallback шрифт
                assert mock_default.call_count == 4
                
                # Проверяем логирование
                mock_logger.warning.assert_called_once()

