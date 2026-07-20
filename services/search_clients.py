import sqlite3
import os

def get_pending_clients():

    conn = sqlite3.connect(
        os.path.join(
            "database",
            "DATABASE.db"
        )
    )

    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT
                id,
                nome,
                email,
                valor,
                data_vencimento
            FROM clientes
            WHERE status = 'PENDENTE'
        """)

        return cursor.fetchall()
    
    except Exception as e:
        print(e)
        return False, f"Erro ao buscar clientes!"

    finally:
        conn.close() 