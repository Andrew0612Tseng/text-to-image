import React, { useState, useEffect } from 'react';
import { generateImage, getModels } from '../services/api';
import '../styles/components.css';

function ImageGenerator({ onStartGeneration, onImageGenerated, onError }) {
  const [prompt, setPrompt] = useState('');
  const [size, setSize] = useState('1024x1024');
  const [numImages, setNumImages] = useState(1);
  const [model, setModel] = useState('dall-e-3');
  const [models, setModels] = useState([]);
  
  useEffect(() => {
    // 載入支持的模型
    const loadModels = async () => {
      try {
        const modelsData = await getModels();
        setModels(modelsData.models);
      } catch (error) {
        console.error("載入模型失敗:", error);
        // 預設模型列表，以防API調用失敗
        setModels([
          { id: 'dall-e-3', name: 'DALL-E 3' },
          { id: 'dall-e-2', name: 'DALL-E 2' }
        ]);
      }
    };
    
    loadModels();
  }, []);
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!prompt.trim()) {
      onError("請輸入提示詞");
      return;
    }
    
    onStartGeneration();
    
    try {
      const result = await generateImage(prompt, size, numImages, model);
      onImageGenerated(result.data);
    } catch (error) {
      console.error("生成圖像失敗:", error);
      onError("生成圖像時發生錯誤：" + (error.message || "未知錯誤"));
    }
  };
  
  return (
    <div className="image-generator">
      <h2>創建新圖像</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="prompt">提示詞描述：</label>
          <textarea
            id="prompt"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="描述你想要生成的圖像，例如：'一隻在夕陽下奔跑的狗'"
            rows="4"
            required
          />
        </div>
        
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="size">圖像大小：</label>
            <select
              id="size"
              value={size}
              onChange={(e) => setSize(e.target.value)}
            >
              <option value="1024x1024">1024x1024</option>
              <option value="512x512">512x512</option>
              <option value="256x256">256x256</option>
            </select>
          </div>
          
          <div className="form-group">
            <label htmlFor="numImages">數量：</label>
            <select
              id="numImages"
              value={numImages}
              onChange={(e) => setNumImages(Number(e.target.value))}
            >
              {[1, 2, 3, 4].map(num => (
                <option key={num} value={num}>{num}</option>
              ))}
            </select>
          </div>
          
          <div className="form-group">
            <label htmlFor="model">模型：</label>
            <select
              id="model"
              value={model}
              onChange={(e) => setModel(e.target.value)}
            >
              {models.map(modelOption => (
                <option key={modelOption.id} value={modelOption.id}>
                  {modelOption.name}
                </option>
              ))}
            </select>
          </div>
        </div>
        
        <button type="submit" className="generate-btn">生成圖像</button>
      </form>
    </div>
  );
}

export default ImageGenerator;