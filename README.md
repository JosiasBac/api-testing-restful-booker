# API Automated Testing Framework - Restful Booker

![Automated API Tests](https://github.com/TU_USUARIO/api-testing-restful-booker/actions/workflows/api-tests.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.12-blue)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-orange)

Framework de pruebas automatizadas para la API REST [Restful Booker](https://restful-booker.herokuapp.com/), desarrollado con **Python**, **Pytest** y **Requests**, e integrado en un pipeline de **CI/CD con GitHub Actions**.

---

## Stack Tecnológico
* **Lenguaje:** Python 3.12
* **Peticiones HTTP:** Requests
* **Framework de Pruebas:** Pytest
* **Reportes:** Pytest-HTML
* **CI/CD:** GitHub Actions

---

## Arquitectura y Patrones Aplicados
* **Patrón AAA (Arrange, Act, Assert):** Estructura clara en cada caso de prueba.
* **Pytest Fixtures (`conftest.py`):** Reutilización eficiente de autenticación y creación de datos dinámicos.
* **Centralización de Configuración:** Gestión limpia de URLs y entornos en `utils/api_client.py`.

---

## Casos de Prueba Cubiertos (CRUD)
- [x] **Autenticación:** Generación correcta de token de acceso (`POST /auth`).
- [x] **Crear Reserva:** Validación de payloads anidados y código de respuesta 200 (`POST /booking`).
- [x] **Consultar Reserva:** Obtención de datos mediante ID dinámico (`GET /booking/{id}`).
- [x] **Eliminar Reserva:** Borrado seguro pasando Token en headers (`DELETE /booking/{id}`).

---

## Cómo Ejecutar el Proyecto Localmente

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/api-testing-restful-booker.git](https://github.com/JosiasBac/api-testing-restful-booker.git)
   cd api-testing-restful-booker