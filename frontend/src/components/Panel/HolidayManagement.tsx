import { useEffect } from 'react'
import { useCRUDManagement } from '../../hooks/useCRUDManagement'
import { api } from '../../services/api'
import { Holiday } from '../../types/holiday'
import { logger } from '../../utils/logger'
import { validateDate } from '../../utils/validation'
import { API_BASE_URL } from '../../config/api'
import './Panel.css'

interface HolidayManagementProps {
  onBack: () => void
}

export default function HolidayManagement({ onBack }: HolidayManagementProps) {
  // Валидация для Holiday (специфичная логика)
  const validateHoliday = (data: Partial<Holiday>): string[] => {
    const errors: string[] = []
    
    if (!data.name?.trim()) {
      errors.push('Название праздника не может быть пустым')
    } else if (data.name.trim().length < 1) {
      errors.push('Название праздника должно содержать минимум 1 символ')
    } else if (data.name.trim().length > 255) {
      errors.push('Название праздника не может быть длиннее 255 символов')
    }
    
    // Проверка даты с использованием утилиты
    if (data.date) {
      const dateValidation = validateDate(data.date)
      if (!dateValidation.isValid) {
        errors.push(...dateValidation.errors)
      }
    } else {
      errors.push('Дата праздника обязательна')
    }
    
    // Проверка длины комментария
    if (data.description && data.description.length > 1000) {
      errors.push('Комментарий не может быть длиннее 1000 символов')
    }
    
    return errors
  }

  // Нормализация даты для редактирования (специфичная логика)
  const normalizeHoliday = (holiday: Holiday): Partial<Holiday> => {
    try {
      let normalizedDate = holiday.date
      if (normalizedDate) {
        // Если дата в формате ISO (с временем), извлечь только дату
        if (normalizedDate.includes('T')) {
          normalizedDate = normalizedDate.split('T')[0]
        }
        // Если дата в другом формате, попытаться преобразовать
        if (!/^\d{4}-\d{2}-\d{2}$/.test(normalizedDate)) {
          logger.warn(`[HolidayManagement] Invalid date format: ${normalizedDate}, attempting to fix`)
          try {
            const date = new Date(normalizedDate)
            if (!isNaN(date.getTime())) {
              normalizedDate = date.toISOString().split('T')[0]
            } else {
              logger.error(`[HolidayManagement] Could not parse date: ${normalizedDate}`)
              normalizedDate = '' // Fallback to empty string
            }
          } catch (e) {
            logger.error(`[HolidayManagement] Error normalizing date: ${e}`)
            normalizedDate = '' // Fallback to empty string
          }
        }
      }
      
      return {
        name: holiday.name || '',
        date: normalizedDate || '',
        description: holiday.description || '',
      }
    } catch (error) {
      logger.error(`[HolidayManagement] Error in normalizeHoliday:`, error)
      // Возвращаем безопасные значения по умолчанию
      return {
        name: holiday.name || '',
        date: holiday.date || '',
        description: holiday.description || '',
      }
    }
  }

  // Использование общего хука для CRUD операций
  const {
    items: holidays,
    loading,
    creating,
    updating,
    deleting,
    editingId,
    error,
    showAddForm,
    formData,
    editFormData,
    setFormData,
    setEditFormData,
    setShowAddForm,
    setError,
    handleSubmit,
    handleEdit,
    handleUpdate,
    handleDelete,
    handleCancelEdit,
  } = useCRUDManagement<Holiday>({
    loadData: api.getHolidays,
    createItem: async (data) => {
      // Преобразуем Partial<Holiday> в Omit<Holiday, 'id'> для API
      const holidayData: Omit<Holiday, 'id'> = {
        name: data.name!,
        date: data.date!,
        description: data.description,
      }
      return api.createHoliday(holidayData)
    },
    updateItem: api.updateHoliday,
    deleteItem: api.deleteHoliday,
    validateItem: validateHoliday,
    normalizeItem: normalizeHoliday,
    getCreateErrorMessage: () => 'Не удалось создать праздник',
    getUpdateErrorMessage: () => 'Не удалось обновить праздник',
    getDeleteErrorMessage: () => 'Не удалось удалить праздник',
    getLoadErrorMessage: () => 'Не удалось загрузить праздники',
    getDeleteConfirmMessage: (holiday) => 
      `Вы уверены, что хотите удалить праздник "${holiday.name}"?\n\nЭто действие нельзя отменить.`,
    useMountedRef: true,
  })

  // Диагностика изменений editingId (только в dev режиме)
  useEffect(() => {
    if (import.meta.env.DEV) {
      logger.info(`[HolidayManagement] editingId changed to: ${editingId}`)
    }
  }, [editingId])

  // Диагностическая информация (специфичная для HolidayManagement)
  const diagnosticInfo = {
    apiUrl: API_BASE_URL,
    hasInitData: typeof window !== 'undefined' && !!window.Telegram?.WebApp?.initData,
    initDataLength: typeof window !== 'undefined' && window.Telegram?.WebApp?.initData 
      ? window.Telegram.WebApp.initData.length 
      : 0,
  }

  return (
    <div className="panel-section">
      <button className="back-button" onClick={onBack}>🔙 Назад</button>
      <h3>Профессиональные праздники</h3>

      {/* Диагностическая информация (только в dev режиме) */}
      {import.meta.env.DEV && (
        <div style={{ 
          padding: '10px', 
          marginBottom: '10px', 
          background: '#e3f2fd', 
          color: '#1976d2', 
          borderRadius: '4px',
          fontSize: '12px',
          fontFamily: 'monospace'
        }}>
          <strong>🔍 Диагностика:</strong><br/>
          API URL: {diagnosticInfo.apiUrl}<br/>
          InitData: {diagnosticInfo.hasInitData ? `✅ (${diagnosticInfo.initDataLength} символов)` : '❌ отсутствует'}
        </div>
      )}

      {error && (
        <div className="error-message" style={{ padding: '10px', marginBottom: '10px', background: '#fee', color: '#c00', borderRadius: '4px', whiteSpace: 'pre-line' }}>
          ⚠️ {error}
        </div>
      )}

      <div style={{ marginBottom: '20px' }}>
        <button
          type="button"
          onClick={() => {
            if (showAddForm) {
              setFormData({ name: '', date: '', description: '' })
              setError(null)
            }
            setShowAddForm(!showAddForm)
          }}
          style={{
            padding: '12px 20px',
            backgroundColor: creating || editingId !== null ? '#ccc' : 'var(--color-success)',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: creating || editingId !== null ? 'not-allowed' : 'pointer',
            fontSize: '16px',
            fontWeight: 'bold',
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            opacity: creating || editingId !== null ? 0.6 : 1
          }}
          disabled={creating || editingId !== null}
        >
          {showAddForm ? '✖️ Отменить' : '➕ Добавить'}
        </button>
      </div>

      {showAddForm && (
        <form className="panel-form" onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Название праздника"
            value={(formData.name as string) || ''}
            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            required
            disabled={creating}
            maxLength={255}
          />
          <input
            type="date"
            placeholder="Дата праздника"
            value={(formData.date as string) || ''}
            onChange={(e) => setFormData({ ...formData, date: e.target.value })}
            required
            disabled={creating}
          />
          <textarea
            placeholder="Комментарий (необязательно)"
            value={(formData.description as string) || ''}
            onChange={(e) => setFormData({ ...formData, description: e.target.value })}
            disabled={creating}
            maxLength={1000}
          />
          <button type="submit" disabled={creating}>
            {creating ? '⏳ Добавление...' : 'Добавить'}
          </button>
        </form>
      )}

      {loading ? (
        <p>Загрузка...</p>
      ) : (
        <ul className="panel-list">
          {holidays.map((holiday, index) => {
            // Проверка валидности id
            const isValidId = holiday.id != null && typeof holiday.id === 'number' && !isNaN(holiday.id) && holiday.id > 0
            const isEditing = isValidId && editingId !== null && editingId === holiday.id
            
            if (import.meta.env.DEV) {
              logger.info(`[HolidayManagement] Rendering holiday id=${holiday.id}, editingId=${editingId}, isValidId=${isValidId}, isEditing=${isEditing}`)
            }
            
            return (
            <li key={holiday.id ?? `holiday-${index}`} className="panel-list-item">
              {isEditing ? (
                <div style={{ width: '100%' }}>
                  {!editFormData.name ? (
                    <div style={{ 
                      padding: '10px', 
                      background: '#fee', 
                      color: '#c00', 
                      borderRadius: '4px',
                      marginBottom: '10px'
                    }}>
                      ⚠️ Ошибка: данные для редактирования не загружены. Попробуйте обновить страницу.
                      <button 
                        onClick={handleCancelEdit}
                        style={{ marginLeft: '10px', padding: '5px 10px' }}
                      >
                        Закрыть
                      </button>
                    </div>
                  ) : (
                    <form
                      noValidate
                      onSubmit={async (e) => {
                        e.preventDefault()
                        logger.info(`[HolidayManagement] Form submitted for holiday id=${holiday.id}`)
                        
                        if (!holiday.id) {
                          logger.error('[HolidayManagement] Cannot update: holiday id is missing')
                          setError('Ошибка: ID праздника не найден')
                          return
                        }
                        
                        await handleUpdate(holiday.id)
                      }}
                      style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}
                    >
                    <input
                      type="text"
                      placeholder="Название праздника"
                      value={(editFormData.name as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, name: e.target.value })}
                      disabled={updating === holiday.id || showAddForm}
                      maxLength={255}
                    />
                    <input
                      type="date"
                      placeholder="Дата праздника"
                      value={(editFormData.date as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, date: e.target.value })}
                      disabled={updating === holiday.id || showAddForm}
                    />
                    <textarea
                      placeholder="Комментарий (необязательно)"
                      value={(editFormData.description as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, description: e.target.value })}
                      disabled={updating === holiday.id || showAddForm}
                      maxLength={1000}
                    />
                    {error && (
                      <div style={{ 
                        color: 'red', 
                        backgroundColor: '#ffebee', 
                        padding: '10px', 
                        borderRadius: '4px',
                        border: '1px solid #f44336',
                        marginTop: '5px',
                        fontSize: '14px',
                        fontWeight: 'bold',
                        whiteSpace: 'pre-line'
                      }}>
                        {error}
                      </div>
                    )}
                    <div style={{ display: 'flex', gap: '10px' }}>
                      <button type="submit" disabled={updating === holiday.id || showAddForm}>
                        {updating === holiday.id ? '⏳ Сохранение...' : 'Сохранить'}
                      </button>
                      <button type="button" onClick={handleCancelEdit} disabled={updating === holiday.id || showAddForm}>
                        Отмена
                      </button>
                    </div>
                  </form>
                  )}
                </div>
              ) : (
                <>
                  <div>
                    <strong>{holiday.name}</strong>
                    <br />
                    {holiday.date} {holiday.description && `(${holiday.description})`}
                  </div>
                  <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                    <button 
                      onClick={() => {
                        if (!holiday.id || holiday.id === 0) {
                          logger.error('[HolidayManagement] Cannot edit: holiday id is missing or invalid', holiday)
                          setError('Ошибка: ID праздника не найден')
                          return
                        }
                        logger.info(`[HolidayManagement] Edit button clicked for id=${holiday.id}, current editingId=${editingId}`)
                        handleEdit(holiday.id)
                        logger.info(`[HolidayManagement] After handleEdit call, editingId should be=${holiday.id}`)
                      }}
                      disabled={deleting === holiday.id || updating === holiday.id || editingId === holiday.id || showAddForm || !isValidId}
                      style={{
                        padding: '8px 16px',
                        backgroundColor: deleting === holiday.id || updating === holiday.id || editingId === holiday.id || showAddForm || !isValidId ? '#ccc' : 'var(--color-primary)',
                        color: 'white',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: deleting === holiday.id || updating === holiday.id || editingId === holiday.id || showAddForm || !isValidId ? 'not-allowed' : 'pointer',
                        fontSize: '14px',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '6px',
                        opacity: deleting === holiday.id || updating === holiday.id || editingId === holiday.id || showAddForm || !isValidId ? 0.6 : 1
                      }}
                    >
                      ✏️ Редактировать
                    </button>
                    <button 
                      onClick={() => {
                        if (!holiday.id || holiday.id === 0) {
                          logger.error('[HolidayManagement] Cannot delete: holiday id is missing or invalid')
                          setError('Ошибка: ID праздника не найден')
                          return
                        }
                        handleDelete(holiday.id)
                      }}
                      disabled={deleting === holiday.id || updating === holiday.id || editingId === holiday.id || showAddForm || !isValidId}
                      style={{
                        padding: '8px 16px',
                        backgroundColor: 'var(--color-danger)',
                        color: 'white',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer',
                        fontSize: '14px',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '6px',
                        opacity: deleting === holiday.id || updating === holiday.id || editingId === holiday.id || showAddForm || !isValidId ? 0.6 : 1
                      }}
                    >
                      {deleting === holiday.id ? '⏳ Удаление...' : '🗑️ Удалить'}
                    </button>
                  </div>
                </>
              )}
            </li>
            )
          })}
        </ul>
      )}
    </div>
  )
}

