# 📝 Full Stack Blog App

A full-stack blog application built with **Django (backend)** and **React (frontend)**.

## 🔧 Tech Stack

| Layer     | Technology            |
|-----------|------------------------|
| Frontend  | React, Axios, React Router |
| Backend   | Django, Django REST Framework |
| Auth      | JWT (via djoser)      |
| Database  | SQLite (default)      |

---

## ✨ Features

- 🔐 JWT Authentication (Login / Register)
- 📝 Create, Read, Update, Delete blog posts
- 👤 Posts linked to authors (Django `User` model)
- 🧾 Secure API endpoints with token protection
- 💡 Clean and minimal UI with routing

---

## 🚀 How to Run Locally

### 🛠 Backend (Django)

```bash
cd blog-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

### 🛠 Frontend (React)

```bash
cd blog-frontend
npm install
npm start


