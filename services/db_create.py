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
                    id TEXT PRIMARY KEY,
                    usuario TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL,
                    admin INTEGER NOT NULL DEFAULT 0,
                    data_criacao DATE NOT NULL,
                    entrada DATE NOT NULL,
                    saida DATE NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    valor REAL NOT NULL DEFAULT 0.0,
                    status TEXT NOT NULL DEFAULT 'PENDENTE',
                    data_vencimento DATE NOT NULL,
                    data_importacao DATE NOT NULL
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS historico_envios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id TEXT NOT NULL,

                    dias_antes INTEGER NOT NULL,

                    data_envio DATE NOT NULL,

                    status TEXT NOT NULL,

                    erro TEXT,

                    FOREIGN KEY(cliente_id)
                        REFERENCES clientes(id)
                )
            """)

            conn.commit()

            return True, f"Database ON!"

        return False, f"Erro Database!"

    except PermissionError as e:
        return False, f"Erro de permissão"
    
    except Exception as e:
        print(e)
        return False, f"Erro inesperado!"
    
    finally:
        cursor.close()
