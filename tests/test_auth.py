
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.user_store import users
from app.services.security import create_access_token


@pytest.fixture
def client():
    users.clear()
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def test_user():
    return {
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "TestPassword@123"
    }


def test_register_success(client, test_user):
    response = client.post(
        "/api/v1/auth/register",
        json=test_user
    )

    assert response.status_code == 201
    assert response.json()["message"] == "Account created successfully"
    assert "password_hash" in users[test_user["email"]]


def test_duplicate_registration(client, test_user):
    client.post("/api/v1/auth/register", json=test_user)

    response = client.post(
        "/api/v1/auth/register",
        json=test_user
    )

    assert response.status_code == 409
    assert response.json()["detail"] == "Email already registered"


def test_login_success(client, test_user):
    client.post("/api/v1/auth/register", json=test_user)

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": test_user["email"],
            "password": test_user["password"]
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_wrong_password(client, test_user):
    client.post("/api/v1/auth/register", json=test_user)

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": test_user["email"],
            "password": "WrongPassword@123"
        }
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"


def test_profile_without_token(client):
    response = client.get("/api/v1/auth/me")

    assert response.status_code == 401


def test_profile_with_valid_token(client, monkeypatch):
    monkeypatch.setenv(
        "JWT_SECRET_KEY",
        "test-only-secret-key-that-is-long-enough-for-testing"
    )

    email = "testuser@example.com"

    users[email] = {
        "name": "Test User",
        "email": email,
        "password_hash": "not-returned-to-client"
    }

    token = create_access_token(email)

    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["user"]["email"] == email
    assert "password_hash" not in response.json()["user"]


def test_profile_with_invalid_token(client):
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": "Bearer invalid.fake.jwt.token"}
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or expired access token"
