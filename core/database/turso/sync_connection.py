import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Configuración de Turso
TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")
DEBUG = True if os.getenv("DEBUG") == "DEBUG" else False

# Generar motor síncrono para Turso
engine = create_engine(
    f"libsql://{TURSO_DATABASE_URL}.turso.io/?authToken={TURSO_AUTH_TOKEN}&secure=true",
    echo=DEBUG
)

# Configurar sesión síncrona
SessionLocal = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

def get_sync_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()