# Proyecto FastAPI con Docker

Este proyecto es una API construida con FastAPI que gestiona solicitudes de ingreso a una academia de magia en el Reino del Trébol y asigna grimorios (libros mágicos) a los estudiantes. La aplicación incluye varias funcionalidades como el envío, actualización, consulta y eliminación de solicitudes, así como la asignación aleatoria de grimorios basada en probabilidades específicas.

## Funcionalidades
- Crear Solicitud: Permite a los estudiantes enviar una solicitud de ingreso a la academia de magia.
- Actualizar Solicitud: Permite actualizar la información de una solicitud existente.
- Actualizar Estatus de Solicitud: Permite cambiar el estatus de una solicitud (recibido, rechazado, aprobado).
- Consultar Solicitudes: Permite consultar todas las solicitudes enviadas.
- Consultar Asignaciones: Permite consultar las asignaciones de grimorios realizadas.
- Eliminar Solicitud: Permite eliminar una solicitud de ingreso.

## Video de explicación 
[![Alt text](https://img.youtube.com/vi/pHsfQL-b7Ms/0.jpg)](https://www.youtube.com/watch?v=pHsfQL-b7Ms)

## Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Instalación y Ejecución

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/dalokdaga/prueba_tecnica_interactive
cd prueba_tecnica_interactive
```
### 1.2 Ejecución en local
```bash
uvicorn main:app
```

### 2. Construir la Imagen Docker
Construye la imagen Docker utilizando Docker Compose:

    ```bash
    docker-compose build
    ```

### 3. Ejecutar la Aplicación
Ejecuta los contenedores utilizando Docker Compose:

    ```bash
    docker-compose up
    ```
### 4. Ejecutar la Aplicación
La aplicación FastAPI estará disponible en http://localhost:8000 Puedes acceder a la documentación interactiva en http://localhost:8000/docs

### Endpoints
- POST /solicitud: Envía solicitud de ingreso.
- PUT /solicitud/{id}: Actualiza solicitud de ingreso.
- PATCH /solicitud/{id}/estatus: Actualiza estatus de solicitud.
- GET /solicitudes: Consulta todas las solicitudes.
- GET /asignaciones: Consulta asignaciones de Grimorios.
- DELETE /solicitud/{id}: Elimina solicitud de ingreso.

### Ejecutar test unitarios
```bash
python -m unittest tests/test.py
```

### Ejemplo de uso, consultas endpoints Fastapi
Envía solicitud de ingreso:
```bash
    curl -X 'POST' \
    'http://localhost:8000/api/v1/solicitud' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "nombre": "Daniel",
    "apellido": "Garcia",
    "identificacion": "DaNGar",
    "edad": 31,
    "afinidad_magica": "Agua"
    }'
```

Actualiza solicitud de ingreso:
```bash
curl -X 'PUT' \
'http://localhost:8000/api/v1/solicitud/1' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"nombre": "Daniel",
"apellido": "Uscanga",
"identificacion": "DaNGar",
"edad": 31,
"afinidad_magica": "Agua"
}'
```

Actualiza estatus de solicitud:
```bash
curl -X 'PATCH' \
'http://localhost:8000/api/v1/solicitud/1/estatus' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"estatus": "aprobado"
}'
```

Consulta todas las solicitudes:
```bash
curl -X 'GET' \
'http://localhost:8000/api/v1/solicitudes?skip=0&limit=10' \
-H 'accept: application/json'
```

Consulta asignaciones de Grimorios:
```bash
curl -X 'GET' \
'http://localhost:8000/api/v1/asignaciones' \
-H 'accept: application/json'
```

Elimina solicitud de ingreso:
```bash
curl -X 'DELETE' \
'http://localhost:8000/api/v1/solicitud/1' \
-H 'accept: application/json'
```