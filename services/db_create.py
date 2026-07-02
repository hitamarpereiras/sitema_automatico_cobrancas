import os
import sqlite3


def run_database():

    try:

        os.makedirs("/database", exist_ok=True)

        if os.path.isdir("/database"):

            conn = sqlite3.connect(
                os.path.join(
                    "database",
                    "base.db"
                )
            )

            return True, conn

        return False, None

    except PermissionError as e:
        return False, f"Erro de permissão"
    
    except Exception as e:
        return False, f"Erro inesperado!"
