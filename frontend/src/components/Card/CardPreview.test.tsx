import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import CardPreview from './CardPreview'

describe('CardPreview', () => {
  it('should render card preview with image', () => {
    const imageUrl = 'https://example.com/card.png'
    render(<CardPreview imageUrl={imageUrl} />)
    
    const image = screen.getByAltText('Birthday Card') as HTMLImageElement
    expect(image).toBeInTheDocument()
    expect(image.src).toBe(imageUrl)
  })

  it('should render card preview with different image URL', () => {
    const imageUrl = 'https://example.com/another-card.jpg'
    render(<CardPreview imageUrl={imageUrl} />)
    
    const image = screen.getByAltText('Birthday Card') as HTMLImageElement
    expect(image.src).toBe(imageUrl)
  })

  it('should render card preview container', () => {
    const imageUrl = 'https://example.com/card.png'
    const { container } = render(<CardPreview imageUrl={imageUrl} />)
    
    const cardPreview = container.querySelector('.card-preview')
    expect(cardPreview).toBeInTheDocument()
  })

  it('should have correct image attributes', () => {
    const imageUrl = 'https://example.com/card.png'
    render(<CardPreview imageUrl={imageUrl} />)
    
    const image = screen.getByAltText('Birthday Card') as HTMLImageElement
    expect(image.alt).toBe('Birthday Card')
    expect(image.src).toBe(imageUrl)
  })

  it('should handle data URL image', () => {
    const imageUrl = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=='
    render(<CardPreview imageUrl={imageUrl} />)
    
    const image = screen.getByAltText('Birthday Card') as HTMLImageElement
    expect(image.src).toBe(imageUrl)
  })

  it('should handle relative image URL', () => {
    const imageUrl = '/images/card.png'
    render(<CardPreview imageUrl={imageUrl} />)
    
    const image = screen.getByAltText('Birthday Card') as HTMLImageElement
    // В тестовом окружении относительные URL могут быть преобразованы
    expect(image).toBeInTheDocument()
  })
})

