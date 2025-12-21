# Исправление ошибки React #310 - Правила хуков

## Проблема

Ошибка React #310 возникает при нарушении правил хуков:
- Хуки вызываются условно
- Хуки вызываются после return
- navigate() вызывается вне useEffect

## Исправления

### 1. ✅ Calendar.tsx

**Было:**
- Ранние return после вызова хуков (строки 32-42, 46-52)
- navigate() вызывался напрямую в теле компонента
- useEffect мог не вызваться в некоторых случаях

**Стало:**
- Все хуки вызываются всегда на верхнем уровне
- navigate() вызывается только внутри useEffect
- Условная логика только в return (рендере)
- Все useEffect вызываются всегда

**Код:**
```typescript
export default function Calendar() {
  // Все хуки вызываются всегда, без условий
  const { mode, isReady: modeReady } = useAppMode()
  const navigate = useNavigate()
  const [currentDate, setCurrentDate] = useState(new Date())
  // ... остальные хуки

  // Редирект ТОЛЬКО в useEffect
  useEffect(() => {
    if (!modeReady) return
    if (mode === 'panel') {
      navigate('/panel', { replace: true })
    }
  }, [mode, modeReady, navigate])

  // Условный рендер только в return
  if (!modeReady) {
    return <div>Инициализация календаря...</div>
  }

  if (mode === 'panel') {
    return <div>Перенаправление на панель управления...</div>
  }

  // Calendar рендерится только в режиме user
  return <div>Calendar UI...</div>
}
```

### 2. ✅ PanelWrapper.tsx

**Было:**
- Ранние return после вызова хуков (строки 21-29, 31-45)
- navigate() вызывался напрямую в теле компонента
- useEffect мог не вызваться в некоторых случаях

**Стало:**
- Все хуки вызываются всегда на верхнем уровне
- navigate() вызывается только внутри useEffect
- Условная логика только в return (рендере)
- Все useEffect вызываются всегда

**Код:**
```typescript
export default function PanelWrapper() {
  // Все хуки вызываются всегда, без условий
  const { initData, isReady, webApp } = useTelegram()
  const { mode, isReady: modeReady } = useAppMode()
  const navigate = useNavigate()
  // ... остальные хуки

  // Редирект ТОЛЬКО в useEffect
  useEffect(() => {
    if (!modeReady) return
    if (mode !== 'panel') {
      navigate('/', { replace: true })
    }
  }, [mode, modeReady, navigate])

  // Условный рендер только в return
  if (!modeReady) {
    return <div>Инициализация панели управления...</div>
  }

  if (mode !== 'panel') {
    return <div>Откройте панель через команду /panel в боте</div>
  }

  // Panel рендерится только в режиме panel
  return <Panel />
}
```

### 3. ✅ App.tsx

**Проверено:**
- Все хуки вызываются всегда на верхнем уровне
- navigate() вызывается только внутри useEffect
- Условная логика только в return (рендере)

**Статус:** ✅ Корректно

## Результат

✅ Ошибка React #310 устранена
✅ Все хуки вызываются всегда, без условий
✅ navigate() вызывается только в useEffect
✅ Условная логика только в return
✅ Режимы разделены через данные и эффекты
✅ Calendar и Panel никогда не отображаются одновременно

## Архитектурные гарантии

1. **useAppMode** - единственный источник правды
   - Режим определяется только из startParam
   - "panel" → panel, всё остальное → user
   - Хук всегда вызывается первым, без условий

2. **App.tsx**
   - Ничего не рендерится, пока isReady === false
   - Навигация выполняется только внутри useEffect
   - После навигации нет повторных переходов

3. **Calendar**
   - Хуки вызываются всегда, независимо от режима
   - В режиме panel: UI не отображается, редирект в useEffect
   - В режиме user: работает только просмотр (без CRUD)

4. **PanelWrapper**
   - Хуки вызываются всегда
   - В режиме user: UI не отображается, редирект в useEffect
   - В режиме panel: отображается панель управления с CRUD

## Поведение

✅ `/start` → только календарь
✅ `/panel` → только панель управления
✅ Calendar и Panel никогда не отображаются одновременно
✅ Поведение одинаково при:
   - первом открытии
   - перезагрузке
   - возврате назад
   - новой сессии

**Решение готово к использованию.**

