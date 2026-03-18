import asyncpg
from .config import DATABASE_URL

async def fetch_message():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        row = await conn.fetchrow("SELECT message FROM greetings LIMIT 1")
        return row['message'] if row else None
    finally:
        await conn.close()
