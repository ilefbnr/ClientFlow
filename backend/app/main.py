from fastapi import FastAPI
from app.api.routes import health,customers,tickets

app = FastAPI(
    title="ClientFlow API",
    description="API for managing customers and service requests",
    version="1.0.0"
)

app.include_router(
    health.router,
    prefix="/api/v1",
    tags=["Health"]
    )


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