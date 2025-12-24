import io
import logging
import os

import qrcode
from PIL import Image, ImageDraw, ImageFont

from src.application.ports.card_generator import CardGeneratorPort

logger = logging.getLogger(__name__)


class CardGeneratorImpl(CardGeneratorPort):
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.background_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.accent_color = (70, 130, 180)
        # Конфигурация шрифтов из переменных окружения
        self.font_path = os.getenv("CARD_FONT_PATH", "arial.ttf")
        self.title_font_size = int(os.getenv("CARD_TITLE_FONT_SIZE", "48"))
        self.name_font_size = int(os.getenv("CARD_NAME_FONT_SIZE", "36"))
        self.text_font_size = int(os.getenv("CARD_TEXT_FONT_SIZE", "24"))
        self.small_font_size = int(os.getenv("CARD_SMALL_FONT_SIZE", "20"))

    def generate_card(
        self,
        full_name: str,
        company: str,
        position: str,
        greeting_text: str,
        comment: str | None = None,
        qr_url: str | None = None,
    ) -> bytes:
        """Сгенерировать открытку."""
        img = Image.new("RGB", (self.width, self.height), self.background_color)
        draw = ImageDraw.Draw(img)

        try:
            title_font = ImageFont.truetype(self.font_path, self.title_font_size)
            name_font = ImageFont.truetype(self.font_path, self.name_font_size)
            text_font = ImageFont.truetype(self.font_path, self.text_font_size)
            small_font = ImageFont.truetype(self.font_path, self.small_font_size)
        except OSError as e:
            logger.warning(
                "Failed to load custom font, using default",
                extra={"error": str(e), "font_path": self.font_path},
            )
            title_font = ImageFont.load_default()
            name_font = ImageFont.load_default()
            text_font = ImageFont.load_default()
            small_font = ImageFont.load_default()

        y_offset = 50

        # Заголовок
        draw.text(
            (self.width // 2, y_offset),
            "С Днем Рождения!",
            fill=self.accent_color,
            font=title_font,
            anchor="mm",
        )
        y_offset += 80

        # ФИО
        draw.text(
            (self.width // 2, y_offset),
            full_name,
            fill=self.text_color,
            font=name_font,
            anchor="mm",
        )
        y_offset += 50

        # Компания и должность
        company_position = f"{company}, {position}"
        draw.text(
            (self.width // 2, y_offset),
            company_position,
            fill=self.text_color,
            font=text_font,
            anchor="mm",
        )
        y_offset += 80

        # Определяем размер и позицию QR-кода заранее
        qr_size = 150
        qr_margin = 20
        qr_x = self.width - qr_size - qr_margin
        qr_y = self.height - qr_size - qr_margin
        
        # Поздравительный текст - структурируем на логические блоки
        # Рассчитываем высоту текста для корректного размещения QR-кода
        text_blocks = self._structure_text(greeting_text)
        # Учитываем место для QR-кода при расчёте ширины текста
        text_max_width = self.width - 200 - (qr_size + qr_margin if qr_url else 0)
        text_height = self._calculate_text_height(text_blocks, text_font, text_max_width)
        
        # Проверяем, не перекрывает ли QR-код текст
        # Если текст занимает слишком много места, уменьшаем QR-код или смещаем выше
        if qr_url and text_height > qr_y - y_offset - 50:
            # Текст может перекрыться с QR-кодом
            available_height = qr_y - y_offset - 50
            if text_height > available_height:
                # Уменьшаем размер QR-кода
                qr_size = 120
                qr_x = self.width - qr_size - qr_margin
                qr_y = self.height - qr_size - qr_margin
                # Пересчитываем ширину текста с новым размером QR-кода
                text_max_width = self.width - 200 - (qr_size + qr_margin)
                text_height = self._calculate_text_height(text_blocks, text_font, text_max_width)
                # Если всё ещё не помещается, смещаем QR-код выше
                if text_height > qr_y - y_offset - 50:
                    qr_y = y_offset + text_height + 50
        
        # Рисуем структурированный текст
        line_spacing = 30  # Межстрочное расстояние
        paragraph_spacing = 20  # Отступ между абзацами
        
        for block_idx, block in enumerate(text_blocks):
            if block_idx > 0:
                # Отступ между блоками
                y_offset += paragraph_spacing
            
            block_lines = self._wrap_text(block, text_font, text_max_width)
            for line in block_lines:
                draw.text(
                    (self.width // 2, y_offset),
                    line,
                    fill=self.text_color,
                    font=text_font,
                    anchor="mm",
                )
                y_offset += line_spacing

        # Комментарий
        if comment:
            y_offset += 20
            draw.text(
                (self.width // 2, y_offset),
                f"Комментарий: {comment}",
                fill=(128, 128, 128),
                font=small_font,
                anchor="mm",
            )

        # QR-код (размещаем в правом нижнем углу с отступами)
        if qr_url:
            qr_img = self._generate_qr_code(qr_url, size=qr_size)
            img.paste(qr_img, (qr_x, qr_y))

        # Сохраняем в bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")
        return img_byte_arr.getvalue()

    def _structure_text(self, text: str) -> list[str]:
        """Разбить текст на логические блоки (обращение, основной текст, пожелания)."""
        import re
        
        # Нормализуем текст
        text = text.strip()
        
        # Разбиваем по предложениям
        sentences = re.split(r'([.!?]+)', text)
        # Объединяем предложения с их знаками препинания
        sentences = [sentences[i] + (sentences[i+1] if i+1 < len(sentences) else '') 
                     for i in range(0, len(sentences), 2) if sentences[i].strip()]
        
        if not sentences:
            return [text]
        
        # Определяем блоки:
        # 1. Обращение (первые 1-2 предложения, обычно содержат имя или обращение)
        # 2. Основной текст (остальные предложения)
        blocks = []
        current_block = []
        
        # Первое предложение обычно обращение
        if sentences:
            first_sentence = sentences[0].strip()
            if first_sentence:
                blocks.append(first_sentence)
        
        # Остальные предложения - основной текст
        if len(sentences) > 1:
            remaining_text = ' '.join(sentences[1:]).strip()
            if remaining_text:
                blocks.append(remaining_text)
        
        # Если блоков нет, возвращаем весь текст как один блок
        if not blocks:
            blocks = [text]
        
        return blocks

    def _calculate_text_height(self, text_blocks: list[str], font, max_width: int) -> int:
        """Рассчитать общую высоту текста с учётом переносов и отступов."""
        line_spacing = 30
        paragraph_spacing = 20
        
        total_height = 0
        for block_idx, block in enumerate(text_blocks):
            if block_idx > 0:
                total_height += paragraph_spacing
            
            block_lines = self._wrap_text(block, font, max_width)
            total_height += len(block_lines) * line_spacing
        
        return total_height

    def _wrap_text(self, text: str, font, max_width: int) -> list[str]:
        """Перенос текста по словам с сохранением логических абзацев."""
        # Если текст содержит переносы строк, сохраняем их как отдельные абзацы
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
                bbox = font.getbbox(test_line)
                text_width = bbox[2] - bbox[0]

                if text_width <= max_width:
                    current_line.append(word)
                else:
                    if current_line:
                        all_lines.append(" ".join(current_line))
                    current_line = [word]

            if current_line:
                all_lines.append(" ".join(current_line))
        
        return all_lines if all_lines else [text]

    def _generate_qr_code(self, url: str, size: int = 150) -> Image.Image:
        """Сгенерировать QR-код."""
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img = qr_img.resize((size, size))
        return qr_img
