import { useState } from 'react'
import { api } from '../../services/api'
import './Panel.css'

interface GreetingGeneratorProps {
  onBack: () => void
}

export default function GreetingGenerator({ onBack }: GreetingGeneratorProps) {
  const [mode, setMode] = useState<'select' | 'manual' | 'generate' | 'card'>('select')
  const [birthdayId, setBirthdayId] = useState('')
  const [greetingText, setGreetingText] = useState('')
  const [style, setStyle] = useState('friendly')
  const [length, setLength] = useState('medium')
  const [theme, setTheme] = useState('')
  const [qrUrl, setQrUrl] = useState('')
  const [generatedGreeting, setGeneratedGreeting] = useState('')
  const [cardUrl, setCardUrl] = useState('')

  const handleGenerate = async () => {
    try {
      const result = await api.generateGreeting(
        parseInt(birthdayId),
        style,
        length,
        theme || undefined
      )
      setGeneratedGreeting(result.greeting)
      setGreetingText(result.greeting)
    } catch (error) {
      console.error('Failed to generate greeting:', error)
    }
  }

  const handleCreateCard = async () => {
    try {
      const blob = await api.createCard(
        parseInt(birthdayId),
        greetingText,
        qrUrl || undefined
      )
      const url = URL.createObjectURL(blob)
      setCardUrl(url)
    } catch (error) {
      console.error('Failed to create card:', error)
    }
  }

  return (
    <div className="panel-section">
      <button className="back-button" onClick={onBack}>🔙 Назад</button>
      <h3>Генерация поздравлений и открыток</h3>

      {mode === 'select' && (
        <div>
          <button onClick={() => setMode('manual')}>✏️ Написать вручную</button>
          <button onClick={() => setMode('generate')}>🤖 Сгенерировать через DeepSeek</button>
          <button onClick={() => setMode('card')}>🖼️ Создать открытку</button>
        </div>
      )}

      {mode === 'manual' && (
        <div className="panel-form">
          <input
            type="number"
            placeholder="ID сотрудника"
            value={birthdayId}
            onChange={(e) => setBirthdayId(e.target.value)}
          />
          <textarea
            placeholder="Текст поздравления"
            value={greetingText}
            onChange={(e) => setGreetingText(e.target.value)}
          />
          <button onClick={() => setMode('card')}>Создать открытку</button>
          <button onClick={() => setMode('select')}>Назад</button>
        </div>
      )}

      {mode === 'generate' && (
        <div className="panel-form">
          <input
            type="number"
            placeholder="ID сотрудника"
            value={birthdayId}
            onChange={(e) => setBirthdayId(e.target.value)}
          />
          <select value={style} onChange={(e) => setStyle(e.target.value)}>
            <option value="formal">Официальный</option>
            <option value="friendly">Дружелюбный</option>
            <option value="humorous">Юмористический</option>
            <option value="warm">Теплый</option>
          </select>
          <select value={length} onChange={(e) => setLength(e.target.value)}>
            <option value="short">Короткое</option>
            <option value="medium">Среднее</option>
            <option value="long">Длинное</option>
          </select>
          <input
            type="text"
            placeholder="Тема (необязательно)"
            value={theme}
            onChange={(e) => setTheme(e.target.value)}
          />
          <button onClick={handleGenerate}>Сгенерировать</button>
          {generatedGreeting && (
            <div>
              <p>{generatedGreeting}</p>
              <button onClick={() => setMode('card')}>Создать открытку</button>
            </div>
          )}
          <button onClick={() => setMode('select')}>Назад</button>
        </div>
      )}

      {mode === 'card' && (
        <div className="panel-form">
          <input
            type="number"
            placeholder="ID сотрудника"
            value={birthdayId}
            onChange={(e) => setBirthdayId(e.target.value)}
          />
          <textarea
            placeholder="Текст поздравления"
            value={greetingText}
            onChange={(e) => setGreetingText(e.target.value)}
          />
          <input
            type="url"
            placeholder="URL для QR-кода (необязательно)"
            value={qrUrl}
            onChange={(e) => setQrUrl(e.target.value)}
          />
          <button onClick={handleCreateCard}>Создать открытку</button>
          {cardUrl && (
            <div>
              <img src={cardUrl} alt="Card" style={{ maxWidth: '100%' }} />
            </div>
          )}
          <button onClick={() => setMode('select')}>Назад</button>
        </div>
      )}
    </div>
  )
}

