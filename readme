# ClientFlow

**A CRM platform for small businesses to manage customers, service requests, and customer interactions.**

ClientFlow is a SaaS-oriented CRM project designed to help small businesses centralize customer information, track service requests, and manage customer interactions.

The project follows a progressive development approach, starting with a traditional CRM before integrating AI capabilities such as automatic ticket classification, RAG, and AI agents.

## Current Features

### Customer Management
- Create, retrieve, update, and delete customers.
- Store customer information: name, email, and phone.
- Prevent duplicate email addresses.

### Ticket Management
- Create and manage customer service requests.
- Associate tickets with existing customers.
- Track ticket status and priority.
- Validate customer references.
- Support partial ticket updates.

### Backend Architecture
- REST API built with FastAPI.
- Layered architecture separating API routes, services, schemas, and database models.
- PostgreSQL database with SQLAlchemy ORM.
- Database migrations managed with Alembic.
- Automated API tests with Pytest.

## Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Migrations | Alembic |
| Testing | Pytest, HTTPX |
| Infrastructure | Docker |

## Project Structure

```text
clientFlow/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   ├── migrations/
│   ├── tests/
│   ├── .env
│   └── alembic.ini
├── frontend/
└── docker-compose.yml
```

## Getting Started

### Prerequisites

- Python 3.13+
- Docker
- Git

### 1. Clone the repository

```bash
git clone <repository-url>
cd clientFlow
```

### 2. Start PostgreSQL

```bash
docker compose up -d
```

### 3. Configure environment variables

Create a `.env` file inside the `backend/` directory:

```env
DATABASE_URL=postgresql+psycopg://clientflow:clientflow_dev@localhost:5432/clientflow_db
```

### 4. Set up the backend

```bash
cd backend

python -m venv venv
```

Activate the virtual environment:

**Windows PowerShell**
```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy "psycopg[binary]" python-dotenv alembic pytest httpx
```

### 5. Apply database migrations

```bash
alembic upgrade head
```

### 6. Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

## API Endpoints

### Customers

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/customers/` | Create a customer |
| GET | `/api/v1/customers/` | Retrieve all customers |
| GET | `/api/v1/customers/{id}` | Retrieve a customer |
| PUT | `/api/v1/customers/{id}` | Update a customer |
| DELETE | `/api/v1/customers/{id}` | Delete a customer |

### Tickets

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/tickets/` | Create a ticket |
| GET | `/api/v1/tickets/` | Retrieve all tickets |
| GET | `/api/v1/tickets/{id}` | Retrieve a ticket |
| PUT | `/api/v1/tickets/{id}` | Update a ticket |
| DELETE | `/api/v1/tickets/{id}` | Delete a ticket |

### Ticket Statuses

- `open`
- `in_progress`
- `resolved`
- `closed`

### Ticket Priorities

- `low`
- `medium`
- `high`
- `urgent`

## Running Tests

From the `backend/` directory:

```bash
python -m pytest -v
```

The current test suite covers customer and ticket CRUD operations, validation, and error handling.

## Development Roadmap

The project is being developed in five phases:

- [x] **Phase 1 — Classic CRM (in progress):** Customer management and ticket management.
- [ ] **Phase 1 — Conversations:** Conversation and message management.
- [ ] **Phase 2 — AI Classification:** Automatic ticket categorization, priority detection, and information extraction.
- [ ] **Phase 3 — RAG:** An assistant that answers questions using company documentation.
- [ ] **Phase 4 — AI Agents:** Agents that interact with CRM tools, with human approval and validation.
- [ ] **Phase 5 — Evaluation & Deployment:** Automated evaluation, metrics, Docker, and deployment.

## Project Goals

ClientFlow aims to explore the development of a practical AI-powered SaaS application, combining:

- Backend engineering and REST API design.
- Relational database modeling.
- Software architecture and automated testing.
- Retrieval-Augmented Generation (RAG).
- LLM-powered automation and AI agents.

---

**Status:** Under active development.