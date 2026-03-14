import psycopg2
from config.settings import settings

def get_db_connection():
    return psycopg2.connect(
        host=settings.db_host,
        port=settings.db_port,
        dbname=settings.db_name,
        user=settings.db_user,
        password=settings.db_password
    )

def log_user_access(user_name: str):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO log_users_access (name) VALUES (%s)", (user_name,))
        conn.commit()
    finally:
        cur.close()
        conn.close()
