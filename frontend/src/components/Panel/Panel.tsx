import { useState } from 'react'
import BirthdayManagement from './BirthdayManagement'
import ResponsibleManagement from './ResponsibleManagement'
import GreetingGenerator from './GreetingGenerator'
import './Panel.css'

type PanelView = 'main' | 'birthdays' | 'responsible' | 'greetings'

export default function Panel() {
  const [currentView, setCurrentView] = useState<PanelView>('main')

  return (
    <div className="panel-container">
      {currentView === 'main' && (
        <div className="panel-main">
          <h2>Панель управления</h2>
          <button onClick={() => setCurrentView('birthdays')}>🎂 Управление ДР</button>
          <button onClick={() => setCurrentView('responsible')}>👤 Управление ответственными</button>
          <button onClick={() => setCurrentView('greetings')}>🎉 Генерация поздравлений</button>
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

