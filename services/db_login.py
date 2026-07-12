import sqlite3
import os
from typing import Optional, Dict, Any
from . import my_hash

def login_user(username: str, password: str) -> Optional[Dict[str, Any]]:

    try:

        conn = sqlite3.connect(
            os.path.join(
                "database",
                "DATABASE.db"
            )
        )
        cursor = conn.cursor()
        
        # Buscar usuário com as credenciais fornecidas
        cursor.execute("""
            SELECT 
                id,
                usuario,
                senha,
                admin,
                data_criacao,
                entrada,
                saida
            FROM usuarios 
            WHERE usuario = ?
        """, (username,))
        
        user_found = cursor.fetchone()
        
        # Criar dicionário com os dados do usuário

        if user_found:
            data_user = {
                'id': user_found[0],
                'usuario': user_found[1],
                'hash': str(user_found[2]),
                'admin': bool(user_found[3]),
                'data_criacao': user_found[4],
                'entrada': user_found[5],
                'saida': user_found[6]
            }

            bln = my_hash.verify_password(password, data_user['hash'])

            if bln:
                return True, data_user
            
            return False, "Senha ou Usuário incorreto!"

        else:
            return False, "Usuário não encontrado!"
            
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
        return False, "Erro inesperado!"
    
    finally:
        if conn:
            conn.close()