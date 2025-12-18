import { useState, useEffect } from 'react'
import { api } from '../../services/api'
import { Birthday } from '../../types/birthday'
import { logger } from '../../utils/logger'
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
    const birthday = birthdays.find(b => b.id === id)
    if (birthday) {
      setEditingId(id)
      setEditFormData({
        full_name: birthday.full_name,
        company: birthday.company,
        position: birthday.position,
        birth_date: birthday.birth_date,
        comment: birthday.comment || '',
      })
      setError(null)
    }
  }

  const handleUpdate = async (id: number) => {
    try {
      setError(null)
      await api.updateBirthday(id, editFormData)
      setEditingId(null)
      setEditFormData({})
      loadBirthdays()
    } catch (error) {
      logger.error('Failed to update birthday:', error)
      setError(error instanceof Error ? error.message : 'Не удалось обновить день рождения')
    }
  }

  const handleCancelEdit = () => {
    setEditingId(null)
    setEditFormData({})
    setError(null)
  }

  const handleDelete = async (id: number) => {
    if (!confirm('Удалить день рождения?')) return
    try {
      setError(null)
      await api.deleteBirthday(id)
      loadBirthdays()
    } catch (error) {
      logger.error('Failed to delete birthday:', error)
      setError(error instanceof Error ? error.message : 'Не удалось удалить день рождения')
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
                    onSubmit={(e) => {
                      e.preventDefault()
                      handleUpdate(bd.id!)
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
                    <button onClick={() => handleDelete(bd.id!)}>Удалить</button>
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

