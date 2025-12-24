/**
 * Утилита для определения и управления тёмной темой
 * 
 * Использует Telegram WebApp API для определения темы и применяет
 * соответствующий класс к корневому элементу документа.
 */

/**
 * Определяет, является ли текущая тема тёмной
 * @returns true, если тема тёмная, false иначе
 */
export function isDarkTheme(): boolean {
  // Проверка через Telegram WebApp API (основной метод)
  if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
    const colorScheme = window.Telegram.WebApp.colorScheme;
    if (colorScheme === 'dark') {
      return true;
    }
    if (colorScheme === 'light') {
      return false;
    }
  }

  // Fallback: проверка через CSS media query
  if (typeof window !== 'undefined' && window.matchMedia) {
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  }

  // По умолчанию светлая тема
  return false;
}

/**
 * Применяет тему к документу
 * @param isDark - true для тёмной темы, false для светлой
 */
export function applyTheme(isDark: boolean): void {
  const root = document.documentElement;
  if (isDark) {
    root.setAttribute('data-theme', 'dark');
  } else {
    root.removeAttribute('data-theme');
  }
}

/**
 * Инициализирует тему при загрузке страницы
 */
export function initTheme(): void {
  const dark = isDarkTheme();
  applyTheme(dark);

  // Слушаем изменения темы через Telegram WebApp API
  if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
    window.Telegram.WebApp.onEvent('themeChanged', () => {
      const newDark = isDarkTheme();
      applyTheme(newDark);
    });
  }

  // Слушаем изменения системной темы (fallback)
  if (typeof window !== 'undefined' && window.matchMedia) {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    mediaQuery.addEventListener('change', (e) => {
      // Проверяем Telegram API в первую очередь
      if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
        const telegramDark = window.Telegram.WebApp.colorScheme === 'dark';
        applyTheme(telegramDark);
      } else {
        applyTheme(e.matches);
      }
    });
  }
}

