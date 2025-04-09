import os
import base64
from pathlib import Path

def ensure_directory(directory_path):
    """確保目錄存在，如果不存在則創建它"""
    Path(directory_path).mkdir(parents=True, exist_ok=True)

def save_base64_image(base64_string, output_path):
    """將base64編碼的圖像保存為文件"""
    ensure_directory(os.path.dirname(output_path))
    
    # 移除可能的base64前綴
    if ',' in base64_string:
        base64_string = base64_string.split(',')[1]
    
    # 解碼並保存圖像
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(base64_string))
    
    return output_path
