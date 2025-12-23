import { useCRUDManagement } from '../../hooks/useCRUDManagement'
import { api } from '../../services/api'
import { Birthday } from '../../types/birthday'
import { logger } from '../../utils/logger'
import { validateDate } from '../../utils/validation'
import { API_BASE_URL } from '../../config/api'
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
          }
        } catch (e) {
          logger.error(`[BirthdayManagement] Could not normalize birth_date: ${e}`)
        }
      }
    }
    
    return {
      full_name: birthday.full_name,
      company: birthday.company,
      position: birthday.position,
      birth_date: normalizedBirthDate,
      comment: birthday.comment || '',
    }
  }

  // Использование общего хука для CRUD операций
  const {
    items: birthdays,
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

  // Диагностическая информация (специфичная для BirthdayManagement)
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
      <h3>Управление днями рождения</h3>

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
              setFormData({ full_name: '', company: '', position: '', birth_date: '', comment: '' })
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
          <input
            type="date"
            value={(formData.birth_date as string) || ''}
            onChange={(e) => setFormData({ ...formData, birth_date: e.target.value })}
            required
            disabled={creating}
          />
          <textarea
            placeholder="Комментарий (необязательно)"
            value={(formData.comment as string) || ''}
            onChange={(e) => setFormData({ ...formData, comment: e.target.value })}
            disabled={creating}
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
          {birthdays.map((bd, index) => (
            <li key={bd.id ?? `birthday-${index}`} className="panel-list-item">
              {editingId === bd.id ? (
                <div style={{ width: '100%' }}>
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
                    <input
                      type="date"
                      value={(editFormData.birth_date as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, birth_date: e.target.value })}
                      disabled={updating === bd.id || showAddForm}
                    />
                    <textarea
                      placeholder="Комментарий (необязательно)"
                      value={(editFormData.comment as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, comment: e.target.value })}
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
                      <button type="button" onClick={handleCancelEdit} disabled={updating === bd.id || showAddForm}>
                        Отмена
                      </button>
                    </div>
                  </form>
                </div>
              ) : (
                <>
                  <div>
                    <strong>{bd.full_name}</strong> - {bd.company}, {bd.position}
                    <br />
                    {bd.birth_date} {bd.comment && `(${bd.comment})`}
                  </div>
                  <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                    <button 
                      onClick={() => bd.id && handleEdit(bd.id)}
                      disabled={deleting === bd.id || updating === bd.id || editingId === bd.id || showAddForm}
                      style={{
                        padding: '8px 16px',
                        backgroundColor: 'var(--color-primary)',
                        color: 'white',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer',
                        fontSize: '14px',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '6px'
                      }}
                    >
                      ✏️ Редактировать
                    </button>
                    <button 
                      onClick={() => {
                        if (!bd.id) {
                          logger.error('[BirthdayManagement] Cannot delete: birthday id is missing')
                          setError('Ошибка: ID дня рождения не найден')
                          return
                        }
                        handleDelete(bd.id)
                      }}
                      disabled={deleting === bd.id || updating === bd.id || editingId === bd.id || showAddForm}
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
                        gap: '6px'
                      }}
                    >
                      {deleting === bd.id ? '⏳ Удаление...' : '🗑️ Удалить'}
                    </button>
                  </div>
                </>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}
