
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
    CustomerUpdate
)
from app.services import customer_service
from app.services.customer_service import CustomerAlreadyExistsError


router = APIRouter()


@router.post(
    "/",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_customer(
    customer_data: CustomerCreate,
    db: Session = Depends(get_db)
):
    try:
        return customer_service.create_customer(db, customer_data)
    except CustomerAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail="Customer email already exists"
        )


@router.get("/", response_model=list[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return customer_service.get_customers(db)


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = customer_service.get_customer_by_id(db, customer_id)

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(
    customer_id: int,
    customer_data: CustomerUpdate,
    db: Session = Depends(get_db)
):
    try:
        customer = customer_service.update_customer(
            db, customer_id, customer_data
        )
    except CustomerAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail="Email already used by another customer"
        )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    deleted = customer_service.delete_customer(db, customer_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return None
