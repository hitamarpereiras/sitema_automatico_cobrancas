from datetime import datetime
from services.search_clients import get_pending_clients
from time import sleep


class CanCharge():
    def __init__(self):

        clients = get_pending_clients()

        if not clients:
            self.clients = []
            return

        
        self.clients = clients
        
        
    def get_date(self, pay_off):
        today = datetime.now().date()

        pay_off = datetime.strptime(
            pay_off,
            "%Y-%m-%d %H:%M:%S"
        ).date()
        
        return pay_off <= today
    
    def can_charge(self):
        print(f"Quantidade de clientes: {len(self.clients)}")

        for client in self.clients:

            date = f"{client[3]:.2f}"

            if self.get_date(client[4]):
                print(
                    f"""
                    Prezado(a) cliente {client[1]},

                    Identificamos que existe um pagamento pendente em seu cadastro no valor de
                    R$ {date.replace(".", ",")} com vencimento em
                    {client[4].replace("-", "/")}.

                    Solicitamos, por gentileza, que realize o pagamento até a data de vencimento
                    para evitar possíveis encargos e manter sua situação financeira regularizada.

                    Caso o pagamento já tenha sido efetuado, por favor, desconsidere esta mensagem.

                    Em caso de dúvidas, entre em contato com nossa equipe de atendimento:

                    📧 atendimentoaocliente@gmail.com
                    📞 (77) 99985-1122

                    Agradecemos pela atenção e permanecemos à disposição.

                    Atenciosamente,

                    Equipe Financeira
                    """
                )
                sleep(1)
        
        return True, "Cobranças efetuadas!"
            