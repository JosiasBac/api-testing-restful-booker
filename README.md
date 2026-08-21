# API Testing Framework - Restful Booker

Este proyecto es un framework de pruebas automatizadas para la API de [Restful Booker](https://restful-booker.herokuapp.com/), construido con **Python, Pytest y Requests**.

## Objetivo del Proyecto
Demostrar mis habilidades como QA Automation Junior diseñando casos de prueba, gestionando peticiones HTTP y validando respuestas (Status Codes, JSON Schemas y Tiempos de respuesta).

## Casos de Prueba
Antes de automatizar, he definido los siguientes escenarios criticos de negocio:

1. **Autenticacion:**
   - [ ] Verificar que un usuario valido recibe un Token `200 OK`.
   - [ ] Verificar que credenciales invalidas devuelven un error manejado.
2. **Gestion de Reservas (CRUD):**
   - [ ] Crear una reserva valida (`POST /booking`).
   - [ ] Obtener la reserva recien creada (`GET /booking/{id}`).
   - [ ] Modificar la reserva (`PUT /booking/{id}`).
   - [ ] Eliminar la reserva (`DELETE /booking/{id}`).