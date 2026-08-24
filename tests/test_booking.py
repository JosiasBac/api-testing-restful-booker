import requests

from utils.api_client import BASE_URL 

def test_create_booking_success():
    """
    Prueba que se puede crear una nueva reserva de hotel exitosamente.
    """
    url = f"{BASE_URL}/booking"
    
   
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
  
    payload = {
        "firstname": "Carlos",
        "lastname": "Dev",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-10"
        },
        "additionalneeds": "Desayuno incluido"
    }

 
    response = requests.post(url, json=payload, headers=headers)

 
    assert response.status_code == 200, f"Error: Código {response.status_code}. Respuesta: {response.text}"
    
    response_data = response.json()
    

    assert "bookingid" in response_data, "Error: El servidor no generó un ID de reserva"
  
    assert response_data["booking"]["firstname"] == "Carlos", "Error: El nombre guardado no coincide"
    
    print(f"\n¡Reserva creada con éxito! ID asignado: {response_data['bookingid']}")

def test_get_booking_by_id(created_booking_id):

    """Prueba que se puede consultar una reserva específica pasando su ID."""
    
    url = f"{BASE_URL}/booking/{created_booking_id}"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)

    assert response.status_code == 200, f"Error al consultar reserva: {response.status_code}"
    response_data = response.json()
    assert response_data["firstname"] == "Laura"
    assert response_data["lastname"] == "Tester"
    print(f"\n¡Reserva {created_booking_id} obtenida correctamente!")


def test_delete_booking(auth_token, created_booking_id):
    """
    Prueba que se puede eliminar una reserva usando el Token de autorización.
    """
    url = f"{BASE_URL}/booking/{created_booking_id}"
    
    
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={auth_token}"
    }

   
    response = requests.delete(url, headers=headers)

    
    assert response.status_code in [200, 201], f"Error al eliminar la reserva: {response.status_code}"
    print(f"\n¡Reserva {created_booking_id} eliminada con éxito!")