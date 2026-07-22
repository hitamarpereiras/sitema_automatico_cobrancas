import os
from datetime import datetime
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image

from services.db_create import run_database
from services.users import User
from services.add_users import criar_usuario
from services.db_login import login_user
from services.updates import updat_entry


def show_logo():
    img = Image.open(
        os.path.join("assets", "logo_.png")
    )

    return ctk.CTkImage(img, size=(100, 100))


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


class LoginFrame(ctk.CTkFrame):

    def __init__(self, master, open_dashboard):

        super().__init__(
            master,
            fg_color="#6b6d6a"
        )

        self.master = master
        self.open_dashboard = open_dashboard

        self.pack(fill="both", expand=True)

        self.database_ok, self.database_message = run_database()

        if self.database_ok:
            self.alert_color = "#007900"
        else:
            self.alert_color = "#A60000"

        self.build()

    def build(self):

        self.grid_columnconfigure(0, weight=1)

        logo = ctk.CTkLabel(
            self,
            image=show_logo(),
            text=""
        )
        logo.pack(pady=(10, 5))

        ctk.CTkLabel(
            self,
            text="Login",
            font=("Arial", 38, "bold")
        ).pack()

        ctk.CTkLabel(
            self,
            text="Entre com suas credenciais\nou registre um novo usuário.",
            font=("Arial", 12)
        ).pack(pady=(5, 15))

        ctk.CTkLabel(
            self,
            text=self.database_message,
            text_color=self.alert_color,
            fg_color="white",
            corner_radius=6,
            width=220
        ).pack(pady=(0, 15))

        ctk.CTkLabel(
            self,
            text="Usuário",
            anchor="w",
            width=212,
            font=("Arial", 12, "bold")
        ).pack()

        self.username = ctk.CTkEntry(
            self,
            width=220,
            height=38,
            placeholder_text="Usuário"
        )
        self.username.pack()

        ctk.CTkLabel(
            self,
            text="Senha",
            anchor="w",
            width=212,
            font=("Arial", 12, "bold")
        ).pack(pady=(10, 0))

        self.password = ctk.CTkEntry(
            self,
            width=220,
            height=38,
            show="*"
        )
        self.password.pack()

        self.progress = ctk.CTkProgressBar(
            self,
            width=220,
            height=8,
            progress_color="#fc3a51",
            mode="indeterminate"
        )

        self.progress.pack_forget()

        self.btn_login = ctk.CTkButton(
            self,
            text="Entrar",
            width=220,
            height=40,
            fg_color="#fc3a51",
            hover_color="#b12a3a",
            command=self.login
        )

        self.btn_login.pack(pady=(20, 10))

        self.btn_register = ctk.CTkButton(
            self,
            text="Registrar",
            width=220,
            height=40,
            fg_color="white",
            text_color="black",
            hover_color="#cbcbcb",
            command=self.register
        )

        self.btn_register.pack()

        ctk.CTkLabel(
            self,
            text="© 2026 Hitamar Silva",
            text_color="#252525"
        ).pack(side="bottom", pady=15)

    def start_loading(self):

        self.progress.pack(pady=(10, 5))

        self.progress.start()

        self.username.configure(state="disabled")
        self.password.configure(state="disabled")

    def stop_loading(self):

        self.progress.stop()

        self.progress.pack_forget()

        self.username.configure(state="normal")
        self.password.configure(state="normal")

    def login(self):

        self.start_loading()

        username = self.username.get()

        password = self.password.get()

        success, response = login_user(
            username,
            password
        )

        self.stop_loading()

        if not success:

            alert_system(response, False)

            return

        updat_entry(
            datetime.now(),
            response["id"]
        )

        self.open_dashboard(response)

    def register(self):

        self.start_loading()

        new_user = User(

            username=self.username.get(),

            password=self.password.get()

        )

        success, response = User.verify_data(
            new_user
        )

        if not success:

            self.stop_loading()

            alert_system(
                response,
                False
            )

            return

        success, response = criar_usuario(
            new_user
        )

        self.stop_loading()

        alert_system(
            response,
            success
        )