
# ============================
# GET CUSTOMERS
# ============================

def test_get_customers(client):
    response = client.get("/api/v1/customers/")

    assert response.status_code == 200
    assert response.json() == []


# ============================
# CREATE CUSTOMER
# ============================

def test_create_customer(client):
    response = client.post(
        "/api/v1/customers/",
        json={
            "full_name": "Ahmed Ben Ali",
            "email": "ahmed@test.com",
            "phone": "22123456"
        }
    )

    assert response.status_code == 201
    assert response.json()["full_name"] == "Ahmed Ben Ali"
    assert response.json()["email"] == "ahmed@test.com"


def test_create_customer_duplicate_email(client):
    customer_data = {
        "full_name": "Ahmed Ben Ali",
        "email": "ahmed@test.com",
        "phone": "22123456"
    }

    client.post("/api/v1/customers/", json=customer_data)

    response = client.post(
        "/api/v1/customers/",
        json=customer_data
    )

    assert response.status_code == 409


# ============================
# GET CUSTOMER BY ID
# ============================

def test_get_customer_by_id(client):
    create_response = client.post(
        "/api/v1/customers/",
        json={
            "full_name": "Sara Ben Ali",
            "email": "sara@test.com",
            "phone": "55123456"
        }
    )

    customer_id = create_response.json()["id"]

    response = client.get(
        f"/api/v1/customers/{customer_id}"
    )

    assert response.status_code == 200
    assert response.json()["full_name"] == "Sara Ben Ali"


def test_get_customer_not_found(client):
    response = client.get("/api/v1/customers/999")

    assert response.status_code == 404


# ============================
# UPDATE CUSTOMER
# ============================

def test_update_customer(client):
    create_response = client.post(
        "/api/v1/customers/",
        json={
            "full_name": "Ahmed Ben Ali",
            "email": "ahmed@test.com",
            "phone": "22123456"
        }
    )

    customer_id = create_response.json()["id"]

    response = client.put(
        f"/api/v1/customers/{customer_id}",
        json={"full_name": "Ahmed Updated"}
    )

    assert response.status_code == 200
    assert response.json()["full_name"] == "Ahmed Updated"
    assert response.json()["email"] == "ahmed@test.com"


def test_update_customer_duplicate_email(client):
    client.post(
        "/api/v1/customers/",
        json={
            "full_name": "Ahmed",
            "email": "ahmed@test.com"
        }
    )

    second_customer = client.post(
        "/api/v1/customers/",
        json={
            "full_name": "Sara",
            "email": "sara@test.com"
        }
    )

    customer_id = second_customer.json()["id"]

    response = client.put(
        f"/api/v1/customers/{customer_id}",
        json={"email": "ahmed@test.com"}
    )

    assert response.status_code == 409


def test_update_customer_not_found(client):
    response = client.put(
        "/api/v1/customers/999",
        json={"full_name": "Unknown"}
    )

    assert response.status_code == 404


# ============================
# DELETE CUSTOMER
# ============================

def test_delete_customer(client):
    create_response = client.post(
        "/api/v1/customers/",
        json={
            "full_name": "Ahmed Ben Ali",
            "email": "ahmed@test.com"
        }
    )

    customer_id = create_response.json()["id"]

    response = client.delete(
        f"/api/v1/customers/{customer_id}"
    )

    assert response.status_code == 204

    get_response = client.get(
        f"/api/v1/customers/{customer_id}"
    )

    assert get_response.status_code == 404


def test_delete_customer_not_found(client):
    response = client.delete("/api/v1/customers/999")

    assert response.status_code == 404
