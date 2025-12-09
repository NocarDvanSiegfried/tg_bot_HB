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
      const data = await api.getBirthdays()
      setBirthdays(data)
    } catch (error) {
      logger.error('Failed to load birthdays:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      await api.createBirthday(formData)
      setFormData({ full_name: '', company: '', position: '', birth_date: '', comment: '' })
      loadBirthdays()
    } catch (error) {
      logger.error('Failed to create birthday:', error)
    }
  }

  const handleDelete = async (id: number) => {
    if (!confirm('Удалить день рождения?')) return
    try {
      await api.deleteBirthday(id)
      loadBirthdays()
    } catch (error) {
      logger.error('Failed to delete birthday:', error)
    }
  }

  return (
    <div className="panel-section">
      <button className="back-button" onClick={onBack}>🔙 Назад</button>
      <h3>Управление днями рождения</h3>

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
              <div>
                <strong>{bd.full_name}</strong> - {bd.company}, {bd.position}
                <br />
                {bd.birth_date} {bd.comment && `(${bd.comment})`}
              </div>
              <button onClick={() => handleDelete(bd.id)}>Удалить</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

