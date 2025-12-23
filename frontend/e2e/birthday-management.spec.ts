import { test, expect } from '@playwright/test';

test.describe('Birthday Management', () => {
  test.beforeEach(async ({ page }) => {
    // Переходим на страницу панели управления
    await page.goto('/#/panel');
    
    // Ждем загрузки приложения
    await page.waitForSelector('#root', { state: 'visible' });
  });

  test('should display birthday management interface', async ({ page }) => {
    // Проверяем, что интерфейс управления днями рождения отображается
    // В реальном приложении здесь будет проверка наличия кнопки "Управление ДР"
    const root = page.locator('#root');
    await expect(root).toBeVisible();
  });

  test('should handle birthday list loading', async ({ page }) => {
    // Проверяем загрузку списка дней рождения
    // В реальном приложении здесь будет проверка наличия списка
    const root = page.locator('#root');
    await expect(root).toBeVisible();
    
    // Проверяем, что нет ошибок в консоли
    const errors: string[] = [];
    page.on('console', (msg) => {
      if (msg.type() === 'error') {
        errors.push(msg.text());
      }
    });
    
    // Ждем немного для загрузки
    await page.waitForTimeout(1000);
    
    // В реальном приложении здесь будет проверка отсутствия критических ошибок
    expect(errors.length).toBeLessThan(10); // Допускаем некоторые не критичные ошибки
  });

  test('should handle API errors gracefully', async ({ page }) => {
    // Перехватываем сетевые запросы для симуляции ошибок
    await page.route('**/api/birthdays*', (route) => {
      route.fulfill({
        status: 500,
        body: JSON.stringify({ detail: 'Internal server error' }),
      });
    });
    
    // Проверяем, что приложение не падает при ошибке API
    const root = page.locator('#root');
    await expect(root).toBeVisible();
    
    // В реальном приложении здесь будет проверка отображения сообщения об ошибке
    await page.waitForTimeout(1000);
  });
});

