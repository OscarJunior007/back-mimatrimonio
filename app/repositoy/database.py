import asyncpg
from typing import Optional, AsyncGenerator
import os

# Pool de conexiones global
db_pool: Optional[asyncpg.Pool] = None


async def init_db_pool():
    """Inicializar el pool de conexiones al arrancar la app"""
    global db_pool
    db_pool = await asyncpg.create_pool(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME", "mimatrimonio_db"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "12345tonto"),
        min_size=5,
        max_size=20,
        command_timeout=60
    )


async def close_db_pool():
    """Cerrar el pool al apagar la app"""
    global db_pool
    if db_pool:
        await db_pool.close()


async def get_db() -> AsyncGenerator[asyncpg.Connection, None]:
    """
    Dependency que proporciona una conexión de la pool.
    Se libera automáticamente después de cada request.
    """
    async with db_pool.acquire() as connection:
        yield connection