
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import (
    health,
    customers,
    tickets,
    conversations,
    messages,
    dashboard

)

app = FastAPI(title="ClientFlow API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["Health"])

app.include_router(
    customers.router,
    prefix="/api/v1/customers",
    tags=["Customers"]
)

app.include_router(
    tickets.router,
    prefix="/api/v1/tickets",
    tags=["Tickets"]
)

app.include_router(
    conversations.router,
    prefix="/api/v1/conversations",
    tags=["Conversations"]
)

app.include_router(
    messages.router,
    prefix="/api/v1",
    tags=["Messages"]
)

app.include_router(
    dashboard.router,
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)