# 🛍️ FastAPI Shop

This is a demo REST API application built with **FastAPI**, simulating a simple online store (categories, products, carts).

---

## 🧩 Tech stack
- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **Uvicorn**
- **Docker & Docker Compose**
- **Pydantic Settings**

---

## ⚡ Quick start
```bash
git clone https://github.com/yourname/fastapi-shop.git
cd fastapi-shop
docker compose up --build
```
---

## 🚀 Run the project locally

### 1. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate    # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create an `.env` file
Create a file named `.env` in the project root (you can copy it from `.env.example` if provided).

### 4. Run the server
```bash
uvicorn app.main:app --reload
```

The API documentation will be available at:  
👉 http://127.0.0.1:8000/api/docs

### 5. (Optional) Seed initial data
```bash
python seed_data.py
```

---

## 🐳 Run with Docker

1. Make sure Docker and Docker Compose are installed.  
2. From the project root, run:
```bash
docker compose up --build
```
3. Open in your browser:  
👉 http://127.0.0.1:8000

---

## ⚙️ Developer commands (Makefile)

| Command | Description |
|---|---|
| `make install` | Install dependencies |
| `make run` | Run the app locally |
| `make seed` | Seed the database |
| `make lint` | Lint the code (ruff) |
| `make docker-up` | Run the app with Docker |

> ⚠️ **Note for Windows users:**  
> The `make` utility is not available by default on Windows.  
> You can either install it via [Git Bash](https://git-scm.com/downloads) or [Chocolatey](https://chocolatey.org/install)  
> (command: `choco install make`),  
> or run the equivalent commands manually:
> - `pip install -r requirements.txt`
> - `uvicorn app.main:app --reload`
> - `python seed_data.py`
> - `docker compose up --build`
---
## 📦 Project structure (extracted from repository)

```
app/
 ├─ __init__.py
 ├─ config.py         # Settings (pydantic)
 ├─ database.py       # SQLAlchemy engine & session, Base
 ├─ main.py           # FastAPI app (lifespan, routes, middleware, static)
 ├─ models/
 │   ├─ __init__.py
 │   ├─ category.py
 │   └─ product.py
 ├─ repositories/
 │   ├─ __init__.py
 │   ├─ base.py
 │   ├─ category.py
 │   └─ product.py
 ├─ routes/
 │   ├─ __init__.py
 │   ├─ cart.py
 │   ├─ category.py
 │   └─ product.py
 ├─ schemas/
 │   ├─ __init__.py
 │   ├─ cart.py
 │   ├─ category.py
 │   └─ product.py
 └─ services/
     ├─ __init__.py
     ├─ cart.py
     ├─ category.py
     └─ product.py

seed_data.py
requirements.txt
.gitignore
```
---
## 📜 License
MIT License © 2025
