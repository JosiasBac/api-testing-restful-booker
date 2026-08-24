import requests

def test_create_token_success():
    """
    Prueba que un usuario válido puede obtener un token de autenticación.
    """

    url = "https://restful-booker.herokuapp.com/auth"
    
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200, f"Error: Código de estado fue {response.status_code}"
    
    response_data = response.json()
    
    assert "token" in response_data, "Error: No se generó ningún token en la respuesta"
    
    print(f"\n¡Prueba superada! El token generado es: {response_data['token']}")