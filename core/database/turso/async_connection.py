import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# Configuración de Turso
TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")
DEBUG = True if os.getenv("DEBUG") == "DEBUG" else False

# Generar motor asíncrono para Turso
engine = create_async_engine(
    f"libsql+async://{TURSO_DATABASE_URL}.turso.io/?authToken={TURSO_AUTH_TOKEN}&secure=true",
    echo=True
)

# Configurar sesión asíncrona
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_async_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()