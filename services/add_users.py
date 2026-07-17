import sqlite3
import os
from datetime import datetime

from services.id_generator import generate_id
from services.my_hash import hash_password


def criar_usuario(user):

    conn = sqlite3.connect(
        os.path.join(
            "database",
            "DATABASE.db"
        )
    )
    cursor = conn.cursor()

    try:
        # Verifica se o usuário já existe
        cursor.execute(
            "SELECT 1 FROM usuarios WHERE usuario = ?",
            (user.username,)
        )

        if cursor.fetchone():
            return False, "Este nome de usuário já está em uso."

        # Gera o ID
        user_id = generate_id()

        # Data de criação
        data_criacao = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Admin
        admin = 0

        # Senha
        passw_hash = hash_password(user.password)

        # Cria o usuário
        cursor.execute("""
            INSERT INTO usuarios (
                id,
                usuario,
                senha,
                admin,
                data_criacao,
                entrada,
                saida
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            user.username,
            passw_hash,
            admin,
            data_criacao,
            None,
            None
        ))

        conn.commit()

        return True, f"{user.username} criado com sucesso."

    except Exception as e:
        return False, f"Erro ao criar usuário"

    finally:
        conn.close()