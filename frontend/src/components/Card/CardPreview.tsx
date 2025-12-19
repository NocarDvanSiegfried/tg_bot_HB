import { memo } from 'react'
import './CardPreview.css'

interface CardPreviewProps {
  imageUrl: string
}

function CardPreview({ imageUrl }: CardPreviewProps) {
  return (
    <div className="card-preview">
      <img src={imageUrl} alt="Birthday Card" />
    </div>
  )
}

// Мемоизация компонента для оптимизации рендеринга
export default memo(CardPreview)

