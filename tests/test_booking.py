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