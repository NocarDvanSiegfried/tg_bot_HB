/**
 * Validation Utilities - утилиты для валидации данных
 * 
 * Централизованные функции валидации для переиспользования
 * в различных компонентах.
 */

export interface ValidationResult {
  isValid: boolean
  errors: string[]
}

/**
 * Валидация даты в формате YYYY-MM-DD
 * 
 * Проверяет:
 * - Формат даты (YYYY-MM-DD)
 * - Валидность даты
 * - Что дата не в будущем
 * 
 * @param date - дата в формате YYYY-MM-DD
 * @returns ValidationResult с результатами валидации
 */
export function validateDate(date: string): ValidationResult {
  const errors: string[] = []
  
  // Проверка наличия даты
  if (!date) {
    errors.push('Дата рождения обязательна')
    return { isValid: false, errors }
  }
  
  // Проверка формата YYYY-MM-DD
  const dateRegex = /^\d{4}-\d{2}-\d{2}$/
  if (!dateRegex.test(date)) {
    errors.push('Неверный формат даты. Используйте формат YYYY-MM-DD')
    return { isValid: false, errors }
  }
  
  // Проверка валидности даты
  const dateObj = new Date(date + 'T00:00:00')
  if (isNaN(dateObj.getTime())) {
    errors.push('Неверная дата рождения. Проверьте правильность введённой даты')
    return { isValid: false, errors }
  }
  
  // Проверка, что дата не в будущем
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  if (dateObj > today) {
    errors.push('Дата рождения не может быть в будущем')
    return { isValid: false, errors }
  }
  
  return { isValid: true, errors: [] }
}

