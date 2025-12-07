import { useState } from 'react'
import { api } from '../../services/api'
import './SearchBar.css'

interface SearchBarProps {
  onSelect: (id: number, type: string) => void
}

export default function SearchBar({ onSelect }: SearchBarProps) {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<Array<{ type: string; id: number; full_name: string; company: string; position: string }>>([])
  const [loading, setLoading] = useState(false)

  const handleSearch = async () => {
    if (!query.trim()) return

    setLoading(true)
    try {
      const data = await api.searchPeople(query)
      setResults(data)
    } catch (error) {
      console.error('Search failed:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Поиск по ФИО, компании, должности..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
      />
      <button onClick={handleSearch}>Поиск</button>

      {loading && <p>Поиск...</p>}

      {results.length > 0 && (
        <ul className="search-results">
          {results.map((result) => (
            <li key={`${result.type}-${result.id}`} onClick={() => onSelect(result.id, result.type)}>
              <strong>{result.full_name}</strong> - {result.company}, {result.position}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

