import React from 'react';
import '../styles/components.css';

function Header() {
  return (
    <header className="header">
      <div className="header-container">
        <h1>AI 圖像生成器</h1>
        <p>使用DALL-E將您的想法轉化為圖像</p>
      </div>
    </header>
  );
}

export default Header;