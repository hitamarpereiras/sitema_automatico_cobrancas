import os
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image


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

        ###############################################
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

        #####################################################
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

        #####################################################
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
            hover_color="#b12a3a"
        )

        self.btn_import.pack(
            pady=(0, 10)
        )

        #####################################################
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
            text="Clientes cadastrados : 0"
        )

        self.lb_clients.pack()

        self.lb_pending = ctk.CTkLabel(
            stats,
            text="Pendentes : 0"
        )

        self.lb_pending.pack()

        self.lb_paid = ctk.CTkLabel(
            stats,
            text="Pagos : 0"
        )

        self.lb_paid.pack(
            pady=(0, 10)
        )

        #####################################################
        # COBRANÇA
        #####################################################

        self.progress = ctk.CTkProgressBar(
            self,
            width=300,
            mode="indeterminate",
            progress_color="#fc3a51"
        )

        self.progress.pack_forget()

        self.btn_charge = ctk.CTkButton(
            self,
            text="Automatizar Cobranças",
            width=300,
            height=45,
            fg_color="#fc3a51",
            hover_color="#b12a3a"
        )

        self.btn_charge.pack(
            pady=20
        )

        #####################################################
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

    #########################################################
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