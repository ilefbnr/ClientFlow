from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.customer import Customer
from app.models.ticket import Ticket
from app.models.conversation import Conversation


def get_dashboard_stats(db: Session):
    total_customers = (
        db.query(func.count(Customer.id)).scalar() or 0
    )

    total_tickets = (
        db.query(func.count(Ticket.id)).scalar() or 0
    )

    open_tickets = (
        db.query(func.count(Ticket.id))
        .filter(Ticket.status == "open")
        .scalar() or 0
    )

    in_progress_tickets = (
        db.query(func.count(Ticket.id))
        .filter(Ticket.status == "in_progress")
        .scalar() or 0
    )

    resolved_tickets = (
        db.query(func.count(Ticket.id))
        .filter(Ticket.status == "resolved")
        .scalar() or 0
    )

    closed_tickets = (
        db.query(func.count(Ticket.id))
        .filter(Ticket.status == "closed")
        .scalar() or 0
    )

    urgent_tickets = (
        db.query(func.count(Ticket.id))
        .filter(Ticket.priority == "urgent")
        .scalar() or 0
    )

    total_conversations = (
        db.query(func.count(Conversation.id)).scalar() or 0
    )

    open_conversations = (
        db.query(func.count(Conversation.id))
        .filter(Conversation.status == "open")
        .scalar() or 0
    )

    return {
        "total_customers": total_customers,
        "total_tickets": total_tickets,
        "open_tickets": open_tickets,
        "in_progress_tickets": in_progress_tickets,
        "resolved_tickets": resolved_tickets,
        "closed_tickets": closed_tickets,
        "urgent_tickets": urgent_tickets,
        "total_conversations": total_conversations,
        "open_conversations": open_conversations,
    }