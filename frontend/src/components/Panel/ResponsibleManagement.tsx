import { useState, useEffect } from 'react'
import { api } from '../../services/api'
import { Responsible } from '../../types/responsible'
import { logger } from '../../utils/logger'
import './Panel.css'

interface ResponsibleManagementProps {
  onBack: () => void
}

export default function ResponsibleManagement({ onBack }: ResponsibleManagementProps) {
  const [responsible, setResponsible] = useState<Responsible[]>([])
  const [loading, setLoading] = useState(false)
  const [creating, setCreating] = useState(false)
  const [updating, setUpdating] = useState<number | null>(null)
  const [deleting, setDeleting] = useState<number | null>(null)
  const [editingId, setEditingId] = useState<number | null>(null)
  const [editFormData, setEditFormData] = useState<Partial<Responsible>>({})
  const [error, setError] = useState<string | null>(null)
  const [showAddForm, setShowAddForm] = useState(false)
  const [formData, setFormData] = useState({
    full_name: '',
    company: '',
    position: '',
  })

  useEffect(() => {
    loadResponsible()
  }, [])

  const loadResponsible = async () => {
    setLoading(true)
    try {
      setError(null)
      const data = await api.getResponsible()
      setResponsible(data)
    } catch (error) {
      logger.error('Failed to load responsible:', error)
      setError(error instanceof Error ? error.message : 'Не удалось загрузить список ответственных')
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (creating) return
    
    try {
      setError(null)
      setCreating(true)
      await api.createResponsible(formData)
      setFormData({ full_name: '', company: '', position: '' })
      setShowAddForm(false) // Закрываем форму после успешного добавления
      await loadResponsible()
    } catch (error) {
      logger.error('Failed to create responsible:', error)
      let errorMessage = 'Не удалось создать ответственного'
      if (error instanceof Error) {
        errorMessage = error.message || errorMessage
        if (errorMessage.includes('CORS') || errorMessage.includes('Network')) {
          errorMessage = 'Ошибка сети. Проверьте подключение к интернету.'
        } else if (errorMessage.includes('401') || errorMessage.includes('авторизац')) {
          errorMessage = 'Ошибка авторизации. Пожалуйста, обновите страницу.'
        } else if (errorMessage.includes('422') || errorMessage.includes('валидац')) {
          errorMessage = 'Ошибка валидации данных. Проверьте введенные данные.'
        } else if (errorMessage.includes('500')) {
          errorMessage = 'Ошибка сервера. Пожалуйста, попробуйте позже.'
        }
      }
      setError(errorMessage)
    } finally {
      setCreating(false)
    }
  }

  const handleEdit = (id: number) => {
    logger.info(`[ResponsibleManagement] handleEdit called for id=${id}`)
    const responsibleItem = responsible.find(r => r.id === id)
    if (responsibleItem) {
      logger.info(`[ResponsibleManagement] Found responsible to edit:`, responsibleItem)
      setEditingId(id)
      setEditFormData({
        full_name: responsibleItem.full_name,
        company: responsibleItem.company,
        position: responsibleItem.position,
      })
      setError(null)
      logger.info(`[ResponsibleManagement] Edit form initialized for id=${id}`)
    } else {
      logger.error(`[ResponsibleManagement] Responsible with id=${id} not found`)
      setError(`Ответственный с ID ${id} не найден`)
    }
  }

  const validateEditForm = (): boolean => {
    const validationErrors: string[] = []
    
    if (!editFormData.full_name?.trim()) {
      validationErrors.push('ФИО не может быть пустым')
    } else if (editFormData.full_name.trim().length < 2) {
      validationErrors.push('ФИО должно содержать минимум 2 символа')
    }
    
    if (!editFormData.company?.trim()) {
      validationErrors.push('Компания не может быть пустой')
    }
    
    if (!editFormData.position?.trim()) {
      validationErrors.push('Должность не может быть пустой')
    }
    
    if (validationErrors.length > 0) {
      const errorMsg = validationErrors.length === 1 
        ? validationErrors[0]
        : `Ошибки валидации:\n${validationErrors.map((err, idx) => `${idx + 1}. ${err}`).join('\n')}`
      setError(errorMsg)
      return false
    }
    
    return true
  }

  const handleUpdate = async (id: number) => {
    logger.info(`[ResponsibleManagement] ===== handleUpdate CALLED for id=${id} =====`)
    
    if (updating === id) return
    
    try {
      setError(null)
      
      if (!validateEditForm()) {
        logger.warn('[ResponsibleManagement] Validation failed - NOT sending request')
        return
      }
      
      setUpdating(id)
      logger.info(`[ResponsibleManagement] ===== READY TO SEND PUT REQUEST =====`)
      logger.info(`[ResponsibleManagement] Data:`, JSON.stringify(editFormData))
      
      await api.updateResponsible(id, editFormData)
      
      logger.info(`[ResponsibleManagement] Responsible ${id} updated successfully`)
      
      setEditingId(null)
      setEditFormData({})
      await loadResponsible()
      logger.info(`[ResponsibleManagement] [STATE UPDATE] State updated successfully after update`)
    } catch (error) {
      logger.error(`[ResponsibleManagement] PUT request failed:`, error)
      logger.error(`[ResponsibleManagement] Error details:`, {
        name: error instanceof Error ? error.name : 'Unknown',
        message: error instanceof Error ? error.message : String(error),
        stack: error instanceof Error ? error.stack : undefined
      })
      
      let errorMessage = 'Не удалось обновить ответственного'
      if (error instanceof Error) {
        errorMessage = error.message || errorMessage
        if (errorMessage.includes('CORS') || errorMessage.includes('Network')) {
          errorMessage = 'Ошибка сети. Проверьте подключение к интернету.'
        } else if (errorMessage.includes('401') || errorMessage.includes('авторизац')) {
          errorMessage = 'Ошибка авторизации. Пожалуйста, обновите страницу.'
        } else if (errorMessage.includes('422') || errorMessage.includes('валидац')) {
          errorMessage = 'Ошибка валидации данных. Проверьте введенные данные.'
        } else if (errorMessage.includes('404')) {
          errorMessage = 'Ответственный не найден. Возможно, он был удален.'
        } else if (errorMessage.includes('500')) {
          errorMessage = 'Ошибка сервера. Пожалуйста, попробуйте позже.'
        }
      }
      setError(errorMessage)
    } finally {
      setUpdating(null)
    }
  }

  const handleCancelEdit = () => {
    setEditingId(null)
    setEditFormData({})
    setError(null)
  }

  const handleDelete = async (id: number) => {
    logger.info(`[ResponsibleManagement] ===== handleDelete CALLED for id=${id} =====`)
    
    if (deleting === id) return
    
    if (!confirm('Удалить ответственного?')) {
      logger.info(`[ResponsibleManagement] Delete cancelled for responsible ${id}`)
      return
    }
    
    try {
      setError(null)
      setDeleting(id)
      
      logger.info(`[ResponsibleManagement] ===== READY TO SEND DELETE REQUEST =====`)
      logger.info(`[ResponsibleManagement] Deleting responsible ${id}`)
      
      await api.deleteResponsible(id)
      
      logger.info(`[ResponsibleManagement] Responsible ${id} deleted successfully`)
      await loadResponsible()
      logger.info(`[ResponsibleManagement] [STATE UPDATE] State updated successfully after delete`)
    } catch (error) {
      logger.error(`[ResponsibleManagement] DELETE request failed:`, error)
      logger.error(`[ResponsibleManagement] Error details:`, {
        name: error instanceof Error ? error.name : 'Unknown',
        message: error instanceof Error ? error.message : String(error),
        stack: error instanceof Error ? error.stack : undefined
      })
      
      let errorMessage = 'Не удалось удалить ответственного'
      if (error instanceof Error) {
        errorMessage = error.message || errorMessage
        if (errorMessage.includes('CORS') || errorMessage.includes('Network')) {
          errorMessage = 'Ошибка сети. Проверьте подключение к интернету.'
        } else if (errorMessage.includes('401') || errorMessage.includes('авторизац')) {
          errorMessage = 'Ошибка авторизации. Пожалуйста, обновите страницу.'
        } else if (errorMessage.includes('404')) {
          errorMessage = 'Ответственный не найден. Возможно, он уже был удален.'
        } else if (errorMessage.includes('500')) {
          errorMessage = 'Ошибка сервера. Пожалуйста, попробуйте позже.'
        }
      }
      setError(errorMessage)
    } finally {
      setDeleting(null)
    }
  }

  return (
    <div className="panel-section">
      <button className="back-button" onClick={onBack}>🔙 Назад</button>
      <h3>Управление ответственными лицами</h3>

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
              // При закрытии формы очищаем данные
              setFormData({ full_name: '', company: '', position: '' })
              setError(null)
            }
            setShowAddForm(!showAddForm)
          }}
          style={{
            padding: '12px 20px',
            backgroundColor: '#28a745',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '16px',
            fontWeight: 'bold',
            display: 'flex',
            alignItems: 'center',
            gap: '8px'
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
          value={formData.full_name}
          onChange={(e) => setFormData({ ...formData, full_name: e.target.value })}
          required
          disabled={creating}
        />
        <input
          type="text"
          placeholder="Компания"
          value={formData.company}
          onChange={(e) => setFormData({ ...formData, company: e.target.value })}
          required
          disabled={creating}
        />
        <input
          type="text"
          placeholder="Должность"
          value={formData.position}
          onChange={(e) => setFormData({ ...formData, position: e.target.value })}
          required
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
          {responsible.map((r) => (
            <li key={r.id} className="panel-list-item">
              {editingId === r.id ? (
                <div style={{ width: '100%' }}>
                  <form
                    noValidate
                    onSubmit={async (e) => {
                      e.preventDefault()
                      logger.info(`[ResponsibleManagement] Form submitted for responsible id=${r.id}`)
                      
                      if (!r.id) {
                        logger.error('[ResponsibleManagement] Cannot update: responsible id is missing')
                        setError('Ошибка: ID ответственного не найден')
                        return
                      }
                      
                      await handleUpdate(r.id)
                    }}
                    style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}
                  >
                    <input
                      type="text"
                      placeholder="ФИО"
                      value={editFormData.full_name || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, full_name: e.target.value })}
                      disabled={updating === r.id || showAddForm}
                    />
                    <input
                      type="text"
                      placeholder="Компания"
                      value={editFormData.company || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, company: e.target.value })}
                      disabled={updating === r.id || showAddForm}
                    />
                    <input
                      type="text"
                      placeholder="Должность"
                      value={editFormData.position || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, position: e.target.value })}
                      disabled={updating === r.id || showAddForm}
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
                      <button type="submit" disabled={updating === r.id || showAddForm}>
                        {updating === r.id ? '⏳ Сохранение...' : 'Сохранить'}
                      </button>
                      <button type="button" onClick={handleCancelEdit} disabled={updating === r.id || showAddForm}>
                        Отмена
                      </button>
                    </div>
                  </form>
                </div>
              ) : (
                <>
                  <div>
                    <strong>{r.full_name}</strong> - {r.company}, {r.position}
                  </div>
                  <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                    <button 
                      onClick={() => handleEdit(r.id)}
                      disabled={deleting === r.id || updating !== null || editingId !== null || showAddForm}
                      style={{
                        padding: '8px 16px',
                        backgroundColor: '#007bff',
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
                      onClick={() => handleDelete(r.id)}
                      disabled={deleting === r.id || updating !== null || editingId !== null || showAddForm}
                      style={{
                        padding: '8px 16px',
                        backgroundColor: '#dc3545',
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
                      {deleting === r.id ? '⏳ Удаление...' : '🗑️ Удалить'}
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

