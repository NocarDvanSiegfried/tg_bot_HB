import { useState, useEffect } from 'react'
import { api } from '../../services/api'
import { Birthday } from '../../types/birthday'
import { logger } from '../../utils/logger'
import { API_BASE_URL } from '../../config/api'
import './Panel.css'

interface BirthdayManagementProps {
  onBack: () => void
}

export default function BirthdayManagement({ onBack }: BirthdayManagementProps) {
  const [birthdays, setBirthdays] = useState<Birthday[]>([])
  const [loading, setLoading] = useState(false)
  const [editingId, setEditingId] = useState<number | null>(null)
  const [editFormData, setEditFormData] = useState<Partial<Birthday>>({})
  const [error, setError] = useState<string | null>(null)
  const [formData, setFormData] = useState({
    full_name: '',
    company: '',
    position: '',
    birth_date: '',
    comment: '',
  })

  useEffect(() => {
    loadBirthdays()
  }, [])

  const loadBirthdays = async () => {
    setLoading(true)
    try {
      setError(null)
      const data = await api.getBirthdays()
      setBirthdays(data)
    } catch (error) {
      logger.error('Failed to load birthdays:', error)
      setError(error instanceof Error ? error.message : 'Не удалось загрузить дни рождения')
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      setError(null)
      await api.createBirthday(formData)
      setFormData({ full_name: '', company: '', position: '', birth_date: '', comment: '' })
      loadBirthdays()
    } catch (error) {
      logger.error('Failed to create birthday:', error)
      setError(error instanceof Error ? error.message : 'Не удалось создать день рождения')
    }
  }

  const handleEdit = (id: number) => {
    logger.info(`[BirthdayManagement] handleEdit called for id=${id}`)
    const birthday = birthdays.find(b => b.id === id)
    if (birthday) {
      logger.info(`[BirthdayManagement] Found birthday to edit:`, birthday)
      
      // Нормализация birth_date для input type="date" (формат YYYY-MM-DD)
      let normalizedBirthDate = birthday.birth_date
      if (normalizedBirthDate) {
        // Если дата в формате ISO (с временем), извлечь только дату
        if (normalizedBirthDate.includes('T')) {
          normalizedBirthDate = normalizedBirthDate.split('T')[0]
        }
        // Если дата в другом формате, попытаться преобразовать
        if (!/^\d{4}-\d{2}-\d{2}$/.test(normalizedBirthDate)) {
          logger.warn(`[BirthdayManagement] Invalid birth_date format: ${normalizedBirthDate}, attempting to fix`)
          // Попытка исправить формат
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
      
      setEditingId(id)
      setEditFormData({
        full_name: birthday.full_name,
        company: birthday.company,
        position: birthday.position,
        birth_date: normalizedBirthDate,
        comment: birthday.comment || '',
      })
      setError(null)
      logger.info(`[BirthdayManagement] Edit form initialized for id=${id}`)
    } else {
      logger.error(`[BirthdayManagement] Birthday with id=${id} not found`)
      setError(`День рождения с ID ${id} не найден`)
    }
  }

  const validateEditForm = (): boolean => {
    logger.info('[BirthdayManagement] Starting validation...')
    logger.info('[BirthdayManagement] editFormData:', editFormData)
    
    // Проверка формата birth_date
    if (editFormData.birth_date) {
      const dateRegex = /^\d{4}-\d{2}-\d{2}$/
      if (!dateRegex.test(editFormData.birth_date)) {
        const errorMsg = 'Неверный формат даты. Используйте формат YYYY-MM-DD'
        setError(errorMsg)
        logger.error('[BirthdayManagement] Invalid birth_date format:', editFormData.birth_date)
        return false
      }
    }
    
    // Проверка обязательных полей
    if (!editFormData.full_name?.trim()) {
      setError('ФИО не может быть пустым')
      logger.warn('[BirthdayManagement] Validation failed: full_name is empty')
      return false
    }
    if (!editFormData.company?.trim()) {
      setError('Компания не может быть пустой')
      logger.warn('[BirthdayManagement] Validation failed: company is empty')
      return false
    }
    if (!editFormData.position?.trim()) {
      setError('Должность не может быть пустой')
      logger.warn('[BirthdayManagement] Validation failed: position is empty')
      return false
    }
    if (!editFormData.birth_date) {
      setError('Дата рождения обязательна')
      logger.warn('[BirthdayManagement] Validation failed: birth_date is missing')
      return false
    }
    
    logger.info('[BirthdayManagement] Validation passed')
    return true
  }

  const handleUpdate = async (id: number) => {
    logger.info(`[BirthdayManagement] handleUpdate called for id=${id}`)
    logger.info(`[BirthdayManagement] editFormData:`, editFormData)
    
    try {
      setError(null)
      
      // Валидация обязательных полей
      if (!validateEditForm()) {
        logger.warn('[BirthdayManagement] Validation failed - not sending request')
        return
      }
      
      // Нормализация данных перед отправкой
      const normalizedData = {
        ...editFormData,
        birth_date: editFormData.birth_date || undefined,
        comment: editFormData.comment?.trim() || undefined
      }
      
      // Проверка формата birth_date перед отправкой
      if (normalizedData.birth_date && !/^\d{4}-\d{2}-\d{2}$/.test(normalizedData.birth_date)) {
        const errorMsg = 'Неверный формат даты рождения'
        setError(errorMsg)
        logger.error('[BirthdayManagement] Invalid birth_date format before sending:', normalizedData.birth_date)
        return
      }
      
      // Перед отправкой проверить, что все готово
      logger.info(`[BirthdayManagement] Ready to send PUT request for id=${id}`)
      logger.info(`[BirthdayManagement] URL: ${API_BASE_URL}/api/panel/birthdays/${id}`)
      logger.info('[BirthdayManagement] Sending data:', normalizedData)
      
      // Отправка запроса - БЕЗ дополнительных проверок
      const result = await api.updateBirthday(id, normalizedData)
      
      logger.info(`[BirthdayManagement] Birthday ${id} updated successfully:`, result)
      
      setEditingId(null)
      setEditFormData({})
      loadBirthdays()
    } catch (error) {
      logger.error(`[BirthdayManagement] PUT request failed:`, error)
      logger.error(`[BirthdayManagement] Error details:`, {
        name: error instanceof Error ? error.name : 'Unknown',
        message: error instanceof Error ? error.message : String(error),
        stack: error instanceof Error ? error.stack : undefined
      })
      
      let errorMessage = 'Не удалось обновить день рождения'
      if (error instanceof Error) {
        errorMessage = error.message || errorMessage
      }
      setError(errorMessage)
      throw error // Пробросить ошибку дальше для обработки в onSubmit
    }
  }

  const handleCancelEdit = () => {
    setEditingId(null)
    setEditFormData({})
    setError(null)
  }

  const handleDelete = async (id: number) => {
    logger.info(`[BirthdayManagement] handleDelete called for id=${id}`)
    
    if (!confirm('Удалить день рождения?')) {
      logger.info(`[BirthdayManagement] Delete cancelled for birthday ${id}`)
      return
    }
    
    try {
      setError(null)
      
      logger.info(`[BirthdayManagement] Deleting birthday ${id}`)
      
      await api.deleteBirthday(id)
      
      logger.info(`[BirthdayManagement] Birthday ${id} deleted successfully`)
      
      loadBirthdays()
    } catch (error) {
      logger.error(`[BirthdayManagement] DELETE request failed:`, error)
      logger.error(`[BirthdayManagement] Error details:`, {
        name: error instanceof Error ? error.name : 'Unknown',
        message: error instanceof Error ? error.message : String(error),
        stack: error instanceof Error ? error.stack : undefined
      })
      
      let errorMessage = 'Не удалось удалить день рождения'
      if (error instanceof Error) {
        errorMessage = error.message || errorMessage
      }
      setError(errorMessage)
    }
  }

  return (
    <div className="panel-section">
      <button className="back-button" onClick={onBack}>🔙 Назад</button>
      <h3>Управление днями рождения</h3>

      {error && (
        <div className="error-message" style={{ padding: '10px', marginBottom: '10px', background: '#fee', color: '#c00', borderRadius: '4px' }}>
          ⚠️ {error}
        </div>
      )}

      <form className="panel-form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="ФИО"
          value={formData.full_name}
          onChange={(e) => setFormData({ ...formData, full_name: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Компания"
          value={formData.company}
          onChange={(e) => setFormData({ ...formData, company: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Должность"
          value={formData.position}
          onChange={(e) => setFormData({ ...formData, position: e.target.value })}
          required
        />
        <input
          type="date"
          value={formData.birth_date}
          onChange={(e) => setFormData({ ...formData, birth_date: e.target.value })}
          required
        />
        <textarea
          placeholder="Комментарий (необязательно)"
          value={formData.comment}
          onChange={(e) => setFormData({ ...formData, comment: e.target.value })}
        />
        <button type="submit">Добавить</button>
      </form>

      {loading ? (
        <p>Загрузка...</p>
      ) : (
        <ul className="panel-list">
          {birthdays.map((bd) => (
            <li key={bd.id} className="panel-list-item">
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
                      
                      try {
                        await handleUpdate(bd.id)
                      } catch (error) {
                        logger.error('[BirthdayManagement] Error in form onSubmit:', error)
                      }
                    }}
                    style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}
                  >
                    <input
                      type="text"
                      placeholder="ФИО"
                      value={editFormData.full_name || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, full_name: e.target.value })}
                      required
                    />
                    <input
                      type="text"
                      placeholder="Компания"
                      value={editFormData.company || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, company: e.target.value })}
                      required
                    />
                    <input
                      type="text"
                      placeholder="Должность"
                      value={editFormData.position || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, position: e.target.value })}
                      required
                    />
                    <input
                      type="date"
                      value={editFormData.birth_date || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, birth_date: e.target.value })}
                      required
                    />
                    <textarea
                      placeholder="Комментарий (необязательно)"
                      value={editFormData.comment || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, comment: e.target.value })}
                    />
                    <div style={{ display: 'flex', gap: '10px' }}>
                      <button type="submit">Сохранить</button>
                      <button type="button" onClick={handleCancelEdit}>Отмена</button>
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
                    <div style={{ display: 'flex', gap: '10px' }}>
                      <button onClick={() => handleEdit(bd.id!)}>Редактировать</button>
                      <button 
                        onClick={async () => {
                          try {
                            await handleDelete(bd.id!)
                          } catch (error) {
                            logger.error('[BirthdayManagement] Error in delete button onClick:', error)
                          }
                        }}
                      >
                        Удалить
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

