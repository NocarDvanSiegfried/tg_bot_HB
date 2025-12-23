import { useCRUDManagement } from '../../hooks/useCRUDManagement'
import { api } from '../../services/api'
import { Responsible } from '../../types/responsible'
import { logger } from '../../utils/logger'
import './Panel.css'

interface ResponsibleManagementProps {
  onBack: () => void
}

export default function ResponsibleManagement({ onBack }: ResponsibleManagementProps) {
  // Валидация для Responsible (специфичная логика)
  const validateResponsible = (data: Partial<Responsible>): string[] => {
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
    
    return errors
  }

  // Использование общего хука для CRUD операций
  const {
    items: responsible,
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
  } = useCRUDManagement<Responsible>({
    loadData: api.getResponsible,
    createItem: async (data) => {
      // Преобразуем Partial<Responsible> в Omit<Responsible, 'id'> для API
      const responsibleData: Omit<Responsible, 'id'> = {
        full_name: data.full_name!,
        company: data.company!,
        position: data.position!,
      }
      return api.createResponsible(responsibleData)
    },
    updateItem: api.updateResponsible,
    deleteItem: api.deleteResponsible,
    validateItem: validateResponsible,
    getCreateErrorMessage: () => 'Не удалось создать ответственного',
    getUpdateErrorMessage: () => 'Не удалось обновить ответственного',
    getDeleteErrorMessage: () => 'Не удалось удалить ответственного',
    getLoadErrorMessage: () => 'Не удалось загрузить список ответственных',
    getDeleteConfirmMessage: () => 'Удалить ответственного?',
  })

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
              setFormData({ full_name: '', company: '', position: '' })
              setError(null)
            }
            setShowAddForm(!showAddForm)
          }}
          style={{
            padding: '12px 20px',
            backgroundColor: 'var(--color-success)',
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
                      value={(editFormData.full_name as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, full_name: e.target.value })}
                      disabled={updating === r.id || showAddForm}
                    />
                    <input
                      type="text"
                      placeholder="Компания"
                      value={(editFormData.company as string) || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, company: e.target.value })}
                      disabled={updating === r.id || showAddForm}
                    />
                    <input
                      type="text"
                      placeholder="Должность"
                      value={(editFormData.position as string) || ''}
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
                      onClick={() => handleDelete(r.id)}
                      disabled={deleting === r.id || updating !== null || editingId !== null || showAddForm}
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
