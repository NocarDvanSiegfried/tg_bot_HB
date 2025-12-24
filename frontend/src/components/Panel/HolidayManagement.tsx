import { useState, useMemo } from 'react'
import { useCRUDManagement } from '../../hooks/useCRUDManagement'
import { api } from '../../services/api'
import { Holiday } from '../../types/holiday'
import { logger } from '../../utils/logger'
import './Panel.css'

interface HolidayManagementProps {
  onBack: () => void
}

type SortOption = 'date' | 'name' | 'month'

export default function HolidayManagement({ onBack }: HolidayManagementProps) {
  // Валидация для Holiday
  const validateHoliday = (data: any): string[] => {
    const errors: string[] = []
    
    if (!data.name?.trim()) {
      errors.push('Название праздника не может быть пустым')
    } else if (data.name.trim().length < 1) {
      errors.push('Название праздника должно содержать минимум 1 символ')
    } else if (data.name.trim().length > 255) {
      errors.push('Название праздника не может быть длиннее 255 символов')
    }
    
    const dayNum = typeof data.day === 'string' ? parseInt(data.day, 10) : data.day
    const monthNum = typeof data.month === 'string' ? parseInt(data.month, 10) : data.month
    
    if (dayNum === undefined || dayNum === null || isNaN(dayNum) || dayNum < 1 || dayNum > 31) {
      errors.push('День должен быть от 1 до 31')
    }
    
    if (monthNum === undefined || monthNum === null || isNaN(monthNum) || monthNum < 1 || monthNum > 12) {
      errors.push('Месяц должен быть от 1 до 12')
    }
    
    if (dayNum && monthNum && !isNaN(dayNum) && !isNaN(monthNum)) {
      const daysInMonth = new Date(2000, monthNum, 0).getDate()
      if (dayNum > daysInMonth) {
        errors.push(`День ${dayNum} недопустим для месяца ${monthNum}. Максимальный день: ${daysInMonth}`)
      }
    }
    
    if (data.description && data.description.length > 1000) {
      errors.push('Комментарий не может быть длиннее 1000 символов')
    }
    
    return errors
  }

  // Нормализация даты для редактирования
  const normalizeHoliday = (holiday: Holiday): any => {
    try {
      let day: number | undefined
      let month: number | undefined
      
      if (holiday.day !== undefined && holiday.month !== undefined) {
        day = holiday.day
        month = holiday.month
      } else if (holiday.date) {
        const dateStr = holiday.date.includes('T') ? holiday.date.split('T')[0] : holiday.date
        const dateMatch = dateStr.match(/^(\d{4})-(\d{2})-(\d{2})$/)
        
        if (dateMatch) {
          month = parseInt(dateMatch[2], 10)
          day = parseInt(dateMatch[3], 10)
        } else {
          const date = new Date(holiday.date)
          if (!isNaN(date.getTime())) {
            month = date.getMonth() + 1
            day = date.getDate()
          }
        }
      }
      
      return {
        name: holiday.name || '',
        day: day ? String(day) : '',
        month: month ? String(month) : '',
        description: holiday.description || '',
      }
    } catch (error) {
      logger.error(`[HolidayManagement] Error in normalizeHoliday:`, error)
      return {
        name: holiday.name || '',
        day: '',
        month: '',
        description: holiday.description || '',
      }
    }
  }

  // Состояния для поиска, сортировки и фильтрации
  const [searchQuery, setSearchQuery] = useState('')
  const [sortOption, setSortOption] = useState<SortOption>('date')
  const [filterMonth, setFilterMonth] = useState<number | ''>('')

  // Использование общего хука для CRUD операций
  const {
    items: allHolidays,
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
      const dayStr = data.day as string | number | undefined
      const monthStr = data.month as string | number | undefined
      
      const dayNum = typeof dayStr === 'string' ? parseInt(dayStr, 10) : (typeof dayStr === 'number' ? dayStr : undefined)
      const monthNum = typeof monthStr === 'string' ? parseInt(monthStr, 10) : (typeof monthStr === 'number' ? monthStr : undefined)
      
      if (dayNum === undefined || isNaN(dayNum) || monthNum === undefined || isNaN(monthNum)) {
        throw new Error('День и месяц должны быть числами')
      }
      
      const holidayData = {
        name: data.name!,
        day: dayNum,
        month: monthNum,
        description: data.description,
      }
      return api.createHoliday(holidayData)
    },
    updateItem: async (id: number, data: any) => {
      const updateData: any = {}
      if (data.name !== undefined) updateData.name = data.name
      if (data.day !== undefined) {
        const dayStr = data.day as string | number | undefined
        const dayNum = typeof dayStr === 'string' ? parseInt(dayStr, 10) : (dayStr as number | undefined)
        if (dayNum !== undefined && !isNaN(dayNum)) updateData.day = dayNum
      }
      if (data.month !== undefined) {
        const monthStr = data.month as string | number | undefined
        const monthNum = typeof monthStr === 'string' ? parseInt(monthStr, 10) : (monthStr as number | undefined)
        if (monthNum !== undefined && !isNaN(monthNum)) updateData.month = monthNum
      }
      if (data.description !== undefined) updateData.description = data.description
      return api.updateHoliday(id, updateData)
    },
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

  // Фильтрация, поиск и сортировка
  const processedHolidays = useMemo(() => {
    let filtered = [...allHolidays]

    // Поиск по названию
    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase().trim()
      filtered = filtered.filter(h => 
        h.name.toLowerCase().includes(query) ||
        (h.description && h.description.toLowerCase().includes(query))
      )
    }

    // Фильтр по месяцу
    if (filterMonth !== '') {
      filtered = filtered.filter(h => {
        const month = h.month || (h.date ? new Date(h.date).getMonth() + 1 : 0)
        return month === filterMonth
      })
    }

    // Сортировка
    filtered.sort((a, b) => {
      if (sortOption === 'name') {
        return a.name.localeCompare(b.name, 'ru')
      } else if (sortOption === 'month') {
        const monthA = a.month || (a.date ? new Date(a.date).getMonth() + 1 : 0)
        const monthB = b.month || (b.date ? new Date(b.date).getMonth() + 1 : 0)
        if (monthA !== monthB) return monthA - monthB
        const dayA = a.day || (a.date ? new Date(a.date).getDate() : 0)
        const dayB = b.day || (b.date ? new Date(b.date).getDate() : 0)
        return dayA - dayB
      } else { // 'date' - по дате (месяц, затем день)
        const monthA = a.month || (a.date ? new Date(a.date).getMonth() + 1 : 0)
        const monthB = b.month || (b.date ? new Date(b.date).getMonth() + 1 : 0)
        if (monthA !== monthB) return monthA - monthB
        const dayA = a.day || (a.date ? new Date(a.date).getDate() : 0)
        const dayB = b.day || (b.date ? new Date(b.date).getDate() : 0)
        return dayA - dayB
      }
    })

    return filtered
  }, [allHolidays, searchQuery, sortOption, filterMonth])

  // Группировка по месяцам
  const groupedHolidays = useMemo(() => {
    const groups: Record<number, Holiday[]> = {}
    
    processedHolidays.forEach(holiday => {
      const month = holiday.month || (holiday.date ? new Date(holiday.date).getMonth() + 1 : 0)
      if (!groups[month]) {
        groups[month] = []
      }
      groups[month].push(holiday)
    })
    
    return groups
  }, [processedHolidays])

  const monthNames = [
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
  ]

  return (
    <div className="holiday-management">
      <button className="back-button" onClick={onBack}>🔙 Назад</button>
      
      <h2 className="holiday-management-title">🎉 Профессиональные праздники</h2>

      {error && (
        <div className="error-message" style={{ whiteSpace: 'pre-line' }}>
          ⚠️ {error}
        </div>
      )}

      {/* Панель управления: поиск, сортировка, фильтр */}
      <div className="holiday-controls-panel">
        <input
          type="text"
          className="holiday-search-input"
          placeholder="🔍 Поиск по названию..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        <select
          className="holiday-sort-select"
          value={sortOption}
          onChange={(e) => setSortOption(e.target.value as SortOption)}
        >
          <option value="date">📅 По дате</option>
          <option value="month">📆 По месяцам</option>
          <option value="name">🔤 По алфавиту</option>
        </select>
        <select
          className="holiday-filter-select"
          value={filterMonth}
          onChange={(e) => setFilterMonth(e.target.value === '' ? '' : parseInt(e.target.value, 10))}
        >
          <option value="">Все месяцы</option>
          {[1,2,3,4,5,6,7,8,9,10,11,12].map(m => (
            <option key={m} value={m}>
              {monthNames[m - 1]}
            </option>
          ))}
        </select>
      </div>

      {/* Счетчик результатов */}
      {(searchQuery || filterMonth !== '' || sortOption !== 'date') && (
        <div className="holiday-results-count">
          Найдено: {processedHolidays.length} из {allHolidays.length}
        </div>
      )}

      {/* Кнопка добавления */}
      <div className="holiday-add-button-container">
        {!showAddForm && (
          <button
            type="button"
            className="holiday-add-button"
            onClick={() => {
              setFormData({ name: '', day: '' as any, month: '' as any, description: '' })
              setError(null)
              setShowAddForm(true)
            }}
            disabled={creating || editingId !== null}
          >
            ➕ Добавить праздник
          </button>
        )}
      </div>

      {/* Форма добавления */}
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
          <div className="holiday-date-inputs">
            <div>
              <label>Месяц:</label>
              <select
                value={(formData.month !== undefined && formData.month !== null) ? String(formData.month) : ''}
                onChange={(e) => setFormData({ ...formData, month: (e.target.value || '') as any })}
                required
                disabled={creating}
              >
                <option value="">Выберите месяц</option>
                {[1,2,3,4,5,6,7,8,9,10,11,12].map(m => (
                  <option key={m} value={m}>
                    {monthNames[m - 1]}
                  </option>
                ))}
              </select>
            </div>
            <div>
              <label>День:</label>
              <input
                type="number"
                min="1"
                max="31"
                placeholder="День"
                value={String(formData.day || '')}
                onChange={(e) => setFormData({ ...formData, day: (e.target.value || '') as any })}
                required
                disabled={creating}
              />
            </div>
          </div>
          <small className="holiday-hint">
            ℹ️ Праздник будет ежегодным
          </small>
          <textarea
            placeholder="Комментарий (необязательно)"
            value={(formData.description as string) || ''}
            onChange={(e) => setFormData({ ...formData, description: e.target.value })}
            disabled={creating}
            maxLength={1000}
          />
          <div className="form-actions">
            <button 
              type="button" 
              className="form-cancel-button"
              onClick={() => {
                setShowAddForm(false)
                setFormData({ name: '', day: '' as any, month: '' as any, description: '' })
                setError(null)
              }}
              disabled={creating}
            >
              Отменить
            </button>
            <button type="submit" className="form-submit-button" disabled={creating}>
              {creating ? '⏳ Добавление...' : '💾 Добавить'}
            </button>
          </div>
        </form>
      )}

      {/* Список праздников */}
      {loading ? (
        <p>Загрузка...</p>
      ) : processedHolidays.length === 0 ? (
        <div className="panel-empty-state">
          {allHolidays.length === 0 
            ? 'Нет праздников. Добавьте первый праздник!'
            : 'Праздники не найдены по заданным критериям.'}
        </div>
      ) : sortOption === 'month' ? (
        // Группировка по месяцам
        <div className="holiday-groups">
          {Object.keys(groupedHolidays)
            .map(Number)
            .sort((a, b) => a - b)
            .map(month => (
              <div key={month} className="holiday-month-group">
                <h3 className="holiday-month-title">{monthNames[month - 1]}</h3>
                <ul className="holiday-list">
                  {groupedHolidays[month].map((holiday, index) => {
                    const isValidId = holiday.id != null && typeof holiday.id === 'number' && !isNaN(holiday.id) && holiday.id > 0
                    const isEditing = isValidId && editingId !== null && editingId === holiday.id
                    
                    return (
                      <li key={holiday.id ?? `holiday-${index}`} className="holiday-card">
                        {isEditing ? (
                          <div className="holiday-edit-form">
                            <form
                              noValidate
                              onSubmit={async (e) => {
                                e.preventDefault()
                                if (!holiday.id) {
                                  setError('Ошибка: ID праздника не найден')
                                  return
                                }
                                await handleUpdate(holiday.id)
                              }}
                            >
                              <input
                                type="text"
                                placeholder="Название праздника"
                                value={(editFormData.name as string) || ''}
                                onChange={(e) => setEditFormData({ ...editFormData, name: e.target.value })}
                                disabled={updating === holiday.id || showAddForm}
                                maxLength={255}
                              />
                              <div className="holiday-date-inputs">
                                <div>
                                  <label>Месяц:</label>
                                  <select
                                    value={String(editFormData.month || '')}
                                    onChange={(e) => setEditFormData({ ...editFormData, month: (e.target.value || '') as any })}
                                    disabled={updating === holiday.id || showAddForm}
                                  >
                                    <option value="">Выберите месяц</option>
                                    {[1,2,3,4,5,6,7,8,9,10,11,12].map(m => (
                                      <option key={m} value={m}>
                                        {monthNames[m - 1]}
                                      </option>
                                    ))}
                                  </select>
                                </div>
                                <div>
                                  <label>День:</label>
                                  <input
                                    type="number"
                                    min="1"
                                    max="31"
                                    placeholder="День"
                                    value={String(editFormData.day || '')}
                                    onChange={(e) => setEditFormData({ ...editFormData, day: (e.target.value || '') as any })}
                                    disabled={updating === holiday.id || showAddForm}
                                  />
                                </div>
                              </div>
                              <textarea
                                placeholder="Комментарий (необязательно)"
                                value={(editFormData.description as string) || ''}
                                onChange={(e) => setEditFormData({ ...editFormData, description: e.target.value })}
                                disabled={updating === holiday.id || showAddForm}
                                maxLength={1000}
                              />
                              <div className="holiday-form-actions">
                                <button type="button" onClick={handleCancelEdit} disabled={updating === holiday.id || showAddForm}>
                                  Отменить
                                </button>
                                <button type="submit" disabled={updating === holiday.id || showAddForm}>
                                  {updating === holiday.id ? '⏳ Сохранение...' : '💾 Сохранить'}
                                </button>
                              </div>
                            </form>
                          </div>
                        ) : (
                          <div className="holiday-card-content">
                            <div className="holiday-card-header">
                              <strong className="holiday-name">{holiday.name}</strong>
                              <span className="holiday-date">
                                {holiday.day && holiday.month 
                                  ? `${String(holiday.day).padStart(2, '0')}.${String(holiday.month).padStart(2, '0')}`
                                  : holiday.date || 'Дата не указана'}
                              </span>
                            </div>
                            {holiday.description && (
                              <p className="holiday-description">{holiday.description}</p>
                            )}
                            <div className="holiday-card-actions">
                              <button
                                className="holiday-edit-button"
                                onClick={() => {
                                  if (!holiday.id || holiday.id === 0) {
                                    setError('Ошибка: ID праздника не найден')
                                    return
                                  }
                                  handleEdit(holiday.id)
                                }}
                                disabled={deleting === holiday.id || updating === holiday.id || showAddForm || !isValidId}
                              >
                                ✏️ Редактировать
                              </button>
                              <button
                                className="holiday-delete-button"
                                onClick={() => {
                                  if (!holiday.id || holiday.id === 0) {
                                    setError('Ошибка: ID праздника не найден')
                                    return
                                  }
                                  handleDelete(holiday.id)
                                }}
                                disabled={deleting === holiday.id || updating === holiday.id || showAddForm || !isValidId}
                              >
                                {deleting === holiday.id ? '⏳ Удаление...' : '🗑️ Удалить'}
                              </button>
                            </div>
                          </div>
                        )}
                      </li>
                    )
                  })}
                </ul>
              </div>
            ))}
        </div>
      ) : (
        // Обычный список (без группировки)
        <ul className="holiday-list">
          {processedHolidays.map((holiday, index) => {
            const isValidId = holiday.id != null && typeof holiday.id === 'number' && !isNaN(holiday.id) && holiday.id > 0
            const isEditing = isValidId && editingId !== null && editingId === holiday.id
            
            return (
              <li key={holiday.id ?? `holiday-${index}`} className="holiday-card">
                {isEditing ? (
                  <div className="holiday-edit-form">
                    <form
                      noValidate
                      onSubmit={async (e) => {
                        e.preventDefault()
                        if (!holiday.id) {
                          setError('Ошибка: ID праздника не найден')
                          return
                        }
                        await handleUpdate(holiday.id)
                      }}
                    >
                      <input
                        type="text"
                        placeholder="Название праздника"
                        value={(editFormData.name as string) || ''}
                        onChange={(e) => setEditFormData({ ...editFormData, name: e.target.value })}
                        disabled={updating === holiday.id || showAddForm}
                        maxLength={255}
                      />
                      <div className="holiday-date-inputs">
                        <div>
                          <label>Месяц:</label>
                          <select
                            value={String(editFormData.month || '')}
                            onChange={(e) => setEditFormData({ ...editFormData, month: (e.target.value || '') as any })}
                            disabled={updating === holiday.id || showAddForm}
                          >
                            <option value="">Выберите месяц</option>
                            {[1,2,3,4,5,6,7,8,9,10,11,12].map(m => (
                              <option key={m} value={m}>
                                {monthNames[m - 1]}
                              </option>
                            ))}
                          </select>
                        </div>
                        <div>
                          <label>День:</label>
                          <input
                            type="number"
                            min="1"
                            max="31"
                            placeholder="День"
                            value={String(editFormData.day || '')}
                            onChange={(e) => setEditFormData({ ...editFormData, day: (e.target.value || '') as any })}
                            disabled={updating === holiday.id || showAddForm}
                          />
                        </div>
                      </div>
                      <textarea
                        placeholder="Комментарий (необязательно)"
                        value={(editFormData.description as string) || ''}
                        onChange={(e) => setEditFormData({ ...editFormData, description: e.target.value })}
                        disabled={updating === holiday.id || showAddForm}
                        maxLength={1000}
                      />
                      <div className="holiday-form-actions">
                        <button type="button" onClick={handleCancelEdit} disabled={updating === holiday.id || showAddForm}>
                          Отменить
                        </button>
                        <button type="submit" disabled={updating === holiday.id || showAddForm}>
                          {updating === holiday.id ? '⏳ Сохранение...' : '💾 Сохранить'}
                        </button>
                      </div>
                    </form>
                  </div>
                ) : (
                  <div className="holiday-card-content">
                    <div className="holiday-card-header">
                      <strong className="holiday-name">{holiday.name}</strong>
                      <span className="holiday-date">
                        {holiday.day && holiday.month 
                          ? `${String(holiday.day).padStart(2, '0')}.${String(holiday.month).padStart(2, '0')}`
                          : holiday.date || 'Дата не указана'}
                      </span>
                    </div>
                    {holiday.description && (
                      <p className="holiday-description">{holiday.description}</p>
                    )}
                    <div className="holiday-card-actions">
                      <button
                        className="holiday-edit-button"
                        onClick={() => {
                          if (!holiday.id || holiday.id === 0) {
                            setError('Ошибка: ID праздника не найден')
                            return
                          }
                          handleEdit(holiday.id)
                        }}
                        disabled={deleting === holiday.id || updating === holiday.id || editingId === holiday.id || showAddForm || !isValidId}
                      >
                        ✏️ Редактировать
                      </button>
                      <button
                        className="holiday-delete-button"
                        onClick={() => {
                          if (!holiday.id || holiday.id === 0) {
                            setError('Ошибка: ID праздника не найден')
                            return
                          }
                          handleDelete(holiday.id)
                        }}
                        disabled={deleting === holiday.id || updating === holiday.id || editingId === holiday.id || showAddForm || !isValidId}
                      >
                        {deleting === holiday.id ? '⏳ Удаление...' : '🗑️ Удалить'}
                      </button>
                    </div>
                  </div>
                )}
              </li>
            )
          })}
        </ul>
      )}
    </div>
  )
}
