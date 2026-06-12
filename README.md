# My FastAPI Project

Ek simple **FastAPI** application jo data store karne ke liye **MongoDB** use karti hai.

## Tech Stack

- **FastAPI** — web framework
- **Uvicorn** — ASGI server
- **MongoDB** — database
- **Motor** — async MongoDB driver
- **Pydantic Settings** — `.env` se configuration

## Project Structure

```
FastAPI/
├── main.py            # Saari app: settings, DB connection, models, routes
├── requirements.txt   # Python dependencies
├── .env               # MongoDB connection settings (git mein ignore)
├── .env.example       # Example env file
└── venv/              # Virtual environment
```

## Requirements

- **Python 3.10+**
- **MongoDB** locally chal raha ho (`mongodb://localhost:27017`)

## Setup

### 1. Virtual environment banayein aur activate karein

```powershell
python -m venv venv
venv\Scripts\activate


Run

uvicorn main:app --reload
```


> macOS/Linux pe: `source venv/bin/activate`

### 2. Dependencies install karein

```powershell
pip install -r requirements.txt
```

### 3. Environment file banayein

`.env.example` ko copy karke `.env` banayein:

```powershell
copy .env.example .env
```

`.env` ke andar:

```env
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=fastapi_db
```

### 4. MongoDB chalu hai confirm karein

MongoDB service running honi chahiye. Check karne ke liye:

```powershell
mongosh --eval "db.runCommand({ ping: 1 })"
```

## Project Run Karna

```powershell
uvicorn main:app --reload
```

Server start ho jayega yahan: **http://127.0.0.1:8000**

- **Swagger UI (interactive docs):** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint           | Kaam                                  |
|--------|--------------------|---------------------------------------|
| GET    | `/`                | Welcome message                       |
| GET    | `/health`          | Health check                          |
| GET    | `/items`           | Saare items list karein               |
| GET    | `/items/{item_id}` | Ek item id se laayein (404 agar nahi) |
| POST   | `/items/{item_id}` | Item create/update (upsert)           |

### Example: Item create karna

```bash
curl -X POST "http://127.0.0.1:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Laptop", "price": 999.99, "is_offer": true}'
```

### Example: Item laana

```bash
curl "http://127.0.0.1:8000/items/1"
```

## Notes

- Data MongoDB ke `fastapi_db` database ki `items` collection mein store hota hai.
- `item_id` ko document ke `_id` ki tarah use kiya jata hai — isliye POST upsert (create ya update) karta hai.
- `.env` file git mein commit nahi hoti (secrets safe rehte hain).
