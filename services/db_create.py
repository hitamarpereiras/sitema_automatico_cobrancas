import os
import sqlite3


def run_database():

    try:

        os.makedirs("/database", exist_ok=True)

        if os.path.isdir("/database"):

            conn = sqlite3.connect(
                os.path.join(
                    "database",
                    "DATABASE.db"
                )
            )

            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id PRIMARY KEY,
                    usuario TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL,
                    admin INTEGER NOT NULL DEFAULT 0,
                    data_criacao TEXT NOT NULL,
                    entrada TEXT,
                    saida TEXT
                )
            """)

            conn.commit()

            return True, f"Database ON!"

        return False, f"Erro Database!"

    except PermissionError as e:
        return False, f"Erro de permissão"
    
    except Exception as e:
        return False, f"Erro inesperado!"
    
    finally:
        cursor.close()
