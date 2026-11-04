from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.models.customer import Customer
from app.schemas.ticket import TicketCreate, TicketUpdate


class CustomerNotFoundError(Exception):
    pass


def create_ticket(db: Session, ticket_data: TicketCreate):
    customer = db.query(Customer).filter(
        Customer.id == ticket_data.customer_id
    ).first()

    if customer is None:
        raise CustomerNotFoundError()

    new_ticket = Ticket(
        title=ticket_data.title,
        description=ticket_data.description,
        status=ticket_data.status,
        priority=ticket_data.priority,
        customer_id=ticket_data.customer_id
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


def get_tickets(db: Session):
    return db.query(Ticket).all()


def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()


def update_ticket(db: Session, ticket_id: int, ticket_data: TicketUpdate):
    ticket = get_ticket_by_id(db, ticket_id)

    if ticket is None:
        return None

    update_data = ticket_data.model_dump(exclude_unset=True)

    if "customer_id" in update_data and update_data["customer_id"] is not None:
        customer = db.query(Customer).filter(
            Customer.id == update_data["customer_id"]
        ).first()

        if customer is None:
            raise CustomerNotFoundError()

    for field, value in update_data.items():
        setattr(ticket, field, value)

    db.commit()
    db.refresh(ticket)

    return ticket


def delete_ticket(db: Session, ticket_id: int):
    ticket = get_ticket_by_id(db, ticket_id)

    if ticket is None:
        return False

    db.delete(ticket)
    db.commit()

    return True