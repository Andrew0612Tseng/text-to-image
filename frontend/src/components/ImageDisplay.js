import React from 'react';
import LoadingSpinner from './LoadingSpinner';
import '../styles/components.css';

function ImageDisplay({ images, isLoading, error }) {
  if (isLoading) {
    return (
      <div className="image-display loading-container">
        <LoadingSpinner />
        <p>正在生成圖像，這可能需要一些時間...</p>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="image-display error-container">
        <div className="error-message">
          <h3>發生錯誤</h3>
          <p>{error}</p>
        </div>
      </div>
    );
  }
  
  if (!images || images.length === 0) {
    return (
      <div className="image-display empty-container">
        <p>輸入提示詞並點擊「生成圖像」按鈕開始生成</p>
      </div>
    );
  }
  
  return (
    <div className="image-display">
      <h2>生成的圖像</h2>
      <div className="image-grid">
        {images.map((image, index) => (
          <div key={index} className="image-card">
            <img src={image.url} alt={`AI生成: ${image.prompt}`} />
            <div className="image-info">
              <p className="image-prompt">{image.prompt}</p>
              <p className="image-meta">大小: {image.size}</p>
              <a 
                href={image.url} 
                download={`generated-image-${index}.png`}
                target="_blank"
                rel="noopener noreferrer"
                className="download-btn"
              >
                下載圖像
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ImageDisplay;