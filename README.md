# Proyecto FastAPI con Docker

Este es un proyecto básico de FastAPI configurado para ejecutarse dentro de un contenedor Docker. La base de datos utilizada es SQLite3.


## Requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Instalación y Ejecución

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git https://github.com/dalokdaga/prueba_tecnica_interactive
cd prueba_tecnica_interactive
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
La aplicación FastAPI estará disponible en http://localhost:8000. Puedes acceder a la documentación interactiva en http://localhost:8000/docs.

### Endpoints
- POST /solicitud: Envía solicitud de ingreso.
- PUT /solicitud/{id}: Actualiza solicitud de ingreso.
- PATCH /solicitud/{id}/estatus: Actualiza estatus de solicitud.
- GET /solicitudes: Consulta todas las solicitudes.
- GET /asignaciones: Consulta asignaciones de Grimorios.
- DELETE /solicitud/{id}: Elimina solicitud de ingreso.

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
"estatus": "aceptado"
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