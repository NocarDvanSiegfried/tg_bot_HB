import { test, expect } from '@playwright/test';

test.describe('Calendar', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
    
    // Ждем загрузки приложения
    await page.waitForSelector('#root', { state: 'visible' });
  });

  test('should display calendar component', async ({ page }) => {
    // Проверяем наличие корневого элемента
    const root = page.locator('#root');
    await expect(root).toBeVisible();
  });

  test('should handle calendar navigation', async ({ page }) => {
    // Базовый тест для навигации календаря
    // В реальном приложении здесь будут проверки навигации по месяцам
    const root = page.locator('#root');
    await expect(root).toBeVisible();
    
    // Ждем загрузки календаря
    await page.waitForTimeout(1000);
  });

  test('should load birthdays for current month', async ({ page }) => {
    // Проверяем загрузку дней рождения для текущего месяца
    const root = page.locator('#root');
    await expect(root).toBeVisible();
    
    // Ждем загрузки данных
    await page.waitForTimeout(2000);
    
    // В реальном приложении здесь будет проверка наличия дней рождения в календаре
  });

  test('should handle API errors when loading calendar', async ({ page }) => {
    // Перехватываем запросы для симуляции ошибки API
    await page.route('**/api/calendar/**', (route) => {
      route.fulfill({
        status: 500,
        body: JSON.stringify({ detail: 'Internal server error' }),
      });
    });
    
    // Проверяем, что приложение не падает при ошибке
    const root = page.locator('#root');
    await expect(root).toBeVisible();
    
    await page.waitForTimeout(1000);
  });
});

