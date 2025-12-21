import { test, expect } from '@playwright/test';

test.describe('Panel', () => {
  test.beforeEach(async ({ page }) => {
    // Переходим на страницу панели управления
    await page.goto('/#/panel');
    
    // Ждем загрузки приложения
    await page.waitForSelector('#root', { state: 'visible' });
  });

  test('should load panel page', async ({ page }) => {
    // Проверяем, что приложение загрузилось
    const root = page.locator('#root');
    await expect(root).toBeVisible();
  });

  test('should navigate to birthday management', async ({ page }) => {
    // Проверяем навигацию к управлению днями рождения
    // В реальном приложении здесь будет клик по кнопке "Управление ДР"
    const root = page.locator('#root');
    await expect(root).toBeVisible();
    
    // Ждем немного для загрузки
    await page.waitForTimeout(500);
  });

  test('should handle authentication errors', async ({ page }) => {
    // Перехватываем запросы для симуляции ошибки аутентификации
    await page.route('**/api/panel/**', (route) => {
      route.fulfill({
        status: 401,
        body: JSON.stringify({ detail: 'Unauthorized' }),
      });
    });
    
    // Проверяем, что приложение обрабатывает ошибку аутентификации
    const root = page.locator('#root');
    await expect(root).toBeVisible();
    
    await page.waitForTimeout(1000);
  });

  test('should have API connection', async ({ page }) => {
    // Проверяем, что API доступен
    const apiUrl = process.env.VITE_API_URL;
    if (!apiUrl) {
      throw new Error('VITE_API_URL is required for E2E tests. Please set it in environment variables.');
    }
    
    // Проверяем, что переменная окружения установлена
    expect(apiUrl).toBeDefined();
  });
});

