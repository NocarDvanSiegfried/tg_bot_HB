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

        # Поздравительный текст
        text_lines = self._wrap_text(greeting_text, text_font, self.width - 200)
        for line in text_lines:
            draw.text(
                (self.width // 2, y_offset),
                line,
                fill=self.text_color,
                font=text_font,
                anchor="mm",
            )
            y_offset += 35

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

        # QR-код
        if qr_url:
            qr_img = self._generate_qr_code(qr_url, size=150)
            qr_x = self.width - 200
            qr_y = self.height - 200
            img.paste(qr_img, (qr_x, qr_y))

        # Сохраняем в bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="PNG")
        return img_byte_arr.getvalue()

    def _wrap_text(self, text: str, font, max_width: int) -> list[str]:
        """Перенос текста по словам."""
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            test_line = " ".join(current_line + [word])
            bbox = font.getbbox(test_line)
            text_width = bbox[2] - bbox[0]

            if text_width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]

        if current_line:
            lines.append(" ".join(current_line))

        return lines

    def _generate_qr_code(self, url: str, size: int = 150) -> Image.Image:
        """Сгенерировать QR-код."""
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img = qr_img.resize((size, size))
        return qr_img
