import openai
from config import OPENAI_API_KEY, DEFAULT_IMAGE_SIZE, DEFAULT_MODEL
import base64
import os
import time

# 設置OpenAI API密鑰
openai.api_key = OPENAI_API_KEY

async def generate_image(prompt, size=DEFAULT_IMAGE_SIZE, n=1, model=DEFAULT_MODEL):
    """
    使用DALL-E API生成圖像
    
    參數:
        prompt: 用於生成圖像的文本描述
        size: 圖像尺寸 (例如: "1024x1024")
        n: 要生成的圖像數量
        model: 使用的模型 (dall-e-2 或 dall-e-3)
    
    返回:
        包含圖像URL的數據
    """
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size,
            model=model,
            response_format="url"  # 或使用"b64_json"獲取base64編碼的圖像
        )
        
        # 構建回應數據
        result = {
            "created": int(time.time()),
            "data": []
        }
        
        for image_data in response['data']:
            result["data"].append({
                "url": image_data['url'],
                # 添加其他可能需要的數據
                "prompt": prompt,
                "size": size
            })
        
        return result
    except Exception as e:
        # 記錄錯誤並重新拋出
        print(f"DALL-E API 錯誤: {str(e)}")
        raise