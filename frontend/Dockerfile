# 使用Node.js作為構建環境
FROM node:20-alpine as build

# 設置工作目錄
WORKDIR /app

# 複製package.json和package-lock.json
COPY package*.json ./

# 安裝依賴
RUN npm ci

# 複製所有源代碼
COPY . .

# 構建應用
RUN npm run build

# 使用Nginx作為生產服務器
FROM nginx:stable-alpine

# 複製構建產物到Nginx
COPY --from=build /app/build /usr/share/nginx/html

# 創建一個健康檢查文件
RUN echo "OK" > /usr/share/nginx/html/health

# 複製Nginx template配置
COPY nginx.template.conf /etc/nginx/templates/default.conf.template

# 設定使用 template 引擎來讀取 PORT
ENV PORT=8080
EXPOSE 8080

# 啟動Nginx
CMD ["sh", "-c", "envsubst '$$PORT' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]