import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from PIL import Image
from services.db_create import run_database
from services.users import User
from services.add_users import criar_usuario
from services.db_login import login_user

ctk.set_appearance_mode("dark")


def show_logo():
    img = Image.open(
        os.path.join("assets", "logo_.png")
    )

    return ctk.CTkImage(img, size=(100, 100))

def alert_sistem(msg, bln):

    if not bln:
        messagebox.showerror(
            "Ops!",
            f"{msg}"
        )
        return

    messagebox.showinfo(
        "Sucesso!",
        f"{msg}"
    )
    return


class Aplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.configure(
            fg_color = "#6b6d6a"
        )

        self.image_types = None

        self.title('Sistema de Cobranças')
        self.geometry("420x560")
        self.resizable(False, False)

        self.iconbitmap(
            os.path.join(
                "assets",
                "icon_window.ico"
            )
        )

        self.build_ui()

    def build_ui(self):

        self.grid_columnconfigure(0, weight=1)


        # Container Login
        self.container = ctk.CTkFrame(
            self,
            width=480,
            height=500,
            fg_color="#6b6d6a"
        )
        self.container.pack(
            fill="both", 
            expand=True, 
            padx=10, 
            pady=10
        )


        logo = ctk.CTkLabel(
            self.container,
            image=show_logo(),
            text=""
        )
        logo.pack(pady=(5, 5))

        title = ctk.CTkLabel(
            self.container,
            text="Login",
            font=("Arial", 40, "bold")
        )
        title.pack(pady=(8, 8))

        title = ctk.CTkLabel(
            self.container,
            text="Se não estiver registrado por favor\ninsira as informações e clique em REGISTRAR!",
            font=("Arial", 12, "bold")
        )
        title.pack(pady=(5, 5))

        LabelData = ctk.CTkLabel(
            self.container,
            fg_color="white",
            text_color=self.alert_color,
            text=self.response,
            height=14,
            font=("Arial", 12, "normal")
        )
        LabelData.pack(pady=(8, 8))

        labeName = ctk.CTkLabel(
            self.container,
            text="Nome de Usuário:",
            width=305,
            font=("Arial", 12, "bold")
        )
        labeName.pack(anchor="w")

        self.username = ctk.CTkEntry(
            self.container,
            width=200,
            height=40,
            placeholder_text="Ex: joaosantos"
        )
        self.username.pack()

        LabelPassw = ctk.CTkLabel(
            self.container,
            text="Senha:",
            width=245,
            font=("Arial", 12, "bold")
        )
        LabelPassw.pack(anchor="w")

        self.password = ctk.CTkEntry(
            self.container,
            width=200,
            height=40,
            show="*",
            border_color="#6b6d6a"
        )
        self.password.pack()

        # Barra de progresso
        self.progress = ctk.CTkProgressBar(
            self.container,
            width=200,
            height=8,
            progress_color="#fc3a51",
            mode="indeterminate"
        )

        self.progress.pack_forget()
        
        btn_login = ctk.CTkButton(
            self.container,
            text="Automatizar agora!",
            fg_color="#fc3a51",
            hover_color="#b12a3a",
            text_color="white",
            width=200,
            height=40,
            command=self.login_now
        )
        btn_login.pack(pady=10)

        btn_register = ctk.CTkButton(
            self.container,
            text="Registrar!",
            fg_color="white",
            hover_color="#bababa",
            text_color="black",
            width=200,
            height=40,
            command=self.register_user
        )
        btn_register.pack(pady=10)


        LabelFooter = ctk.CTkLabel(
            self,
            text_color="#252525",
            text="© 2026 Hitamar Silva",
            font=("Arial", 12, "italic")
        )
        LabelFooter.pack(pady=10)

    bln, response = run_database()

    if not bln:
        alert_color = "#A60000"
    else:
        alert_color = "#007900"
        

    """ Funções da Interface """

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


    # Função de login
    def login_now(self):
        self.start_loading()
        self.update_idletasks()

        username = self.username.get()
        password = self.password.get()

        bln, response = login_user(username, password)

        self.stop_loading()

        if bln:
            alert_sistem(response, bln)
        else:
            alert_sistem(response, bln)

        return


    # Função de registro
    def register_user(self):
        self.start_loading()
        self.update_idletasks()

        username = self.username.get()
        password = self.password.get()

        new_user = User(
            username=username,
            password=password
        )

        bln, response = User.verify_data(new_user)

        self.stop_loading()

        if not bln:
            alert_sistem(response, bln)
            return
        else:
            bln, response = criar_usuario(new_user)
            if bln:
                alert_sistem(response, bln)
                return
            else:
                alert_sistem(response, bln)
                return



if __name__ == "__main__":
    app = Aplication()
    app.mainloop()