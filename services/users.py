
# classe de usuário

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        
    # verifica os dados

    def verify_data(self):
        
        if len(self.username) < 6 or len(self.username) > 20:

            return False, "O nome de usuário não deve ser muito longo\nmin 6 max 20 caracteres"
        
        if len(self.password) < 6 or len(self.password) > 12:

            return False, "Senha no min: 6 max 12 digitos"
        
        return True, "ok"