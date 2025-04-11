# 🖼️ Text-to-Image Generator

A full-stack project that takes text prompts and generates corresponding images using DALL-E model.

🚀 Deployed on **GCP Cloud Run** with a modern frontend interface.

---

## 🌐 Give it a try!

👉 [Open the Text-to-Image App](https://dalle-frontend-641883752192.asia-east1.run.app/)

---

## 🖼️ Screenshots

### 🔧 GCP Cloud Run Deployment

> Application deployed via Docker on GCP Cloud Run:

![GCP Cloud Run](./png/cloud-run.png)

---

### 💡 UI Demo

> Input your prompt and generate images with one click:

![UI Demo](./png/ui-demo.png)

---

## ⚙️ Features

- ✍️ Text-to-Image generation using a backend LLM API model
- 🎨 Real-time frontend preview
- 🌩️ Cloud-native deployment (GCP Cloud Run + Docker)
- 📦 RESTful API with FastAPI
- ⚛️ Modern frontend (React)

---

## 📦 Tech Stack

- **Backend**: Python, FastAPI, OpenAI API (DALL-E)
- **Frontend**: React (Vite), CSS
- **Cloud**: Docker, GCP Cloud Run, GCR
- **Others**: Nginx, GitLab CI/CD (optional)

---

## 🚀 Getting Started (Local)

### Backend (FastAPI)

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend (React)

```bash
cd frontend
npm install
npm start
```