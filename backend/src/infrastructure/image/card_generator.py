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
        
        # Цвета (КОНТРАСТНЫЕ для читаемости)
        self.text_color = (20, 20, 20)  # Очень тёмный для максимального контраста
        self.accent_color = (50, 100, 150)  # Тёмно-синий для заголовков
        self.subtitle_color = (80, 80, 80)  # Тёмно-серый для подзаголовков
        
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
        """Создать универсальный градиентный фон для открытки с рамкой."""
        # ОДИН УНИВЕРСАЛЬНЫЙ ШАБЛОН - без вариаций
        img = Image.new("RGB", (self.width, self.height), (250, 250, 250))  # Светло-серый базовый
        draw = ImageDraw.Draw(img)
        
        # Мягкий градиент от светло-голубого к светло-серому (УНИВЕРСАЛЬНЫЙ)
        for y in range(self.height):
            # Градиент от (248, 252, 255) к (245, 248, 250)
            ratio = y / self.height
            r = int(248 + (245 - 248) * ratio)
            g = int(252 + (248 - 252) * ratio)
            b = int(255 + (250 - 255) * ratio)
            draw.line([(0, y), (self.width, y)], fill=(r, g, b))
        
        # Рамка по периметру (ОБЯЗАТЕЛЬНА)
        border_width = 4
        border_color = (200, 210, 220)  # Нейтральный серый
        
        # Верхняя граница
        draw.rectangle([(0, 0), (self.width, border_width)], fill=border_color)
        # Нижняя граница
        draw.rectangle([(0, self.height - border_width), (self.width, self.height)], fill=border_color)
        # Левая граница
        draw.rectangle([(0, 0), (border_width, self.height)], fill=border_color)
        # Правая граница
        draw.rectangle([(self.width - border_width, 0), (self.width, self.height)], fill=border_color)
        
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

    def _wrap_text(self, text: str, font, max_width: int, max_lines: int = 20) -> list[str]:
        """Перенос текста по словам с жёстким ограничением ширины и количества строк."""
        # Разбиваем на абзацы
        paragraphs = text.split('\n')
        all_lines = []
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue
            
            # Если достигнут лимит строк - обрезаем
            if len(all_lines) >= max_lines:
                all_lines.append("...")
                break
            
            words = paragraph.split()
            current_line = []

            for word in words:
                # Если достигнут лимит строк - обрезаем
                if len(all_lines) >= max_lines:
                    if current_line:
                        all_lines.append(" ".join(current_line) + "...")
                    break
                
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
                    
                    # Если одно слово длиннее max_width - разбиваем принудительно
                    if len(word) * (font.size if hasattr(font, 'size') else 12) > max_width:
                        # Разбиваем длинное слово
                        chars_per_line = max_width // (font.size if hasattr(font, 'size') else 12)
                        for i in range(0, len(word), chars_per_line):
                            if len(all_lines) >= max_lines:
                                break
                            all_lines.append(word[i:i+chars_per_line])
                        current_line = []

            if current_line and len(all_lines) < max_lines:
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

        # Отступы (минимум 64px как требуется)
        padding_x = 64
        padding_y = 64
        content_width = self.width - 2 * padding_x
        
        # QR-код: фиксированный размер и позиция (ЖЁСТКО ЗАХАРДКОЖЕНО)
        qr_size = 150
        qr_bottom_padding = 48  # ТОЧНО 48px от низа
        
        # Позиция QR-кода: ЖЁСТКО ЗАХАРДКОЖЕНО (абсолютные координаты, БЕЗ anchor)
        qr_x = (self.width - qr_size) // 2  # Центр по X
        qr_y = self.height - qr_size - qr_bottom_padding  # Внизу с отступом 48px
        
        # ЯВНОЕ ЛОГИРОВАНИЕ позиции QR-кода
        logger.info(
            f"[CardGeneratorImpl] QR code position calculated: "
            f"qr_url={bool(qr_url)}, qr_x={qr_x}, qr_y={qr_y}, qr_size={qr_size}, "
            f"canvas_size=({self.width}, {self.height})"
        )
        
        # Максимальная ширина текста (жёстко ограничена)
        text_max_width = content_width - 40  # Дополнительный отступ для читаемости
        
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

        # QR-код (ОБЯЗАТЕЛЬНО должен быть нарисован, если передан)
        qr_drawn = False
        if qr_url and qr_url.strip():
            try:
                logger.info(f"[CardGeneratorImpl] Generating QR code for URL: {qr_url[:50]}...")
                qr_img = self._generate_qr_code(qr_url.strip(), size=qr_size)
                
                # Вставляем QR-код по абсолютным координатам (БЕЗ anchor)
                img.paste(qr_img, (qr_x, qr_y))
                qr_drawn = True
                
                logger.info(
                    f"[CardGeneratorImpl] QR code SUCCESSFULLY drawn at absolute position: "
                    f"x={qr_x}, y={qr_y}, size={qr_size}x{qr_size}, "
                    f"canvas_size=({self.width}x{self.height})"
                )
            except Exception as e:
                logger.error(
                    f"[CardGeneratorImpl] FAILED to generate/draw QR code: {e}",
                    exc_info=True
                )
                # КРИТИЧНО: если QR запрошен, но не нарисован - это ошибка
                raise InvalidGreetingTextError(
                    f"Не удалось сгенерировать QR-код: {str(e)}"
                ) from e
        else:
            logger.info("[CardGeneratorImpl] QR code not requested (qr_url is empty or None)")
        
        # ПРОВЕРКА: если QR должен был быть нарисован, но не был - ошибка
        if qr_url and qr_url.strip() and not qr_drawn:
            logger.error("[CardGeneratorImpl] QR code was requested but NOT drawn!")
            raise InvalidGreetingTextError("QR-код не был нарисован на открытке")

        # Сохраняем в bytes
        try:
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format="PNG", optimize=True)
            card_bytes = img_byte_arr.getvalue()
        except Exception as e:
            logger.error(f"[CardGeneratorImpl] Failed to save image to bytes: {e}", exc_info=True)
            raise InvalidGreetingTextError(f"Не удалось сохранить открытку: {str(e)}") from e
        
        # КРИТИЧЕСКАЯ ПРОВЕРКА: картинка должна быть валидной
        if not card_bytes:
            logger.error("[CardGeneratorImpl] Generated card is EMPTY (0 bytes)")
            raise InvalidGreetingTextError("Сгенерированная открытка пуста")
        
        if len(card_bytes) < 100:
            logger.error(f"[CardGeneratorImpl] Generated card is too small: {len(card_bytes)} bytes")
            raise InvalidGreetingTextError("Сгенерированная открытка повреждена (слишком маленький размер)")
        
        # Проверяем, что это валидный PNG (должен начинаться с PNG signature)
        if not card_bytes.startswith(b'\x89PNG\r\n\x1a\n'):
            logger.error("[CardGeneratorImpl] Generated card is not a valid PNG file")
            raise InvalidGreetingTextError("Сгенерированная открытка повреждена (невалидный формат)")
        
        logger.info(
            f"[CardGeneratorImpl] Card generated SUCCESSFULLY: "
            f"size={len(card_bytes)} bytes, qr_drawn={qr_drawn}, "
            f"canvas_size=({self.width}x{self.height})"
        )
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
