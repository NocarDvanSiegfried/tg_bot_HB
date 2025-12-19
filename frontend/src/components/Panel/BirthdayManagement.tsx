import { useState, useEffect, useRef } from 'react'
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
  const isMountedRef = useRef(true)

  useEffect(() => {
    isMountedRef.current = true
    loadBirthdays()
    return () => {
      isMountedRef.current = false
    }
  }, [])

  const loadBirthdays = async () => {
    setLoading(true)
    try {
      setError(null)
      const data = await api.getBirthdays()
      // Проверяем, что компонент всё ещё смонтирован перед обновлением состояния
      if (isMountedRef.current) {
        setBirthdays(data)
      }
    } catch (error) {
      logger.error('Failed to load birthdays:', error)
      // Проверяем, что компонент всё ещё смонтирован перед обновлением состояния
      if (isMountedRef.current) {
        setError(error instanceof Error ? error.message : 'Не удалось загрузить дни рождения')
      }
    } finally {
      // Проверяем, что компонент всё ещё смонтирован перед обновлением состояния
      if (isMountedRef.current) {
        setLoading(false)
      }
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
    logger.info('[BirthdayManagement] ===== Starting validation =====')
    logger.info('[BirthdayManagement] editFormData:', JSON.stringify(editFormData))
    
    // Проверка формата birth_date с детальным логированием
    if (editFormData.birth_date) {
      const dateRegex = /^\d{4}-\d{2}-\d{2}$/
      if (!dateRegex.test(editFormData.birth_date)) {
        const errorMsg = 'Неверный формат даты. Используйте формат YYYY-MM-DD'
        logger.error('[BirthdayManagement] Validation failed: Invalid birth_date format', {
          value: editFormData.birth_date,
          expectedFormat: 'YYYY-MM-DD'
        })
        setError(errorMsg)
        return false
      }
      logger.info('[BirthdayManagement] ✓ birth_date format is valid')
    } else {
      logger.warn('[BirthdayManagement] Validation failed: birth_date is missing')
      setError('Дата рождения обязательна')
      return false
    }
    
    // Проверка обязательных полей с детальным логированием
    if (!editFormData.full_name?.trim()) {
      logger.warn('[BirthdayManagement] Validation failed: full_name is empty')
      setError('ФИО не может быть пустым')
      return false
    }
    logger.info('[BirthdayManagement] ✓ full_name is valid')
    
    if (!editFormData.company?.trim()) {
      logger.warn('[BirthdayManagement] Validation failed: company is empty')
      setError('Компания не может быть пустой')
      return false
    }
    logger.info('[BirthdayManagement] ✓ company is valid')
    
    if (!editFormData.position?.trim()) {
      logger.warn('[BirthdayManagement] Validation failed: position is empty')
      setError('Должность не может быть пустой')
      return false
    }
    logger.info('[BirthdayManagement] ✓ position is valid')
    
    logger.info('[BirthdayManagement] ===== Validation PASSED =====')
    return true
  }

  const handleUpdate = async (id: number) => {
    logger.info(`[BirthdayManagement] ===== handleUpdate CALLED for id=${id} =====`)
    logger.info(`[BirthdayManagement] editFormData:`, JSON.stringify(editFormData))
    
    try {
      setError(null)
      
      // Валидация обязательных полей
      if (!validateEditForm()) {
        logger.warn('[BirthdayManagement] Validation failed - NOT sending request')
        return
      }
      
      // Нормализация данных перед отправкой
      const normalizedData = {
        ...editFormData,
        birth_date: editFormData.birth_date || undefined,
        comment: editFormData.comment?.trim() || undefined
      }
      
      // Проверка формата birth_date перед отправкой
      if (normalizedData.birth_date) {
        // Проверяем формат YYYY-MM-DD через регулярное выражение
        if (!/^\d{4}-\d{2}-\d{2}$/.test(normalizedData.birth_date)) {
          const errorMsg = 'Неверный формат даты рождения. Используйте формат YYYY-MM-DD'
          setError(errorMsg)
          logger.error('[BirthdayManagement] Invalid birth_date format before sending:', normalizedData.birth_date)
          return
        }
        
        // Парсим дату и проверяем, что она валидна
        const dateObj = new Date(normalizedData.birth_date + 'T00:00:00')
        if (isNaN(dateObj.getTime())) {
          const errorMsg = 'Неверная дата рождения. Проверьте правильность введённой даты'
          setError(errorMsg)
          logger.error('[BirthdayManagement] Invalid birth_date (NaN) before sending:', normalizedData.birth_date)
          return
        }
        
        // Проверяем, что дата не в будущем (опционально, но логично для дня рождения)
        const today = new Date()
        today.setHours(0, 0, 0, 0)
        if (dateObj > today) {
          const errorMsg = 'Дата рождения не может быть в будущем'
          setError(errorMsg)
          logger.error('[BirthdayManagement] Birth date is in the future:', normalizedData.birth_date)
          return
        }
      }
      
      // Дополнительная проверка наличия всех обязательных полей перед отправкой
      if (!normalizedData.full_name || !normalizedData.company || !normalizedData.position || !normalizedData.birth_date) {
        const missingFields = []
        if (!normalizedData.full_name) missingFields.push('ФИО')
        if (!normalizedData.company) missingFields.push('Компания')
        if (!normalizedData.position) missingFields.push('Должность')
        if (!normalizedData.birth_date) missingFields.push('Дата рождения')
        
        const errorMsg = `Отсутствуют обязательные поля: ${missingFields.join(', ')}`
        setError(errorMsg)
        logger.warn(`[BirthdayManagement] Missing required fields before sending: ${missingFields.join(', ')}`)
        logger.warn(`[BirthdayManagement] normalizedData:`, JSON.stringify(normalizedData))
        return
      }
      
      logger.info(`[BirthdayManagement] ===== READY TO SEND PUT REQUEST =====`)
      logger.info(`[BirthdayManagement] URL: ${API_BASE_URL}/api/panel/birthdays/${id}`)
      logger.info(`[BirthdayManagement] Method: PUT`)
      logger.info(`[BirthdayManagement] Data:`, JSON.stringify(normalizedData))
      
      // Отправка запроса
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
      // Ошибка уже обработана и отображена, не пробрасываем дальше
    }
  }

  const handleCancelEdit = () => {
    setEditingId(null)
    setEditFormData({})
    setError(null)
  }

  const handleDelete = async (id: number) => {
    logger.info(`[BirthdayManagement] ===== handleDelete CALLED for id=${id} =====`)
    
    if (!confirm('Удалить день рождения?')) {
      logger.info(`[BirthdayManagement] Delete cancelled for birthday ${id}`)
      return
    }
    
    try {
      setError(null)
      
      logger.info(`[BirthdayManagement] ===== READY TO SEND DELETE REQUEST =====`)
      logger.info(`[BirthdayManagement] URL: ${API_BASE_URL}/api/panel/birthdays/${id}`)
      logger.info(`[BirthdayManagement] Method: DELETE`)
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
                      
                      // handleUpdate уже обрабатывает ошибки и отображает их через setError
                      await handleUpdate(bd.id)
                    }}
                    style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}
                  >
                    <input
                      type="text"
                      placeholder="ФИО"
                      value={editFormData.full_name || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, full_name: e.target.value })}
                    />
                    <input
                      type="text"
                      placeholder="Компания"
                      value={editFormData.company || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, company: e.target.value })}
                    />
                    <input
                      type="text"
                      placeholder="Должность"
                      value={editFormData.position || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, position: e.target.value })}
                    />
                    <input
                      type="date"
                      value={editFormData.birth_date || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, birth_date: e.target.value })}
                    />
                    <textarea
                      placeholder="Комментарий (необязательно)"
                      value={editFormData.comment || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, comment: e.target.value })}
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
                        fontWeight: 'bold'
                      }}>
                        {error}
                      </div>
                    )}
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
                      <button onClick={() => bd.id && handleEdit(bd.id)}>Редактировать</button>
                      <button 
                        onClick={() => {
                          if (!bd.id) {
                            logger.error('[BirthdayManagement] Cannot delete: birthday id is missing')
                            setError('Ошибка: ID дня рождения не найден')
                            return
                          }
                          // handleDelete уже обрабатывает ошибки и отображает их через setError
                          handleDelete(bd.id)
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

