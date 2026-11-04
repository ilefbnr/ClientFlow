
from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate


class CustomerAlreadyExistsError(Exception):
    pass


def create_customer(db: Session, customer_data: CustomerCreate):
    existing_customer = db.query(Customer).filter(
        Customer.email == customer_data.email
    ).first()

    if existing_customer:
        raise CustomerAlreadyExistsError()

    new_customer = Customer(
        full_name=customer_data.full_name,
        email=customer_data.email,
        phone=customer_data.phone
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


def get_customers(db: Session):
    return db.query(Customer).all()


def get_customer_by_id(db: Session, customer_id: int):
    return db.query(Customer).filter(
        Customer.id == customer_id
    ).first()


def update_customer(
    db: Session,
    customer_id: int,
    customer_data: CustomerUpdate
):
    customer = get_customer_by_id(db, customer_id)

    if customer is None:
        return None

    update_data = customer_data.model_dump(exclude_unset=True)

    if "email" in update_data and update_data["email"] is not None:
        existing_customer = db.query(Customer).filter(
            Customer.email == update_data["email"],
            Customer.id != customer_id
        ).first()

        if existing_customer:
            raise CustomerAlreadyExistsError()

    for field, value in update_data.items():
        setattr(customer, field, value)

    db.commit()
    db.refresh(customer)

    return customer


def delete_customer(db: Session, customer_id: int):
    customer = get_customer_by_id(db, customer_id)

    if customer is None:
        return False

    db.delete(customer)
    db.commit()

    return True
