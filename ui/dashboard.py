import os
import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from services.spreadsheet_reader import ExcelService
import threading



def alert_system(msg, success):

    if success:
        messagebox.showinfo(
            "Sucesso!",
            msg
        )
    else:
        messagebox.showerror(
            "Ops!",
            msg
        )


def show_logo():

    img = Image.open(
        os.path.join(
            "assets",
            "logo_.png"
        )
    )

    return ctk.CTkImage(
        img,
        size=(80, 80)
    )


class DashboardFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#6b6d6a"
        )

        self.pack(
            fill="both",
            expand=True
        )

        self.path = ""

        self.build()

    def build(self):

        
        # TOPO
        ###############################################

        top = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top.pack(
            fill="x",
            pady=15,
            padx=15
        )

        logo = ctk.CTkLabel(
            top,
            image=show_logo(),
            text=""
        )

        logo.pack()

        title = ctk.CTkLabel(
            top,
            text="Sistema de Cobranças",
            font=("Arial", 28, "bold")
        )

        title.pack(
            pady=(10, 0)
        )

        
        # ULTIMO ACESSO
        #####################################################

        access = ctk.CTkFrame(
            self,
            fg_color="#575757",
            corner_radius=10
        )

        access.pack(
            fill="x",
            padx=15,
            pady=10
        )

        ctk.CTkLabel(
            access,
            text="Último acesso",
            font=("Arial", 18, "bold")
        ).pack(
            pady=(10, 5)
        )

        self.lb_user = ctk.CTkLabel(
            access,
            text="Usuário : --------"
        )

        self.lb_user.pack()

        self.lb_entry = ctk.CTkLabel(
            access,
            text="Entrada : --------"
        )

        self.lb_entry.pack()

        self.lb_exit = ctk.CTkLabel(
            access,
            text="Saída : --------"
        )

        self.lb_exit.pack(
            pady=(0, 10)
        )

        
        # PLANILHA
        #####################################################

        plan = ctk.CTkFrame(
            self,
            fg_color="#575757",
            corner_radius=10
        )

        plan.pack(
            fill="x",
            padx=15,
            pady=10
        )

        ctk.CTkLabel(
            plan,
            text="Planilha de Clientes",
            font=("Arial", 18, "bold")
        ).pack(
            pady=(10, 5)
        )

        self.path_entry = ctk.CTkEntry(
            plan,
            width=350,
            placeholder_text="Selecione uma planilha..."
        )

        self.path_entry.pack(
            pady=5
        )

        self.btn_search = ctk.CTkButton(
            plan,
            text="Selecionar Planilha",
            width=220,
            fg_color="white",
            text_color="black",
            hover_color="#cbcbcb",
            command=self.search_file
        )

        self.btn_search.pack(
            pady=10
        )

        self.btn_import = ctk.CTkButton(
            plan,
            text="Importar Clientes",
            width=220,
            fg_color="#fc3a51",
            hover_color="#e03549",
            command=self.add_clients_db
        )

        self.btn_import.pack(
            pady=(0, 10)
        )

        # BARRA DE PROGRESSO
        #####################################################

        self.progress = ctk.CTkProgressBar(
            self,
            width=220,
            mode="indeterminate",
            progress_color="#fc3a51"
        )

        self.progress.pack_forget()

        
        # RESUMO
        #####################################################

        stats = ctk.CTkFrame(
            self,
            fg_color="#575757",
            corner_radius=10
        )

        stats.pack(
            fill="x",
            padx=15,
            pady=10
        )

        ctk.CTkLabel(
            stats,
            text="Resumo",
            font=("Arial", 18, "bold")
        ).pack(
            pady=(10, 10)
        )

        self.lb_clients = ctk.CTkLabel(
            stats,
            text=f"Total de Clientes : 0"
        )

        self.lb_clients.pack()

        self.lb_pending = ctk.CTkLabel(
            stats,
            text=f"Atualizações : 0"
        )

        self.lb_pending.pack()

       
        # COBRANÇA
        #####################################################


        self.btn_charge = ctk.CTkButton(
            self,
            text="Automatizar Cobranças",
            width=240,
            height=30,
            text_color="black",
            fg_color="white",
            hover_color="#aab5d2"
        )

        self.btn_charge.pack(
            pady=10
        )

        
        # RODAPÉ
        #####################################################

        footer = ctk.CTkLabel(
            self,
            text="© 2026 Hitamar Silva",
            text_color="#252525"
        )

        footer.pack(
            side="bottom",
            pady=10
        )


    # BARRA DE PROGRESSO
    #########################################################

    def start_loading(self):

        self.progress.pack(pady=(10, 5))

        self.progress.start()

    def stop_loading(self):

        self.progress.stop()

        self.progress.pack_forget()



    # ESCOLHER PLANILHA
    #########################################################

    def search_file(self):

        filename = filedialog.askopenfilename(

            title="Selecionar Planilha",

            filetypes=[

                ("Planilhas Excel", "*.xlsx"),

                ("Planilhas Excel", "*.xls")

            ]

        )

        if filename:

            self.path = filename

            self.path_entry.delete(
                0,
                "end"
            )

            self.path_entry.insert(
                0,
                filename
            )


    # ADICINAR CLIENTES
    #########################################################

    def add_clients_db(self):
        path_excel = self.path_entry.get().strip()

        if not path_excel:
            alert_system("Selecione uma planilha primeiro.", False)
            return

        self.start_loading()
        self.btn_import.configure(state="disabled")
        self.btn_search.configure(state="disabled")

        threading.Thread(
            target=self.import_clients,
            args=(path_excel,),
            daemon=True
        ).start()

    def import_clients(self, path_excel):
        try:
            excel = ExcelService(path_excel)
            bln, response = excel.add_clients()
        except Exception as error:
            bln = False
            response = f"Erro ao importar: {error}"

        # Widgets do CustomTkinter só podem ser alterados pela thread principal.
        self.after(0, self.finish_import, bln, response)

    def finish_import(self, bln, response):
        self.stop_loading()
        self.btn_import.configure(state="normal")
        self.btn_search.configure(state="normal")

        if bln:
            self.lb_clients.configure(
                text=f"Total de Clientes : {response['total']}"
            )
            self.lb_pending.configure(
                text=f"Atualiza\u00e7\u00f5es : {response['updates']}"
            )

            alert_system(
                "Operação efetuada com sucesso!",
                bln
            )

        else:
            alert_system(
                response,
                bln
            )




