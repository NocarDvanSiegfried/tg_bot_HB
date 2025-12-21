import { useState } from 'react'
import BirthdayManagement from './BirthdayManagement'
import ResponsibleManagement from './ResponsibleManagement'
import GreetingGenerator from './GreetingGenerator'
import './Panel.css'

type PanelView = 'main' | 'birthdays' | 'responsible' | 'greetings'

export default function Panel() {
  const [currentView, setCurrentView] = useState<PanelView>('main')

  // КРИТИЧНО: В режиме panel переход на календарь архитектурно запрещен
  // Панель и календарь не могут существовать одновременно
  // Пользователь должен закрыть Mini App и открыть через /start для просмотра календаря

  return (
    <div className="panel-container">
      {/* Визуальный заголовок панели управления */}
      <div style={{
        padding: '16px',
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        color: 'white',
        textAlign: 'center',
        marginBottom: '20px',
        borderRadius: '0 0 12px 12px',
        boxShadow: '0 2px 8px rgba(0,0,0,0.1)'
      }}>
        <h1 style={{ margin: 0, fontSize: '24px', fontWeight: 'bold' }}>🎛️ Панель управления</h1>
        <p style={{ margin: '8px 0 0 0', fontSize: '14px', opacity: 0.9 }}>
          Режим управления днями рождения
        </p>
      </div>

      {currentView === 'main' && (
        <div className="panel-main">
          <h2>Меню управления</h2>
          <p className="panel-description">
            Управляйте днями рождения, ответственными и генерируйте поздравления
          </p>
          <div className="panel-buttons">
            <button onClick={() => setCurrentView('birthdays')} className="panel-button">
              🎂 Управление ДР
            </button>
            <button onClick={() => setCurrentView('responsible')} className="panel-button">
              👤 Управление ответственными
            </button>
            <button onClick={() => setCurrentView('greetings')} className="panel-button">
              🎉 Генерация поздравлений
            </button>
            {/* КРИТИЧНО: Кнопка "Вернуться к календарю" удалена
                В режиме panel переход на календарь архитектурно запрещен
                Панель и календарь не могут существовать одновременно
                Пользователь должен закрыть Mini App и открыть через /start для просмотра календаря
            */}
          </div>
        </div>
      )}

      {currentView === 'birthdays' && (
        <BirthdayManagement onBack={() => setCurrentView('main')} />
      )}

      {currentView === 'responsible' && (
        <ResponsibleManagement onBack={() => setCurrentView('main')} />
      )}

      {currentView === 'greetings' && (
        <GreetingGenerator onBack={() => setCurrentView('main')} />
      )}
    </div>
  )
}

