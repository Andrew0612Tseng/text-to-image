import requests
import json
import os
import base64
import time
from urllib.request import urlretrieve

# 測試配置
BASE_URL = "http://localhost:8000"  # API 服務URL
OUTPUT_DIR = "test_output"  # 保存生成圖像的目錄

# 確保輸出目錄存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

def test_health_check():
    """測試API健康狀況"""
    print("\n=== 測試健康檢查端點 ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'
    return True

def test_generate_image(prompt, size="1024x1024", n=1):
    """測試圖像生成API"""
    print(f"\n=== 測試圖像生成 ===")
    print(f"提示詞: '{prompt}'")
    
    # 準備請求數據
    payload = {
        "prompt": prompt,
        "size": size,
        "n": n,
        "model": "dall-e-3"  # 或 "dall-e-2"
    }
    
    # 發送請求
    start_time = time.time()
    response = requests.post(
        f"{BASE_URL}/api/images/generate", 
        json=payload
    )
    elapsed_time = time.time() - start_time
    
    print(f"狀態碼: {response.status_code}")
    print(f"處理時間: {elapsed_time:.2f} 秒")
    
    # 檢查回應
    if response.status_code != 200:
        print(f"錯誤: {response.text}")
        return False
    
    # 處理並保存圖像
    result = response.json()
    print(f"生成了 {len(result['data'])} 張圖像")
    
    # 下載並保存每張圖像
    for i, img_data in enumerate(result['data']):
        image_url = img_data['url']
        timestamp = int(time.time())
        filename = f"{OUTPUT_DIR}/generated_{timestamp}_{i+1}.png"
        
        # 下載圖像
        try:
            urlretrieve(image_url, filename)
            print(f"圖像已保存至: {filename}")
        except Exception as e:
            print(f"下載圖像失敗: {str(e)}")
    
    return True

def test_models_endpoint():
    """測試可用模型端點"""
    print("\n=== 測試可用模型端點 ===")
    response = requests.get(f"{BASE_URL}/api/images/models")
    print(f"狀態碼: {response.status_code}")
    print(f"回應: {response.json()}")
    assert response.status_code == 200
    assert 'models' in response.json()
    return True

def main():
    """執行所有測試"""
    print("開始API測試...\n")
    
    # 執行健康檢查測試
    health_ok = test_health_check()
    if not health_ok:
        print("健康檢查失敗，終止測試")
        return
    
    # 測試模型端點
    models_ok = test_models_endpoint()
    if not models_ok:
        print("模型端點測試失敗")
    
    # 測試圖像生成 - 可以嘗試不同的提示詞
    test_prompts = [
        "一隻可愛的灰色貓咪在窗台上看著窗外的鳥",
        "科技風格的未來城市夜景，霓虹燈和高樓大廈"
    ]
    
    for prompt in test_prompts:
        test_generate_image(prompt)
    
    print("\n所有測試完成!")

if __name__ == "__main__":
    main()