FROM python:3.11-slim

WORKDIR /app

# 安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式代碼
COPY . .

# 設置環境變量
ENV PORT=8000
# 注意：OPENAI_API_KEY 應該通過環境變量或密鑰管理系統提供，不要硬編碼

# 暴露端口
EXPOSE 8000

# 啟動應用
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]