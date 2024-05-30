from fastapi import FastAPI
from app.core.models import Base
from config.database import engine
from app.api.urls import urls  # Importar urls desde urls.py

# Crear las tablas de la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI()

# Registrar las rutas en la aplicación
app.include_router(urls)

@app.get('/')
def home():
    return { 
        "version": 1,
        "proyect": "Test Interactive"
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)