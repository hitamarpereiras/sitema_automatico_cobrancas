import pandas as pd
import os
import sqlite3
from datetime import datetime
from services.id_generator import generate_id


class ExcelService:
    def __init__(self, path_xlsx):
        self.df = pd.read_excel(path_xlsx)

        self.df["Data_Vencimento"] = pd.to_datetime(
            self.df["Data_Vencimento"]
        )

    def clients(self):
        return self.df.iterrows()
    
    def get_id(self, cursor, email):
        cursor.execute(
            """
            SELECT id
            FROM clientes
            WHERE email = ?
            LIMIT 1
            """,
            (email,)
        )
        response = cursor.fetchone()

        if response:
            return response[0]
    
    def email_exists(self, cursor, email):
        cursor.execute(
            "SELECT 1 FROM clientes WHERE email = ? LIMIT 1",
            (email, )
        )
        return cursor.fetchone() is not None
    
    def status_check(self, cursor, cliente_id):

        cursor.execute("""
            SELECT status
            FROM clientes
            WHERE id = ?
        """, (cliente_id,))

        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]

        return None
    
    def add_clients(self):
        conn = sqlite3.connect(
            os.path.join(
                "database",
                "DATABASE.db"
            )
        )

        cursor = conn.cursor()

        try:

            for i, client in self.clients():

                # Verifica se o cliente ja existe por email
                if self.email_exists(cursor, client["Email"]):

                    this_id = self.get_id(cursor, client["Email"])

                    # Verifica se o status esta diferente
                    if self.status_check(cursor, client["Status"]) != "PENDENTE":

                        cursor.execute("""
                            UPDATE clientes
                            SET status = ?
                            WHERE id = ?
                        """, (
                            client["Status"],
                            this_id 
                        ))

                else:

                    # ID do cliente
                    id_client = generate_id()

                    # Data de criação
                    data_created = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                    cursor.execute("""
                        INSERT INTO clientes (
                            id,
                            nome,
                            email,
                            valor,
                            data_vencimento,
                            data_importacao
                        )
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        id_client,
                        client["Nome"],
                        client["Email"],
                        client["Valor"],
                        str(client["Data_Vencimento"]),
                        data_created
                    ))

            conn.commit()
            return True, "Clientes adicionados com sucesso!"

        except Exception as e:
            print(e)
            return False, f"Erro ao cadastrar!"

        finally:
            conn.close() 
