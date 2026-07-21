import sqlite3
import os


def updat_entry(date, userId):

    conn = sqlite3.connect(
        os.path.join(
            "database",
            "DATABASE.db"
        )
    )

    cursor = conn.cursor()

    try:

        cursor.execute("""
            UPDATE usuarios
            SET entrada = ?
            WHERE id = ?
        """, (
            date,
            userId 
        ))

        conn.commit()

    except Exception as e:
        return f"Erro ao atualizar entrada"

    finally:
        conn.close()



def update_release(date, userId):

    conn = sqlite3.connect(
        os.path.join(
            "database",
            "DATABASE.db"
        )
    )

    cursor = conn.cursor()

    try:

        cursor.execute("""
            UPDATE usuarios
            SET saida = ?
            WHERE id = ?
        """, (
            date,
            userId 
        ))

        conn.commit()

    except Exception as e:
        return f"Erro ao atualizar entrada"

    finally:
        conn.close()