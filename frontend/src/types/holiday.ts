export interface Holiday {
  id: number
  name: string
  day: number
  month: number
  description?: string
  date?: string // Только для API ответов, не используется в логике
}

