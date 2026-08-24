import pytest
import requests
from utils.api_client import BASE_URL

@pytest.fixture
def auth_token():
    """Fixture que solicita un token válido de autenticación antes de la prueba."""
    url = f"{BASE_URL}/auth"
    payload = {"username": "admin", "password": "password123"}
    response = requests.post(url, json=payload)
    return response.json()["token"]

@pytest.fixture
def created_booking_id():
    """Fixture que crea una reserva dinámica y devuelve su ID para usarla en los tests."""
    url = f"{BASE_URL}/booking"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {
        "firstname": "Laura",
        "lastname": "Tester",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
        "additionalneeds": "Cama adicional"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["bookingid"]