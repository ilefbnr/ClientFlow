
def create_test_customer(client):
    response = client.post("/api/v1/customers/", json={
        "full_name": "John Doe",
        "email": "john@example.com"
    })
    return response.json()


def create_test_conversation(client):
    customer = create_test_customer(client)

    response = client.post("/api/v1/conversations/", json={
        "channel": "whatsapp",
        "customer_id": customer["id"]
    })

    return response.json()


# ==========================
# CONVERSATION TESTS
# ==========================

def test_create_conversation(client):
    customer = create_test_customer(client)

    response = client.post("/api/v1/conversations/", json={
        "channel": "whatsapp",
        "customer_id": customer["id"]
    })

    assert response.status_code == 201
    assert response.json()["channel"] == "whatsapp"
    assert response.json()["status"] == "open"


def test_create_conversation_invalid_customer(client):
    response = client.post("/api/v1/conversations/", json={
        "channel": "email",
        "customer_id": 999
    })

    assert response.status_code == 404


def test_get_conversations(client):
    create_test_conversation(client)

    response = client.get("/api/v1/conversations/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_conversation_by_id(client):
    conversation = create_test_conversation(client)

    response = client.get(
        f"/api/v1/conversations/{conversation['id']}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == conversation["id"]


def test_get_nonexistent_conversation(client):
    response = client.get("/api/v1/conversations/999")

    assert response.status_code == 404


def test_update_conversation(client):
    conversation = create_test_conversation(client)

    response = client.put(
        f"/api/v1/conversations/{conversation['id']}",
        json={"status": "closed"}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "closed"


def test_delete_conversation(client):
    conversation = create_test_conversation(client)

    response = client.delete(
        f"/api/v1/conversations/{conversation['id']}"
    )

    assert response.status_code == 204

    get_response = client.get(
        f"/api/v1/conversations/{conversation['id']}"
    )

    assert get_response.status_code == 404


# ==========================
# MESSAGE TESTS
# ==========================

def test_create_message(client):
    conversation = create_test_conversation(client)

    response = client.post(
        f"/api/v1/conversations/{conversation['id']}/messages",
        json={
            "content": "Hello, I need help.",
            "sender_type": "customer"
        }
    )

    assert response.status_code == 201
    assert response.json()["content"] == "Hello, I need help."
    assert response.json()["sender_type"] == "customer"


def test_create_message_invalid_conversation(client):
    response = client.post(
        "/api/v1/conversations/999/messages",
        json={
            "content": "Hello",
            "sender_type": "customer"
        }
    )

    assert response.status_code == 404


def test_get_messages(client):
    conversation = create_test_conversation(client)

    url = f"/api/v1/conversations/{conversation['id']}/messages"

    client.post(url, json={
        "content": "Hello",
        "sender_type": "customer"
    })

    client.post(url, json={
        "content": "How can we help?",
        "sender_type": "business"
    })

    response = client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_messages_invalid_conversation(client):
    response = client.get(
        "/api/v1/conversations/999/messages"
    )

    assert response.status_code == 404


def test_get_message_by_id(client):
    conversation = create_test_conversation(client)

    message = client.post(
        f"/api/v1/conversations/{conversation['id']}/messages",
        json={
            "content": "Hello",
            "sender_type": "customer"
        }
    ).json()

    response = client.get(f"/api/v1/{message['id']}")

    assert response.status_code == 200
    assert response.json()["content"] == "Hello"


def test_get_nonexistent_message(client):
    response = client.get("/api/v1/999")

    assert response.status_code == 404


def test_delete_message(client):
    conversation = create_test_conversation(client)

    message = client.post(
        f"/api/v1/conversations/{conversation['id']}/messages",
        json={
            "content": "Hello",
            "sender_type": "customer"
        }
    ).json()

    response = client.delete(f"/api/v1/{message['id']}")

    assert response.status_code == 204

    get_response = client.get(f"/api/v1/{message['id']}")
    assert get_response.status_code == 404


def test_delete_nonexistent_message(client):
    response = client.delete("/api/v1/999")

    assert response.status_code == 404
