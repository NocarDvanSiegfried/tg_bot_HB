import { useState, useEffect } from 'react'
import { api } from '../../services/api'
import { Responsible } from '../../types/responsible'
import './Panel.css'

interface ResponsibleManagementProps {
  onBack: () => void
}

export default function ResponsibleManagement({ onBack }: ResponsibleManagementProps) {
  const [responsible, setResponsible] = useState<Responsible[]>([])
  const [loading, setLoading] = useState(false)
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
      const data = await api.getResponsible()
      setResponsible(data)
    } catch (error) {
      logger.error('Failed to load responsible:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      await api.createResponsible(formData)
      setFormData({ full_name: '', company: '', position: '' })
      loadResponsible()
    } catch (error) {
      logger.error('Failed to create responsible:', error)
    }
  }

  const handleDelete = async (id: number) => {
    if (!confirm('Удалить ответственного?')) return
    try {
      await api.deleteResponsible(id)
      loadResponsible()
    } catch (error) {
      logger.error('Failed to delete responsible:', error)
    }
  }

  return (
    <div className="panel-section">
      <button className="back-button" onClick={onBack}>🔙 Назад</button>
      <h3>Управление ответственными лицами</h3>

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
        <button type="submit">Добавить</button>
      </form>

      {loading ? (
        <p>Загрузка...</p>
      ) : (
        <ul className="panel-list">
          {responsible.map((r) => (
            <li key={r.id} className="panel-list-item">
              <div>
                <strong>{r.full_name}</strong> - {r.company}, {r.position}
              </div>
              <button onClick={() => handleDelete(r.id)}>Удалить</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

