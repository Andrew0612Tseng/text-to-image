import React, { useState } from 'react';
import Header from './components/Header';
import ImageGenerator from './components/ImageGenerator';
import ImageDisplay from './components/ImageDisplay';
import './styles/index.css';

function App() {
  const [generatedImages, setGeneratedImages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  
  const handleImageGenerated = (images) => {
    setGeneratedImages(images);
    setIsLoading(false);
  };
  
  return (
    <div className="app-container">
      <Header />
      <main className="main-content">
        <ImageGenerator 
          onStartGeneration={() => {
            setIsLoading(true);
            setError(null);
          }}
          onImageGenerated={handleImageGenerated}
          onError={(errorMsg) => {
            setError(errorMsg);
            setIsLoading(false);
          }}
        />
        <ImageDisplay 
          images={generatedImages} 
          isLoading={isLoading}
          error={error}
        />
      </main>
      <footer className="footer">
        <p>Text-to-Image 生成器 &copy; {new Date().getFullYear()}</p>
      </footer>
    </div>
  );
}

export default App;