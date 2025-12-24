import './NavigationBar.css'

interface NavigationBarProps {
  activeSection: 'calendar' | 'birthdays' | 'holidays'
  onSectionChange: (section: 'calendar' | 'birthdays' | 'holidays') => void
}

export default function NavigationBar({ activeSection, onSectionChange }: NavigationBarProps) {
  return (
    <nav className="navigation-bar">
      <button
        className={`nav-button ${activeSection === 'calendar' ? 'active' : ''}`}
        onClick={() => onSectionChange('calendar')}
        title="Календарь"
      >
        📅 Календарь
      </button>
      <button
        className={`nav-button ${activeSection === 'birthdays' ? 'active' : ''}`}
        onClick={() => onSectionChange('birthdays')}
        title="Дни рождения"
      >
        🎂 Дни рождения
      </button>
      <button
        className={`nav-button ${activeSection === 'holidays' ? 'active' : ''}`}
        onClick={() => onSectionChange('holidays')}
        title="Праздники"
      >
        🎉 Праздники
      </button>
    </nav>
  )
}

