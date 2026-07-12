import sqlite3
import os
from typing import Optional, Dict, Any

def login_user(usuario: str, senha: str) -> Optional[Dict[str, Any]]:

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
                admin,
                data_criacao,
                entrada,
                saida
            FROM usuarios 
            WHERE usuario = ? AND senha = ?
        """, (usuario, senha))
        
        user_found = cursor.fetchone()
        
        # Criar dicionário com os dados do usuário

        if user_found:
            dados_usuario = {
                'id': user_found[0],
                'usuario': user_found[1],
                'admin': bool(user_found[2]),
                'data_criacao': user_found[3],
                'entrada': user_found[4],
                'saida': user_found[5]
            }
            return dados_usuario
        else:
            return False, "Usuário não encontrado!"
            
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
        return False, "Erro inesperado!"
    
    finally:
        if conn:
            conn.close()