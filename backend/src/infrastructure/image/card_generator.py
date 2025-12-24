import io
import logging
import os
import re

import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from src.application.ports.card_generator import CardGeneratorPort
from src.domain.exceptions.validation import InvalidGreetingTextError, TextTooLongError

logger = logging.getLogger(__name__)


class CardGeneratorImpl(CardGeneratorPort):
    def __init__(self):
        self.width = 1200
        self.height = 800
        
        # Цвета
        self.text_color = (30, 30, 30)  # Тёмно-серый для лучшей читаемости
        self.accent_color = (70, 130, 180)  # Синий для заголовков
        self.subtitle_color = (100, 100, 100)  # Серый для подзаголовков
        
        # Конфигурация шрифтов
        self.font_path = os.getenv("CARD_FONT_PATH", "arial.ttf")
        self.title_font_size = int(os.getenv("CARD_TITLE_FONT_SIZE", "48"))
        self.name_font_size = int(os.getenv("CARD_NAME_FONT_SIZE", "36"))
        self.text_font_size = int(os.getenv("CARD_TEXT_FONT_SIZE", "24"))
        self.small_font_size = int(os.getenv("CARD_SMALL_FONT_SIZE", "20"))
        
        # Лимиты длины текста
        self.max_text_length = 1200
        self.min_font_size = 18  # Минимальный размер шрифта

    def _load_font(self, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        """Загрузить шрифт с fallback на системный."""
        try:
            if os.path.exists(self.font_path):
                return ImageFont.truetype(self.font_path, size)
            else:
                # Пробуем стандартные шрифты
                for fallback_path in [
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                    "/System/Library/Fonts/Helvetica.ttc",
                    "C:/Windows/Fonts/arial.ttf",
                ]:
                    if os.path.exists(fallback_path):
                        return ImageFont.truetype(fallback_path, size)
        except Exception as e:
            logger.warning(f"Failed to load font {self.font_path}: {e}")
        
        # Fallback на системный шрифт
        return ImageFont.load_default()

    def _create_gradient_background(self) -> Image.Image:
        """Создать градиентный фон для открытки с рамкой."""
        img = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # Мягкий градиент от светло-голубого к кремовому
        for y in range(self.height):
            # Градиент от (245, 250, 255) к (255, 252, 245)
            ratio = y / self.height
            r = int(245 + (255 - 245) * ratio)
            g = int(250 + (252 - 250) * ratio)
            b = int(255 + (245 - 255) * ratio)
            draw.line([(0, y), (self.width, y)], fill=(r, g, b))
        
        # Добавляем тонкую рамку для структуры
        border_width = 3
        border_color = (220, 230, 240)  # Светло-серый
        
        # Верхняя и нижняя границы
        draw.rectangle(
            [(0, 0), (self.width, border_width)],
            fill=border_color
        )
        draw.rectangle(
            [(0, self.height - border_width), (self.width, self.height)],
            fill=border_color
        )
        
        # Левая и правая границы
        draw.rectangle(
            [(0, 0), (border_width, self.height)],
            fill=border_color
        )
        draw.rectangle(
            [(self.width - border_width, 0), (self.width, self.height)],
            fill=border_color
        )
        
        return img

    def _validate_and_normalize_text(self, text: str) -> str:
        """Валидировать и нормализовать текст перед отрисовкой."""
        # Удаляем markdown
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # **bold**
        text = re.sub(r'\*([^*]+)\*', r'\1', text)  # *italic*
        text = re.sub(r'#+\s*', '', text)  # заголовки
        text = re.sub(r'`([^`]+)`', r'\1', text)  # inline code
        text = re.sub(r'```[\s\S]*?```', '', text)  # code blocks
        
        # Нормализуем пробелы
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
        text = text.strip()
        
        # Проверяем длину
        if len(text) > self.max_text_length:
            raise TextTooLongError(
                f"Текст слишком длинный ({len(text)} символов). "
                f"Максимальная длина: {self.max_text_length} символов."
            )
        
        return text

    def _calculate_font_size_for_text(
        self, text: str, font_size: int, max_width: int, max_height: int
    ) -> tuple[int, ImageFont.FreeTypeFont | ImageFont.ImageFont]:
        """Рассчитать оптимальный размер шрифта для текста."""
        # Пробуем разные размеры шрифта
        for size in range(font_size, self.min_font_size - 1, -2):
            font = self._load_font(size)
            lines = self._wrap_text(text, font, max_width)
            line_height = size + 10  # Межстрочное расстояние
            total_height = len(lines) * line_height
            
            if total_height <= max_height:
                return size, font
        
        # Если не помещается даже с минимальным шрифтом, возвращаем минимальный
        return self.min_font_size, self._load_font(self.min_font_size)

    def _wrap_text(self, text: str, font, max_width: int) -> list[str]:
        """Перенос текста по словам с правильной обработкой."""
        # Разбиваем на абзацы
        paragraphs = text.split('\n')
        all_lines = []
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue
            
            words = paragraph.split()
            current_line = []

            for word in words:
                test_line = " ".join(current_line + [word])
                try:
                    bbox = font.getbbox(test_line)
                    text_width = bbox[2] - bbox[0]
                except Exception:
                    # Fallback: используем приблизительную ширину
                    text_width = len(test_line) * (font.size if hasattr(font, 'size') else 12)

                if text_width <= max_width:
                    current_line.append(word)
                else:
                    if current_line:
                        all_lines.append(" ".join(current_line))
                    current_line = [word]

            if current_line:
                all_lines.append(" ".join(current_line))
        
        return all_lines if all_lines else [text]

    def _validate_anchor(self, anchor: str) -> str:
        """Валидировать и нормализовать anchor параметр."""
        # Проверяем тип
        if not isinstance(anchor, str):
            logger.warning(f"[CardGeneratorImpl] Invalid anchor type: {type(anchor)}, using 'mm'")
            return "mm"
        
        # Проверяем длину
        if len(anchor) != 2:
            logger.warning(f"[CardGeneratorImpl] Invalid anchor length: {len(anchor)}, using 'mm'")
            return "mm"
        
        # Проверяем допустимые значения (Pillow поддерживает: lt, lm, lb, mt, mm, mb, rt, rm, rb, la, ma, ra)
        valid_anchors = ["lt", "lm", "lb", "mt", "mm", "mb", "rt", "rm", "rb", "la", "ma", "ra"]
        if anchor not in valid_anchors:
            logger.warning(f"[CardGeneratorImpl] Invalid anchor value: {anchor}, using 'mm'")
            return "mm"
        
        return anchor

    def _draw_text_multiline(
        self,
        draw: ImageDraw.ImageDraw,
        text: str,
        position: tuple[int, int],
        font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
        fill: tuple[int, int, int],
        max_width: int,
        line_spacing: int = 10,
        anchor: str = "mm",
    ) -> int:
        """Нарисовать многострочный текст с правильным переносом."""
        # ВАЛИДАЦИЯ: anchor должен быть строго 2 символа
        anchor = self._validate_anchor(anchor)
        
        lines = self._wrap_text(text, font, max_width)
        x, y = position
        
        # Получаем высоту строки
        try:
            bbox = font.getbbox("Ag")
            line_height = bbox[3] - bbox[1]
        except Exception:
            line_height = font.size if hasattr(font, 'size') else 20
        
        # Для многострочного текста используем горизонтальное центрирование
        # Вертикальное выравнивание - по базовой линии (ma = middle-ascent)
        # Если ma не поддерживается, используем mm (middle-middle)
        text_anchor = "ma"  # middle-ascent: горизонтально по центру, вертикально по базовой линии
        # Проверяем валидность
        text_anchor = self._validate_anchor(text_anchor)
        
        # Рисуем текст построчно
        for line in lines:
            try:
                draw.text((x, y), line, fill=fill, font=font, anchor=text_anchor)
            except ValueError as e:
                if "anchor" in str(e).lower():
                    logger.error(f"[CardGeneratorImpl] Anchor error: {e}, using fallback 'mm'")
                    text_anchor = "mm"
                    draw.text((x, y), line, fill=fill, font=font, anchor=text_anchor)
                else:
                    raise
            y += line_height + line_spacing
        
        return y

    def generate_card(
        self,
        full_name: str,
        company: str,
        position: str,
        greeting_text: str,
        comment: str | None = None,
        qr_url: str | None = None,
    ) -> bytes:
        """Сгенерировать открытку с retry механизмом."""
        max_retries = 2
        last_error = None
        
        for attempt in range(max_retries):
            try:
                return self._generate_card_internal(
                    full_name, company, position, greeting_text, comment, qr_url
                )
            except Exception as e:
                last_error = e
                logger.warning(
                    f"[CardGeneratorImpl] Card generation attempt {attempt + 1} failed: {e}",
                    exc_info=True
                )
                if attempt == max_retries - 1:
                    raise InvalidGreetingTextError(
                        f"Не удалось сгенерировать открытку: {str(e)}"
                    ) from e
        
        raise InvalidGreetingTextError("Не удалось сгенерировать открытку") from last_error

    def _generate_card_internal(
        self,
        full_name: str,
        company: str,
        position: str,
        greeting_text: str,
        comment: str | None = None,
        qr_url: str | None = None,
    ) -> bytes:
        """Внутренний метод генерации открытки."""
        # Валидация и нормализация текста
        greeting_text = self._validate_and_normalize_text(greeting_text)
        
        # Создаём изображение с градиентным фоном
        img = self._create_gradient_background()
        draw = ImageDraw.Draw(img)

        # Загружаем шрифты
        title_font = self._load_font(self.title_font_size)
        name_font = self._load_font(self.name_font_size)
        text_font = self._load_font(self.text_font_size)
        small_font = self._load_font(self.small_font_size)

        # Отступы
        padding_x = 80
        padding_y = 60
        content_width = self.width - 2 * padding_x
        
        # QR-код: фиксированный размер и позиция (по центру внизу)
        qr_size = 150  # Увеличиваем размер для лучшей читаемости
        qr_bottom_padding = 50  # Отступ от низа открытки
        
        # Позиция QR-кода: по центру горизонтально, внизу с отступом
        qr_x = (self.width - qr_size) // 2  # Центр по горизонтали
        qr_y = self.height - qr_size - qr_bottom_padding  # Внизу с отступом
        
        # Ширина текста не зависит от QR-кода (QR внизу, текст выше)
        text_max_width = content_width
        
        y_offset = padding_y

        # Заголовок (центрированный)
        try:
            draw.text(
                (self.width // 2, y_offset),
                "С Днем Рождения!",
                fill=self.accent_color,
                font=title_font,
                anchor="mm",
            )
        except ValueError as e:
            if "anchor" in str(e).lower():
                logger.error(f"[CardGeneratorImpl] Anchor error in title: {e}")
                raise InvalidGreetingTextError("Card rendering failed: invalid text layout configuration") from e
            raise
        y_offset += 90

        # ФИО (центрированный)
        try:
            draw.text(
                (self.width // 2, y_offset),
                full_name,
                fill=self.text_color,
                font=name_font,
                anchor="mm",
            )
        except ValueError as e:
            if "anchor" in str(e).lower():
                logger.error(f"[CardGeneratorImpl] Anchor error in name: {e}")
                raise InvalidGreetingTextError("Card rendering failed: invalid text layout configuration") from e
            raise
        y_offset += 50

        # Компания и должность (центрированный)
        company_position = f"{company}, {position}"
        try:
            draw.text(
                (self.width // 2, y_offset),
                company_position,
                fill=self.subtitle_color,
                font=text_font,
                anchor="mm",
            )
        except ValueError as e:
            if "anchor" in str(e).lower():
                logger.error(f"[CardGeneratorImpl] Anchor error in company/position: {e}")
                raise InvalidGreetingTextError("Card rendering failed: invalid text layout configuration") from e
            raise
        y_offset += 70

        # Поздравительный текст
        # Рассчитываем доступную высоту (учитываем место для QR-кода внизу)
        max_text_height = (qr_y - y_offset - 40) if qr_url else (self.height - y_offset - 40)
        
        # Подбираем размер шрифта под текст
        optimal_font_size, optimal_font = self._calculate_font_size_for_text(
            greeting_text, self.text_font_size, text_max_width, max_text_height
        )
        
        # Рисуем текст с правильным переносом
        line_spacing = optimal_font_size + 10
        y_offset = self._draw_text_multiline(
            draw,
            greeting_text,
            (self.width // 2, y_offset),
            optimal_font,
            self.text_color,
            text_max_width,
            line_spacing=line_spacing,
            anchor="mm",
        )

        # Комментарий (если есть, центрированный)
        if comment:
            y_offset += 30
            try:
                draw.text(
                    (self.width // 2, y_offset),
                    f"Комментарий: {comment}",
                    fill=self.subtitle_color,
                    font=small_font,
                    anchor="mm",
                )
            except ValueError as e:
                if "anchor" in str(e).lower():
                    logger.error(f"[CardGeneratorImpl] Anchor error in comment: {e}")
                    raise InvalidGreetingTextError("Card rendering failed: invalid text layout configuration") from e
                raise

        # QR-код (всегда по центру внизу открытки)
        if qr_url and qr_url.strip():
            try:
                qr_img = self._generate_qr_code(qr_url.strip(), size=qr_size)
                # Вставляем QR-код по центру внизу
                img.paste(qr_img, (qr_x, qr_y))
                logger.info(f"[CardGeneratorImpl] QR code generated and placed at ({qr_x}, {qr_y}), size={qr_size}")
            except Exception as e:
                logger.error(f"[CardGeneratorImpl] Failed to generate QR code: {e}", exc_info=True)
                # НЕ пропускаем ошибку - QR-код критичен, если он запрошен
                raise InvalidGreetingTextError(f"Не удалось сгенерировать QR-код: {str(e)}") from e

        # Сохраняем в bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG", optimize=True)
        card_bytes = img_byte_arr.getvalue()
        
        # Проверяем результат
        if not card_bytes or len(card_bytes) < 100:
            raise InvalidGreetingTextError("Сгенерированная открытка пуста или повреждена")
        
        logger.info(f"[CardGeneratorImpl] Card generated successfully, size={len(card_bytes)} bytes")
        return card_bytes

    def _generate_qr_code(self, url: str, size: int = 150) -> Image.Image:
        """Сгенерировать QR-код с высоким качеством."""
        # Используем более высокую коррекцию ошибок для надёжности
        qr = qrcode.QRCode(
            version=None,  # Автоматический выбор версии
            box_size=8,  # Уменьшаем box_size для более чёткого изображения
            border=2,  # Уменьшаем border для компактности
            error_correction=qrcode.constants.ERROR_CORRECT_M,  # Средняя коррекция ошибок
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Генерируем QR-код с высоким разрешением
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Используем NEAREST для сохранения чёткости (без размытия)
        qr_img = qr_img.resize((size, size), Image.Resampling.NEAREST)
        
        return qr_img
