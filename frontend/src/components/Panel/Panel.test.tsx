import { describe, it, expect, vi, beforeEach } from 'vitest'
import { screen, fireEvent } from '@testing-library/react'
import { renderWithRouter } from '../../test/test-utils'
import Panel from './Panel'

// Мокируем дочерние компоненты
vi.mock('./BirthdayManagement', () => ({
  default: ({ onBack }: { onBack: () => void }) => (
    <div data-testid="birthday-management">
      <button onClick={onBack}>Назад</button>
    </div>
  ),
}))

vi.mock('./ResponsibleManagement', () => ({
  default: ({ onBack }: { onBack: () => void }) => (
    <div data-testid="responsible-management">
      <button onClick={onBack}>Назад</button>
    </div>
  ),
}))

vi.mock('./GreetingGenerator', () => ({
  default: ({ onBack }: { onBack: () => void }) => (
    <div data-testid="greeting-generator">
      <button onClick={onBack}>Назад</button>
    </div>
  ),
}))

describe('Panel', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('should render main panel view by default', () => {
    renderWithRouter(<Panel />)
    
    expect(screen.getByText('Панель управления')).toBeInTheDocument()
    expect(screen.getByText('🎂 Управление ДР')).toBeInTheDocument()
    expect(screen.getByText('👤 Управление ответственными')).toBeInTheDocument()
    expect(screen.getByText('🎉 Генерация поздравлений')).toBeInTheDocument()
  })

  it('should navigate to birthday management view', () => {
    renderWithRouter(<Panel />)
    
    const birthdayButton = screen.getByText('🎂 Управление ДР')
    fireEvent.click(birthdayButton)
    
    expect(screen.getByTestId('birthday-management')).toBeInTheDocument()
    expect(screen.queryByText('Панель управления')).not.toBeInTheDocument()
  })

  it('should navigate to responsible management view', () => {
    renderWithRouter(<Panel />)
    
    const responsibleButton = screen.getByText('👤 Управление ответственными')
    fireEvent.click(responsibleButton)
    
    expect(screen.getByTestId('responsible-management')).toBeInTheDocument()
    expect(screen.queryByText('Панель управления')).not.toBeInTheDocument()
  })

  it('should navigate to greeting generator view', () => {
    renderWithRouter(<Panel />)
    
    const greetingButton = screen.getByText('🎉 Генерация поздравлений')
    fireEvent.click(greetingButton)
    
    expect(screen.getByTestId('greeting-generator')).toBeInTheDocument()
    expect(screen.queryByText('Панель управления')).not.toBeInTheDocument()
  })

  it('should return to main view when back button is clicked', () => {
    renderWithRouter(<Panel />)
    
    // Переходим в birthday management
    const birthdayButton = screen.getByText('🎂 Управление ДР')
    fireEvent.click(birthdayButton)
    
    expect(screen.getByTestId('birthday-management')).toBeInTheDocument()
    
    // Нажимаем назад
    const backButton = screen.getByText('Назад')
    fireEvent.click(backButton)
    
    expect(screen.getByText('Панель управления')).toBeInTheDocument()
    expect(screen.queryByTestId('birthday-management')).not.toBeInTheDocument()
  })

  it('should switch between different views', () => {
    renderWithRouter(<Panel />)
    
    // Переходим в birthday management
    const birthdayButton = screen.getByText('🎂 Управление ДР')
    fireEvent.click(birthdayButton)
    expect(screen.getByTestId('birthday-management')).toBeInTheDocument()
    
    // Возвращаемся назад
    const backButton = screen.getByText('Назад')
    fireEvent.click(backButton)
    
    // Переходим в responsible management
    const responsibleButton = screen.getByText('👤 Управление ответственными')
    fireEvent.click(responsibleButton)
    expect(screen.getByTestId('responsible-management')).toBeInTheDocument()
  })
})

