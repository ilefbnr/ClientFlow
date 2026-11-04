
def test_create_ticket(client):
    customer = client.post("/api/v1/customers/", json={
        "full_name": "John Doe",
        "email": "john@example.com"
    }).json()

    response = client.post("/api/v1/tickets/", json={
        "title": "Website issue",
        "description": "Website is down",
        "priority": "high",
        "customer_id": customer["id"]
    })

    assert response.status_code == 201
    assert response.json()["title"] == "Website issue"
    assert response.json()["status"] == "open"
    assert response.json()["priority"] == "high"


def test_create_ticket_with_invalid_customer(client):
    response = client.post("/api/v1/tickets/", json={
        "title": "Website issue",
        "customer_id": 999
    })

    assert response.status_code == 404


def test_create_ticket_with_invalid_status(client):
    customer = client.post("/api/v1/customers/", json={
        "full_name": "Jane Doe",
        "email": "jane@example.com"
    }).json()

    response = client.post("/api/v1/tickets/", json={
        "title": "Website issue",
        "status": "invalid",
        "customer_id": customer["id"]
    })

    assert response.status_code == 422


def test_get_tickets(client):
    customer = client.post("/api/v1/customers/", json={
        "full_name": "John Doe",
        "email": "john@example.com"
    }).json()

    client.post("/api/v1/tickets/", json={
        "title": "Ticket 1",
        "customer_id": customer["id"]
    })

    response = client.get("/api/v1/tickets/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_ticket_by_id(client):
    customer = client.post("/api/v1/customers/", json={
        "full_name": "John Doe",
        "email": "john@example.com"
    }).json()

    ticket = client.post("/api/v1/tickets/", json={
        "title": "Ticket 1",
        "customer_id": customer["id"]
    }).json()

    response = client.get(f"/api/v1/tickets/{ticket['id']}")

    assert response.status_code == 200
    assert response.json()["title"] == "Ticket 1"


def test_get_nonexistent_ticket(client):
    response = client.get("/api/v1/tickets/999")

    assert response.status_code == 404


def test_update_ticket(client):
    customer = client.post("/api/v1/customers/", json={
        "full_name": "John Doe",
        "email": "john@example.com"
    }).json()

    ticket = client.post("/api/v1/tickets/", json={
        "title": "Old title",
        "customer_id": customer["id"]
    }).json()

    response = client.put(
        f"/api/v1/tickets/{ticket['id']}",
        json={"title": "Updated title", "priority": "urgent"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"
    assert response.json()["priority"] == "urgent"


def test_update_ticket_with_invalid_customer(client):
    customer = client.post("/api/v1/customers/", json={
        "full_name": "John Doe",
        "email": "john@example.com"
    }).json()

    ticket = client.post("/api/v1/tickets/", json={
        "title": "Ticket 1",
        "customer_id": customer["id"]
    }).json()

    response = client.put(
        f"/api/v1/tickets/{ticket['id']}",
        json={"customer_id": 999}
    )

    assert response.status_code == 404


def test_update_nonexistent_ticket(client):
    response = client.put(
        "/api/v1/tickets/999",
        json={"title": "Updated"}
    )

    assert response.status_code == 404


def test_delete_ticket(client):
    customer = client.post("/api/v1/customers/", json={
        "full_name": "John Doe",
        "email": "john@example.com"
    }).json()

    ticket = client.post("/api/v1/tickets/", json={
        "title": "Ticket 1",
        "customer_id": customer["id"]
    }).json()

    response = client.delete(f"/api/v1/tickets/{ticket['id']}")

    assert response.status_code == 204

    get_response = client.get(f"/api/v1/tickets/{ticket['id']}")
    assert get_response.status_code == 404


def test_delete_nonexistent_ticket(client):
    response = client.delete("/api/v1/tickets/999")

    assert response.status_code == 404
