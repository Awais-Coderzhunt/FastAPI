# Users API

A simple CRUD REST API built with **FastAPI**, **SQLAlchemy**, and **SQLite**.

## Features

- Create, read, update, and delete users
- SQLite database (auto-created on startup as `app.db`)
- Pydantic models for request/response validation
- Interactive API docs via Swagger UI

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — ORM
- [SQLite](https://www.sqlite.org/) — database
- [Uvicorn](https://www.uvicorn.org/) — ASGI server

## Project Structure

```
.
├── main.py          # FastAPI app and route handlers
├── database.py      # DB engine, session, and Base setup
├── models.py        # SQLAlchemy table models
├── schemas.py       # Pydantic request/response schemas
└── requirements.txt # Python dependencies
```

## Setup

1. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**

   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

Once running, open:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

| Method | Path               | Description           |
| ------ | ------------------ | --------------------- |
| GET    | `/`                | Health check          |
| GET    | `/users`           | List all users        |
| GET    | `/users/{user_id}` | Get a single user     |
| POST   | `/users`           | Create a new user     |
| PUT    | `/users/{user_id}` | Update an existing user |
| DELETE | `/users/{user_id}` | Delete a user         |

### Example: Create a user

```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Ali"}'
```

Response:

```json
{
  "id": 1,
  "name": "Ali"
}
```
