import { useEffect, useState, useMemo } from 'react'
import { useCRUDManagement } from '../../hooks/useCRUDManagement'
import { api } from '../../services/api'
import { Birthday } from '../../types/birthday'
import { logger } from '../../utils/logger'
import { validateDate } from '../../utils/validation'
import { API_BASE_URL } from '../../config/api'
import BirthdayDateInput from '../DatePicker/BirthdayDateInput'
import './Panel.css'

interface BirthdayManagementProps {
  onBack: () => void
}

export default function BirthdayManagement({ onBack }: BirthdayManagementProps) {
  // Валидация для Birthday (специфичная логика)
  const validateBirthday = (data: Partial<Birthday>): string[] => {
    const errors: string[] = []
    
    if (!data.full_name?.trim()) {
      errors.push('ФИО не может быть пустым')
    } else if (data.full_name.trim().length < 2) {
      errors.push('ФИО должно содержать минимум 2 символа')
    }
    
    if (!data.company?.trim()) {
      errors.push('Компания не может быть пустой')
    }
    
    if (!data.position?.trim()) {
      errors.push('Должность не может быть пустой')
    }
    
    // Проверка даты рождения с использованием утилиты
    if (data.birth_date) {
      const dateValidation = validateDate(data.birth_date)
      if (!dateValidation.isValid) {
        errors.push(...dateValidation.errors)
      }
    } else {
      errors.push('Дата рождения обязательна')
    }
    
    // Проверка длины комментария
    if (data.comment && data.comment.length > 1000) {
      errors.push('Комментарий не может быть длиннее 1000 символов')
    }
    
    return errors
  }

  // Нормализация даты для редактирования (специфичная логика)
  const normalizeBirthday = (birthday: Birthday): Partial<Birthday> => {
    try {
      let normalizedBirthDate = birthday.birth_date
      if (normalizedBirthDate) {
        // Если дата в формате ISO (с временем), извлечь только дату
        if (normalizedBirthDate.includes('T')) {
          normalizedBirthDate = normalizedBirthDate.split('T')[0]
        }
        // Если дата в другом формате, попытаться преобразовать
        if (!/^\d{4}-\d{2}-\d{2}$/.test(normalizedBirthDate)) {
          logger.warn(`[BirthdayManagement] Invalid birth_date format: ${normalizedBirthDate}, attempting to fix`)
          try {
            const date = new Date(normalizedBirthDate)
            if (!isNaN(date.getTime())) {
              normalizedBirthDate = date.toISOString().split('T')[0]
            } else {
              logger.error(`[BirthdayManagement] Could not parse birth_date: ${normalizedBirthDate}`)
              normalizedBirthDate = '' // Fallback to empty string
            }
          } catch (e) {
            logger.error(`[BirthdayManagement] Error normalizing birth_date: ${e}`)
            normalizedBirthDate = '' // Fallback to empty string
          }
        }
      }
      
      return {
        full_name: birthday.full_name || '',
        company: birthday.company || '',
        position: birthday.position || '',
        birth_date: normalizedBirthDate || '',
        comment: birthday.comment || '',
        responsible: birthday.responsible || '',
      }
    } catch (error) {
      logger.error(`[BirthdayManagement] Error in normalizeBirthday:`, error)
      // Возвращаем безопасные значения по умолчанию
      return {
        full_name: birthday.full_name || '',
        company: birthday.company || '',
        position: birthday.position || '',
        birth_date: birthday.birth_date || '',
        comment: birthday.comment || '',
        responsible: birthday.responsible || '',
      }
    }
  }

  // Состояния для поиска и фильтров
  const [searchQuery, setSearchQuery] = useState('')
  const [filterMonth, setFilterMonth] = useState<number | ''>('')
  
  // Состояние для ошибок даты в формах
  const [dateError, setDateError] = useState<string | null>(null)

  // Использование общего хука для CRUD операций
  const {
    items: allBirthdays,
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
  } = useCRUDManagement<Birthday>({
    loadData: api.getBirthdays,
    createItem: async (data) => {
      // Преобразуем Partial<Birthday> в Omit<Birthday, 'id'> для API
      const birthdayData: Omit<Birthday, 'id'> = {
        full_name: data.full_name!,
        company: data.company!,
        position: data.position!,
        birth_date: data.birth_date!,
        comment: data.comment,
        responsible: data.responsible,
      }
      return api.createBirthday(birthdayData)
    },
    updateItem: api.updateBirthday,
    deleteItem: api.deleteBirthday,
    validateItem: validateBirthday,
    normalizeItem: normalizeBirthday,
    getCreateErrorMessage: () => 'Не удалось создать день рождения',
    getUpdateErrorMessage: () => 'Не удалось обновить день рождения',
    getDeleteErrorMessage: () => 'Не удалось удалить день рождения',
    getLoadErrorMessage: () => 'Не удалось загрузить дни рождения',
    getDeleteConfirmMessage: (birthday) => 
      `Вы уверены, что хотите удалить день рождения "${birthday.full_name}${birthday.company ? ` (${birthday.company})` : ''}"?\n\nЭто действие нельзя отменить.`,
    useMountedRef: true,
  })

  // Фильтрация и поиск
  const birthdays = useMemo(() => {
    let filtered = [...allBirthdays]

    // Поиск по имени, компании, должности
    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase().trim()
      filtered = filtered.filter(bd => 
        bd.full_name.toLowerCase().includes(query) ||
        bd.company.toLowerCase().includes(query) ||
        bd.position.toLowerCase().includes(query)
      )
    }

    // Фильтр по месяцу
    if (filterMonth !== '') {
      filtered = filtered.filter(bd => {
        const birthDate = new Date(bd.birth_date)
        return birthDate.getMonth() + 1 === filterMonth
      })
    }

    return filtered
  }, [allBirthdays, searchQuery, filterMonth])

  // Диагностика изменений editingId (только в dev режиме)
  useEffect(() => {
    if (import.meta.env.DEV) {
      logger.info(`[BirthdayManagement] editingId changed to: ${editingId}`)
    }
  }, [editingId])

  // Диагностическая информация (специфичная для BirthdayManagement)
  const diagnosticInfo = {
    apiUrl: API_BASE_URL,
    hasInitData: typeof window !== 'undefined' && !!window.Telegram?.WebApp?.initData,
    initDataLength: typeof window !== 'undefined' && window.Telegram?.WebApp?.initData 
      ? window.Telegram.WebApp.initData.length 
      : 0,
  }

  return (
    <div className="birthday-management">
      <button className="back-button" onClick={onBack}>🔙 Назад</button>
      
      <h2 className="birthday-management-title">Управление днями рождения</h2>

      {/* Диагностическая информация (только в dev режиме) */}
      {import.meta.env.DEV && (
        <div className="diagnostic-info">
          <strong>🔍 Диагностика:</strong><br/>
          API URL: {diagnosticInfo.apiUrl}<br/>
          InitData: {diagnosticInfo.hasInitData ? `✅ (${diagnosticInfo.initDataLength} символов)` : '❌ отсутствует'}
        </div>
      )}

      {error && (
        <div className="error-message" style={{ whiteSpace: 'pre-line' }}>
          ⚠️ {error}
        </div>
      )}

      {/* Панель управления: поиск и фильтр в одной строке */}
      <div className="birthday-controls-panel">
        <input
          type="text"
          className="birthday-search-input"
          placeholder="🔍 Поиск по имени, компании, должности..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <select
          className="birthday-filter-select"
          value={filterMonth}
          onChange={(e) => setFilterMonth(e.target.value === '' ? '' : parseInt(e.target.value, 10))}
        >
          <option value="">Все месяцы</option>
          {[1,2,3,4,5,6,7,8,9,10,11,12].map(m => (
            <option key={m} value={m}>
              {new Date(2000, m-1, 1).toLocaleString('ru', { month: 'long' })}
            </option>
          ))}
        </select>
      </div>

      {/* Счетчик результатов */}
      {searchQuery || filterMonth !== '' ? (
        <div className="birthday-results-count">
          Найдено: {birthdays.length} из {allBirthdays.length}
        </div>
      ) : null}

      {/* Кнопка добавления */}
      {!showAddForm && (
        <div className="birthday-add-button-container">
          <button
            type="button"
            className="birthday-add-button"
            onClick={() => {
              setFormData({ full_name: '', company: '', position: '', birth_date: '', comment: '', responsible: '' })
              setError(null)
              setDateError(null)
              setShowAddForm(true)
            }}
            disabled={creating || editingId !== null}
          >
            ➕ Добавить день рождения
          </button>
        </div>
      )}

      {showAddForm && (
        <form className="panel-form" onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="ФИО"
            value={(formData.full_name as string) || ''}
            onChange={(e) => setFormData({ ...formData, full_name: e.target.value })}
            required
            disabled={creating}
          />
          <input
            type="text"
            placeholder="Компания"
            value={(formData.company as string) || ''}
            onChange={(e) => setFormData({ ...formData, company: e.target.value })}
            required
            disabled={creating}
          />
          <input
            type="text"
            placeholder="Должность"
            value={(formData.position as string) || ''}
            onChange={(e) => setFormData({ ...formData, position: e.target.value })}
            required
            disabled={creating}
          />
          <BirthdayDateInput
            value={(formData.birth_date as string) || ''}
            onChange={(date) => {
              setFormData({ ...formData, birth_date: date })
              // Очищаем ошибку при изменении даты
              if (dateError) setDateError(null)
              // Валидируем дату в реальном времени
              if (date) {
                const validation = validateDate(date)
                if (!validation.isValid) {
                  setDateError(validation.errors[0])
                } else {
                  setDateError(null)
                }
              } else {
                setDateError(null)
              }
            }}
            disabled={creating}
            error={dateError || (error && error.includes('дата') ? error : undefined)}
          />
          <textarea
            placeholder="Комментарий (необязательно)"
            value={(formData.comment as string) || ''}
            onChange={(e) => setFormData({ ...formData, comment: e.target.value })}
            disabled={creating}
          />
          <input
            type="text"
            placeholder="Ответственное лицо (необязательно)"
            value={(formData.responsible as string) || ''}
            onChange={(e) => setFormData({ ...formData, responsible: e.target.value })}
            disabled={creating}
          />
          <div className="form-actions">
            <button 
              type="button" 
              className="form-cancel-button"
              onClick={() => {
                setShowAddForm(false)
                setFormData({ full_name: '', company: '', position: '', birth_date: '', comment: '', responsible: '' })
                setError(null)
                setDateError(null)
              }}
              disabled={creating}
            >
              Отменить
            </button>
            <button type="submit" className="form-submit-button" disabled={creating}>
              {creating ? '⏳ Добавление...' : 'Добавить'}
            </button>
          </div>
        </form>
      )}

      {loading ? (
        <p>Загрузка...</p>
      ) : (
        <ul className="panel-list">
          {birthdays.map((bd, index) => {
            // Проверка валидности id
            const isValidId = bd.id != null && typeof bd.id === 'number' && !isNaN(bd.id)
            const isEditing = isValidId && editingId !== null && editingId === bd.id
            
            if (import.meta.env.DEV) {
              logger.info(`[BirthdayManagement] Rendering birthday id=${bd.id}, editingId=${editingId}, isValidId=${isValidId}, isEditing=${isEditing}`)
            }
            return (
            <li key={bd.id ?? `birthday-${index}`} className="birthday-card">
              {isEditing ? (
                <div style={{ width: '100%' }}>
                  {!editFormData.full_name && !editFormData.company && !editFormData.position ? (
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
                        logger.info(`[BirthdayManagement] Form submitted for birthday id=${bd.id}`)
                        
                        if (!bd.id) {
                          logger.error('[BirthdayManagement] Cannot update: birthday id is missing')
                          setError('Ошибка: ID дня рождения не найден')
                          return
                        }
                        
                        await handleUpdate(bd.id)
                      }}
                      style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}
                    >
                    <input
                      type="text"
                      placeholder="ФИО"
                      value={(editFormData.full_name as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, full_name: e.target.value })}
                      disabled={updating === bd.id || showAddForm}
                    />
                    <input
                      type="text"
                      placeholder="Компания"
                      value={(editFormData.company as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, company: e.target.value })}
                      disabled={updating === bd.id || showAddForm}
                    />
                    <input
                      type="text"
                      placeholder="Должность"
                      value={(editFormData.position as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, position: e.target.value })}
                      disabled={updating === bd.id || showAddForm}
                    />
                    <BirthdayDateInput
                      value={(editFormData.birth_date as string) || ''}
                      onChange={(date) => {
                        setEditFormData({ ...editFormData, birth_date: date })
                        // Очищаем ошибку при изменении даты
                        if (dateError) setDateError(null)
                        // Валидируем дату в реальном времени
                        if (date) {
                          const validation = validateDate(date)
                          if (!validation.isValid) {
                            setDateError(validation.errors[0])
                          } else {
                            setDateError(null)
                          }
                        } else {
                          setDateError(null)
                        }
                      }}
                      disabled={updating === bd.id || showAddForm}
                      error={dateError || (error && error.includes('дата') ? error : undefined)}
                    />
                    <textarea
                      placeholder="Комментарий (необязательно)"
                      value={(editFormData.comment as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, comment: e.target.value })}
                      disabled={updating === bd.id || showAddForm}
                    />
                    <input
                      type="text"
                      placeholder="Ответственное лицо (необязательно)"
                      value={(editFormData.responsible as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, responsible: e.target.value })}
                      disabled={updating === bd.id || showAddForm}
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
                      <button type="submit" disabled={updating === bd.id || showAddForm}>
                        {updating === bd.id ? '⏳ Сохранение...' : 'Сохранить'}
                      </button>
                      <button 
                        type="button" 
                        onClick={() => {
                          handleCancelEdit()
                          setDateError(null) // Очищаем ошибки при отмене
                        }} 
                        disabled={updating === bd.id || showAddForm}
                      >
                        Отмена
                      </button>
                    </div>
                  </form>
                  )}
                </div>
              ) : (
                <>
                  <div className="birthday-card-content">
                    <div className="birthday-card-name">{bd.full_name}</div>
                    <div className="birthday-card-company-position">{bd.company}, {bd.position}</div>
                    <div className="birthday-card-date">{bd.birth_date}</div>
                    {bd.comment && (
                      <div className="birthday-card-comment">{bd.comment}</div>
                    )}
                    {bd.responsible && (
                      <div className="birthday-card-responsible">
                        <span>👤</span>
                        <span><strong>Ответственный:</strong> {bd.responsible}</span>
                      </div>
                    )}
                  </div>
                  <div className="birthday-card-actions">
                    <button 
                      className="birthday-action-button birthday-edit-button"
                      onClick={() => {
                        if (!bd.id) {
                          logger.error('[BirthdayManagement] Cannot edit: birthday id is missing', bd)
                          setError('Ошибка: ID дня рождения не найден')
                          return
                        }
                        logger.info(`[BirthdayManagement] Edit button clicked for id=${bd.id}, current editingId=${editingId}`)
                        handleEdit(bd.id)
                        logger.info(`[BirthdayManagement] After handleEdit call, editingId should be=${bd.id}`)
                      }}
                      disabled={deleting === bd.id || updating === bd.id || showAddForm}
                    >
                      ✏️ Редактировать
                    </button>
                    <button 
                      className="birthday-action-button birthday-delete-button"
                      onClick={() => {
                        if (!bd.id) {
                          logger.error('[BirthdayManagement] Cannot delete: birthday id is missing')
                          setError('Ошибка: ID дня рождения не найден')
                          return
                        }
                        handleDelete(bd.id)
                      }}
                      disabled={deleting === bd.id || updating === bd.id || showAddForm}
                    >
                      {deleting === bd.id ? '⏳ Удаление...' : '🗑️ Удалить'}
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
