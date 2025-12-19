import { ReactElement } from 'react'
import { render, RenderOptions } from '@testing-library/react'
import { MemoryRouter } from 'react-router-dom'

/**
 * Helper функция для рендеринга компонентов с Router контекстом.
 * 
 * @param ui - React компонент для рендеринга
 * @param options - Опции для render и Router
 * @returns Результат render с Router контекстом
 */
export function renderWithRouter(
  ui: ReactElement,
  options?: {
    initialEntries?: string[]
    renderOptions?: Omit<RenderOptions, 'wrapper'>
  }
) {
  const { initialEntries = ['/'], renderOptions } = options || {}

  const Wrapper = ({ children }: { children: React.ReactNode }) => {
    return <MemoryRouter initialEntries={initialEntries}>{children}</MemoryRouter>
  }

  return render(ui, { wrapper: Wrapper, ...renderOptions })
}

// Re-export все из @testing-library/react для удобства
export * from '@testing-library/react'

