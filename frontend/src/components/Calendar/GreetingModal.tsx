import { useState, useEffect } from 'react'
import { api } from '../../services/api'
import { logger } from '../../utils/logger'
import './GreetingModal.css'

interface GreetingModalProps {
  isOpen: boolean
  birthdayId: number
  birthdayName: string
  birthdayCompany: string
  birthdayPosition: string
  onClose: () => void
  onCardCreated?: (cardUrl: string) => void
}

export default function GreetingModal({
  isOpen,
  birthdayId,
  birthdayName,
  birthdayCompany,
  birthdayPosition,
  onClose,
  onCardCreated,
}: GreetingModalProps) {
  const [style, setStyle] = useState<string>('friendly')
  const [length, setLength] = useState<string>('medium')
  const [theme, setTheme] = useState<string>('')
  const [qrUrl, setQrUrl] = useState<string>('')
  const [generating, setGenerating] = useState(false)
  const [creatingCard, setCreatingCard] = useState(false)
  const [greetingText, setGreetingText] = useState<string>('')
  const [cardUrl, setCardUrl] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  // Закрытие по ESC
  useEffect(() => {
    if (!isOpen) return

    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose()
      }
    }

    document.addEventListener('keydown', handleEscape)
    return () => {
      document.removeEventListener('keydown', handleEscape)
    }
  }, [isOpen, onClose])

  // Сброс состояния при закрытии
  useEffect(() => {
    if (!isOpen) {
      setGreetingText('')
      setCardUrl(null)
      setError(null)
      setStyle('friendly')
      setLength('medium')
      setTheme('')
      setQrUrl('')
    }
  }, [isOpen])

  const handleGenerate = async () => {
    setGenerating(true)
    setError(null)
    setGreetingText('')
    setCardUrl(null)

    try {
      const result = await api.generateGreeting(
        birthdayId,
        style,
        length,
        theme || undefined
      )
      setGreetingText(result.greeting)
    } catch (err) {
      logger.error('[GreetingModal] Failed to generate greeting:', err)
      const errorMessage = err instanceof Error ? err.message : 'Не удалось сгенерировать поздравление'
      
      // Улучшаем сообщения об ошибках для пользователя
      let userFriendlyMessage = errorMessage
      if (errorMessage.includes('403') || errorMessage.includes('доступ') || errorMessage.includes('Access denied')) {
        userFriendlyMessage = 'Ошибка авторизации. Пожалуйста, обновите страницу и попробуйте снова.'
      } else if (errorMessage.includes('401') || errorMessage.includes('авторизац')) {
        userFriendlyMessage = 'Ошибка авторизации. Пожалуйста, обновите страницу.'
      } else if (errorMessage.includes('Network') || errorMessage.includes('fetch')) {
        userFriendlyMessage = 'Ошибка подключения. Проверьте интернет-соединение и попробуйте снова.'
      }
      
      setError(userFriendlyMessage)
    } finally {
      setGenerating(false)
    }
  }

  const handleCreateCard = async () => {
    if (!greetingText.trim()) {
      setError('Сначала сгенерируйте поздравление')
      return
    }

    setCreatingCard(true)
    setError(null)
    setCardUrl(null)

    try {
      const blob = await api.createCard(
        birthdayId,
        greetingText,
        qrUrl || undefined
      )
      
      // Создаем URL для превью
      const url = URL.createObjectURL(blob)
      setCardUrl(url)

      // Вызываем callback если передан
      if (onCardCreated) {
        onCardCreated(url)
      }
    } catch (err) {
      logger.error('[GreetingModal] Failed to create card:', err)
      const errorMessage = err instanceof Error ? err.message : 'Не удалось создать открытку'
      
      // Улучшаем сообщения об ошибках для пользователя
      let userFriendlyMessage = errorMessage
      if (errorMessage.includes('403') || errorMessage.includes('доступ') || errorMessage.includes('Access denied')) {
        userFriendlyMessage = 'Ошибка авторизации. Пожалуйста, обновите страницу и попробуйте снова.'
      } else if (errorMessage.includes('401') || errorMessage.includes('авторизац')) {
        userFriendlyMessage = 'Ошибка авторизации. Пожалуйста, обновите страницу.'
      } else if (errorMessage.includes('Network') || errorMessage.includes('fetch')) {
        userFriendlyMessage = 'Ошибка подключения. Проверьте интернет-соединение и попробуйте снова.'
      }
      
      setError(userFriendlyMessage)
    } finally {
      setCreatingCard(false)
    }
  }

  const handleDownload = () => {
    if (!cardUrl) return

    const link = document.createElement('a')
    link.href = cardUrl
    link.download = `greeting-${birthdayName.replace(/\s+/g, '-')}-${Date.now()}.png`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  if (!isOpen) return null

  return (
    <div className="greeting-modal-overlay" onClick={onClose}>
      <div className="greeting-modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="greeting-modal-header">
          <h2>🤖 Генерация поздравления</h2>
          <button className="greeting-modal-close" onClick={onClose} aria-label="Закрыть">
            ✕
          </button>
        </div>

        <div className="greeting-modal-body">
          {/* Информация о сотруднике */}
          <div className="greeting-employee-info">
            <p><strong>Сотрудник:</strong> {birthdayName}</p>
            <p><strong>Компания:</strong> {birthdayCompany}</p>
            <p><strong>Должность:</strong> {birthdayPosition}</p>
          </div>

          {/* Параметры генерации */}
          <div className="greeting-params">
            <div className="greeting-param-group">
              <label htmlFor="greeting-style">Стиль:</label>
              <select
                id="greeting-style"
                value={style}
                onChange={(e) => setStyle(e.target.value)}
                disabled={generating}
              >
                <option value="formal">Официальный</option>
                <option value="friendly">Дружелюбный</option>
                <option value="humorous">Юмористический</option>
                <option value="warm">Тёплый</option>
              </select>
            </div>

            <div className="greeting-param-group">
              <label htmlFor="greeting-length">Длина:</label>
              <select
                id="greeting-length"
                value={length}
                onChange={(e) => setLength(e.target.value)}
                disabled={generating}
              >
                <option value="short">Короткое</option>
                <option value="medium">Среднее</option>
                <option value="long">Длинное</option>
              </select>
            </div>

            <div className="greeting-param-group">
              <label htmlFor="greeting-theme">Тема (необязательно):</label>
              <input
                id="greeting-theme"
                type="text"
                value={theme}
                onChange={(e) => setTheme(e.target.value)}
                placeholder="Например: успех, здоровье, карьера"
                disabled={generating}
              />
            </div>

            <div className="greeting-param-group">
              <label htmlFor="greeting-qr">QR-код URL (необязательно):</label>
              <input
                id="greeting-qr"
                type="url"
                value={qrUrl}
                onChange={(e) => setQrUrl(e.target.value)}
                placeholder="https://example.com"
                disabled={generating || creatingCard}
              />
            </div>
          </div>

          {/* Кнопка генерации */}
          <button
            className="greeting-generate-button"
            onClick={handleGenerate}
            disabled={generating}
          >
            {generating ? '⏳ Генерация...' : '✨ Сгенерировать поздравление'}
          </button>

          {/* Результат генерации */}
          {greetingText && (
            <div className="greeting-result">
              <label htmlFor="greeting-text">Сгенерированное поздравление:</label>
              <textarea
                id="greeting-text"
                value={greetingText}
                onChange={(e) => setGreetingText(e.target.value)}
                rows={6}
                placeholder="Здесь появится сгенерированное поздравление..."
                disabled={creatingCard}
              />
            </div>
          )}

          {/* Кнопка создания открытки */}
          {greetingText && (
            <button
              className="greeting-create-card-button"
              onClick={handleCreateCard}
              disabled={creatingCard || !greetingText.trim()}
            >
              {creatingCard ? '⏳ Создание открытки...' : '🎨 Создать открытку'}
            </button>
          )}

          {/* Превью открытки */}
          {cardUrl && (
            <div className="greeting-card-preview">
              <p><strong>Превью открытки:</strong></p>
              <img src={cardUrl} alt="Превью открытки" className="greeting-card-image" />
              <button
                className="greeting-download-button"
                onClick={handleDownload}
              >
                📥 Скачать открытку
              </button>
            </div>
          )}

          {/* Ошибки */}
          {error && (
            <div className="greeting-error">
              ⚠️ {error}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

