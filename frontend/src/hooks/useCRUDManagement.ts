import { useState, useEffect, useRef } from 'react'
import { logger } from '../utils/logger'

/**
 * Generic хук для управления CRUD операциями
 * 
 * Устраняет дублирование кода между BirthdayManagement и ResponsibleManagement
 * 
 * @template T - тип сущности, должен иметь поле id: number
 */
export interface UseCRUDManagementOptions<T extends { id: number }> {
  /** Функция загрузки списка элементов */
  loadData: () => Promise<T[]>
  /** Функция создания нового элемента */
  createItem: (data: Partial<T>) => Promise<T>
  /** Функция обновления элемента */
  updateItem: (id: number, data: Partial<T>) => Promise<T>
  /** Функция удаления элемента */
  deleteItem: (id: number) => Promise<void>
  /** Опциональная функция валидации перед созданием/обновлением */
  validateItem?: (data: Partial<T>, isEdit?: boolean) => boolean | string[]
  /** Опциональная функция нормализации элемента перед редактированием (например, нормализация даты) */
  normalizeItem?: (item: T) => Partial<T>
  /** Опциональная функция получения сообщения об ошибке создания */
  getCreateErrorMessage?: () => string
  /** Опциональная функция получения сообщения об ошибке обновления */
  getUpdateErrorMessage?: () => string
  /** Опциональная функция получения сообщения об ошибке удаления */
  getDeleteErrorMessage?: () => string
  /** Опциональная функция получения сообщения об ошибке загрузки */
  getLoadErrorMessage?: () => string
  /** Опциональная функция получения текста подтверждения удаления */
  getDeleteConfirmMessage?: (item: T) => string
  /** Опциональный флаг использования isMountedRef (для компонентов с cleanup) */
  useMountedRef?: boolean
}

export interface UseCRUDManagementReturn<T extends { id: number }> {
  // Состояния
  items: T[]
  loading: boolean
  creating: boolean
  updating: number | null
  deleting: number | null
  editingId: number | null
  error: string | null
  showAddForm: boolean
  formData: Partial<T>
  editFormData: Partial<T>
  
  // Функции управления состоянием
  setFormData: React.Dispatch<React.SetStateAction<Partial<T>>>
  setEditFormData: React.Dispatch<React.SetStateAction<Partial<T>>>
  setShowAddForm: React.Dispatch<React.SetStateAction<boolean>>
  setError: React.Dispatch<React.SetStateAction<string | null>>
  
  // CRUD операции
  loadItems: () => Promise<void>
  handleSubmit: (e: React.FormEvent) => Promise<void>
  handleEdit: (id: number) => void
  handleUpdate: (id: number) => Promise<void>
  handleDelete: (id: number) => Promise<void>
  handleCancelEdit: () => void
  
  // Валидация
  validateForm: () => boolean
  validateEditForm: () => boolean
}

/**
 * Общий хук для CRUD операций
 */
export function useCRUDManagement<T extends { id: number }>(
  options: UseCRUDManagementOptions<T>
): UseCRUDManagementReturn<T> {
  const {
    loadData,
    createItem,
    updateItem,
    deleteItem,
    validateItem,
    normalizeItem,
    getCreateErrorMessage = () => 'Не удалось создать элемент',
    getUpdateErrorMessage = () => 'Не удалось обновить элемент',
    getDeleteErrorMessage = () => 'Не удалось удалить элемент',
    getLoadErrorMessage = () => 'Не удалось загрузить данные',
    getDeleteConfirmMessage = () => 'Вы уверены, что хотите удалить этот элемент?',
    useMountedRef = false,
  } = options

  // Состояния
  const [items, setItems] = useState<T[]>([])
  const [loading, setLoading] = useState(false)
  const [creating, setCreating] = useState(false)
  const [updating, setUpdating] = useState<number | null>(null)
  const [deleting, setDeleting] = useState<number | null>(null)
  const [editingId, setEditingId] = useState<number | null>(null)
  const [editFormData, setEditFormData] = useState<Partial<T>>({})
  const [error, setError] = useState<string | null>(null)
  const [showAddForm, setShowAddForm] = useState(false)
  const [formData, setFormData] = useState<Partial<T>>({})
  
  const isMountedRef = useRef(true)

  useEffect(() => {
    if (useMountedRef) {
      isMountedRef.current = true
    }
    loadItems()
    return () => {
      if (useMountedRef) {
        isMountedRef.current = false
      }
    }
  }, [])

  /**
   * Обработка ошибок с универсальными сообщениями
   */
  const handleError = (error: unknown, defaultMessage: string): string => {
    logger.error('CRUD operation error:', error)
    let errorMessage = defaultMessage
    
    if (error instanceof Error) {
      errorMessage = error.message || errorMessage
      
      // Улучшенная обработка различных типов ошибок
      if (errorMessage.includes('CORS') || errorMessage.includes('Network')) {
        errorMessage = 'Ошибка сети. Проверьте подключение к интернету.'
      } else if (errorMessage.includes('401') || errorMessage.includes('авторизац')) {
        errorMessage = 'Ошибка авторизации. Пожалуйста, обновите страницу.'
      } else if (errorMessage.includes('422') || errorMessage.includes('валидац')) {
        errorMessage = 'Ошибка валидации данных. Проверьте введенные данные.'
      } else if (errorMessage.includes('404')) {
        errorMessage = 'Элемент не найден. Возможно, он был удален.'
      } else if (errorMessage.includes('500')) {
        errorMessage = 'Ошибка сервера. Пожалуйста, попробуйте позже.'
      }
    }
    
    return errorMessage
  }

  /**
   * Загрузка списка элементов
   */
  const loadItems = async () => {
    setLoading(true)
    try {
      setError(null)
      const data = await loadData()
      
      if (useMountedRef && !isMountedRef.current) return
      
      setItems(data)
    } catch (error) {
      logger.error('Failed to load items:', error)
      
      if (useMountedRef && !isMountedRef.current) return
      
      setError(handleError(error, getLoadErrorMessage()))
    } finally {
      if (useMountedRef && !isMountedRef.current) return
      
      setLoading(false)
    }
  }

  /**
   * Валидация формы создания
   */
  const validateForm = (): boolean => {
    if (!validateItem) return true
    
    const result = validateItem(formData, false)
    
    if (typeof result === 'boolean') {
      return result
    }
    
    if (Array.isArray(result) && result.length > 0) {
      const errorMsg = result.length === 1 
        ? result[0]
        : `Ошибки валидации:\n${result.map((err, idx) => `${idx + 1}. ${err}`).join('\n')}`
      setError(errorMsg)
      return false
    }
    
    return true
  }

  /**
   * Валидация формы редактирования
   */
  const validateEditForm = (): boolean => {
    if (!validateItem) return true
    
    const result = validateItem(editFormData, true)
    
    if (typeof result === 'boolean') {
      return result
    }
    
    if (Array.isArray(result) && result.length > 0) {
      const errorMsg = result.length === 1 
        ? result[0]
        : `Ошибки валидации:\n${result.map((err, idx) => `${idx + 1}. ${err}`).join('\n')}`
      setError(errorMsg)
      return false
    }
    
    return true
  }

  /**
   * Создание нового элемента
   */
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (creating) return
    
    try {
      setError(null)
      
      if (!validateForm()) {
        return
      }
      
      setCreating(true)
      await createItem(formData)
      
      // Очистка формы после успешного создания
      setFormData({})
      setShowAddForm(false)
      await loadItems()
    } catch (error) {
      logger.error('Failed to create item:', error)
      setError(handleError(error, getCreateErrorMessage()))
    } finally {
      setCreating(false)
    }
  }

  /**
   * Инициализация редактирования элемента
   */
  const handleEdit = (id: number) => {
    logger.info(`[CRUD] handleEdit called for id=${id}`)
    const item = items.find(i => i.id === id)
    
    if (item) {
      logger.info(`[CRUD] Found item to edit:`, item)
      
      // Применяем нормализацию, если она указана
      const normalizedData = normalizeItem ? normalizeItem(item) : { ...item }
      
      setEditingId(id)
      setEditFormData(normalizedData)
      setError(null)
      logger.info(`[CRUD] Edit form initialized for id=${id}`)
    } else {
      logger.error(`[CRUD] Item with id=${id} not found`)
      setError(`Элемент с ID ${id} не найден`)
    }
  }

  /**
   * Обновление элемента
   */
  const handleUpdate = async (id: number) => {
    logger.info(`[CRUD] ===== handleUpdate CALLED for id=${id} =====`)
    
    if (updating === id) return
    
    try {
      setError(null)
      
      if (!validateEditForm()) {
        logger.warn('[CRUD] Validation failed - NOT sending request')
        return
      }
      
      setUpdating(id)
      logger.info(`[CRUD] ===== READY TO SEND PUT REQUEST =====`)
      logger.info(`[CRUD] Data:`, JSON.stringify(editFormData))
      
      await updateItem(id, editFormData)
      
      logger.info(`[CRUD] Item ${id} updated successfully`)
      
      setEditingId(null)
      setEditFormData({})
      await loadItems()
      logger.info(`[CRUD] [STATE UPDATE] State updated successfully after update`)
    } catch (error) {
      logger.error(`[CRUD] PUT request failed:`, error)
      logger.error(`[CRUD] Error details:`, {
        name: error instanceof Error ? error.name : 'Unknown',
        message: error instanceof Error ? error.message : String(error),
        stack: error instanceof Error ? error.stack : undefined
      })
      
      setError(handleError(error, getUpdateErrorMessage()))
    } finally {
      setUpdating(null)
    }
  }

  /**
   * Отмена редактирования
   */
  const handleCancelEdit = () => {
    setEditingId(null)
    setEditFormData({})
    setError(null)
  }

  /**
   * Удаление элемента
   */
  const handleDelete = async (id: number) => {
    logger.info(`[CRUD] ===== handleDelete CALLED for id=${id} =====`)
    
    if (deleting === id) return
    
    // Находим элемент для отображения в подтверждении
    const itemToDelete = items.find(i => i.id === id)
    const confirmMessage = itemToDelete 
      ? getDeleteConfirmMessage(itemToDelete)
      : 'Вы уверены, что хотите удалить этот элемент?'
    
    if (!confirm(confirmMessage)) {
      logger.info(`[CRUD] Delete cancelled for item ${id}`)
      return
    }
    
    try {
      setError(null)
      setDeleting(id)
      
      logger.info(`[CRUD] ===== READY TO SEND DELETE REQUEST =====`)
      logger.info(`[CRUD] Deleting item ${id}`)
      
      await deleteItem(id)
      
      logger.info(`[CRUD] Item ${id} deleted successfully`)
      await loadItems()
      logger.info(`[CRUD] [STATE UPDATE] State updated successfully after delete`)
    } catch (error) {
      logger.error(`[CRUD] DELETE request failed:`, error)
      logger.error(`[CRUD] Error details:`, {
        name: error instanceof Error ? error.name : 'Unknown',
        message: error instanceof Error ? error.message : String(error),
        stack: error instanceof Error ? error.stack : undefined
      })
      
      setError(handleError(error, getDeleteErrorMessage()))
    } finally {
      setDeleting(null)
    }
  }

  return {
    // Состояния
    items,
    loading,
    creating,
    updating,
    deleting,
    editingId,
    error,
    showAddForm,
    formData,
    editFormData,
    
    // Функции управления состоянием
    setFormData,
    setEditFormData,
    setShowAddForm,
    setError,
    
    // CRUD операции
    loadItems,
    handleSubmit,
    handleEdit,
    handleUpdate,
    handleDelete,
    handleCancelEdit,
    
    // Валидация
    validateForm,
    validateEditForm,
  }
}

