def test_dashboard_empty(client):
    response = client.get("/api/v1/dashboard/")

    assert response.status_code == 200

    data = response.json()

    assert data["total_customers"] == 0
    assert data["total_tickets"] == 0
    assert data["open_tickets"] == 0
    assert data["in_progress_tickets"] == 0
    assert data["resolved_tickets"] == 0
    assert data["closed_tickets"] == 0
    assert data["urgent_tickets"] == 0
    assert data["total_conversations"] == 0
    assert data["open_conversations"] == 0


def test_dashboard_with_data(client):
    # Create a customer
    customer_response = client.post(
        "/api/v1/customers/",
        json={
            "full_name": "Test Customer",
            "email": "dashboard@test.com",
            "phone": "12345678"
        }
    )

    assert customer_response.status_code == 201
    customer_id = customer_response.json()["id"]

    # Create tickets
    tickets = [
        {
            "title": "Open ticket",
            "description": "First ticket",
            "status": "open",
            "priority": "urgent",
            "customer_id": customer_id
        },
        {
            "title": "In progress ticket",
            "description": "Second ticket",
            "status": "in_progress",
            "priority": "medium",
            "customer_id": customer_id
        },
        {
            "title": "Resolved ticket",
            "description": "Third ticket",
            "status": "resolved",
            "priority": "low",
            "customer_id": customer_id
        }
    ]

    for ticket in tickets:
        response = client.post(
            "/api/v1/tickets/",
            json=ticket
        )
        assert response.status_code == 201

    # Create conversations
    conversations = [
        {
            "channel": "email",
            "status": "open",
            "customer_id": customer_id
        },
        {
            "channel": "whatsapp",
            "status": "closed",
            "customer_id": customer_id
        }
    ]

    for conversation in conversations:
        response = client.post(
            "/api/v1/conversations/",
            json=conversation
        )
        assert response.status_code == 201

    # Check dashboard
    response = client.get("/api/v1/dashboard/")

    assert response.status_code == 200

    data = response.json()

    assert data["total_customers"] == 1
    assert data["total_tickets"] == 3
    assert data["open_tickets"] == 1
    assert data["in_progress_tickets"] == 1
    assert data["resolved_tickets"] == 1
    assert data["closed_tickets"] == 0
    assert data["urgent_tickets"] == 1
    assert data["total_conversations"] == 2
    assert data["open_conversations"] == 1