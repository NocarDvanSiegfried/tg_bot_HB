import './CardPreview.css'

interface CardPreviewProps {
  imageUrl: string
}

export default function CardPreview({ imageUrl }: CardPreviewProps) {
  return (
    <div className="card-preview">
      <img src={imageUrl} alt="Birthday Card" />
    </div>
  )
}

