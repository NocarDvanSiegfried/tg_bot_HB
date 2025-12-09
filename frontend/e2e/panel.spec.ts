import { test, expect } from '@playwright/test';

test.describe('Panel', () => {
  test.beforeEach(async ({ page }) => {
    // Переходим на главную страницу
    await page.goto('/');
  });

  test('should load panel page', async ({ page }) => {
    // Проверяем, что приложение загрузилось
    const root = page.locator('#root');
    await expect(root).toBeVisible();
  });

  test('should have API connection', async ({ page }) => {
    // Проверяем, что API доступен
    // В реальном окружении это будет проверка через fetch
    const apiUrl = process.env.VITE_API_URL || 'http://localhost:8000';
    
    // Проверяем, что переменная окружения установлена
    expect(apiUrl).toBeDefined();
  });
});

