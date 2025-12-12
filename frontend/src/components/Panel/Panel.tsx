import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import BirthdayManagement from './BirthdayManagement'
import ResponsibleManagement from './ResponsibleManagement'
import GreetingGenerator from './GreetingGenerator'
import './Panel.css'

type PanelView = 'main' | 'birthdays' | 'responsible' | 'greetings'

export default function Panel() {
  const [currentView, setCurrentView] = useState<PanelView>('main')
  const navigate = useNavigate()

  const handleBackToCalendar = () => {
    // Переходим на календарь через роутинг
    navigate('/')
  }

  return (
    <div className="panel-container">
      {currentView === 'main' && (
        <div className="panel-main">
          <h2>Панель управления</h2>
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
            <button onClick={handleBackToCalendar} className="panel-button panel-button-secondary">
              📅 Вернуться к календарю
            </button>
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

