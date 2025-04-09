const API_BASE_URL = '/api';

export async function generateImage(prompt, size = '1024x1024', n = 1, model = 'dall-e-3') {
  try {
    const response = await fetch(`${API_BASE_URL}/api/images/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        prompt,
        size,
        n,
        model
      }),
    });
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || `API錯誤: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API調用失敗:', error);
    throw error;
  }
}

export async function getModels() {
  try {
    const response = await fetch(`${API_BASE_URL}/api/images/models`);
    
    if (!response.ok) {
      throw new Error(`API錯誤: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('獲取模型列表失敗:', error);
    throw error;
  }
}