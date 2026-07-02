import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from PIL import Image, ImageTk

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

    messagebox.showinfo(
        "Sucesso!",
        f"{msg}"
    )

def login():
    alert_sistem("Muito bem dev!", True)


class Aplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.configure(
            fg_color = "#6b6d6a"
        )

        self.image_types = None

        self.title('Sistema de Cobranças')
        self.geometry("420x500")
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
        logo.pack(pady=(10, 10))

        title = ctk.CTkLabel(
            self.container,
            text="Login",
            font=("Arial", 40, "bold")
        )
        title.pack(pady=(8, 8))

        title = ctk.CTkLabel(
            self.container,
            text="Se não tiver cadastro por favor\ninsira as informações e clique em REGISTRAR!",
            font=("Arial", 12, "bold")
        )
        title.pack(pady=(5, 5))

        labeName = ctk.CTkLabel(
            self.container,
            text="Nome de Usuário:"
        )
        labeName.pack()

        username = ctk.CTkEntry(
            self.container,
            width=200,
            height=40
        )
        username.pack()

        LabelPassw = ctk.CTkLabel(
            self.container,
            text="Senha:"
        )
        LabelPassw.pack()

        password = ctk.CTkEntry(
            self.container,
            width=200,
            height=40,
            show="*",
            border_color="#6b6d6a"
        )
        password.pack()

        btn_login = ctk.CTkButton(
            self.container,
            text="Automatizar agora!",
            fg_color="#fc3a51",
            hover_color="#b12a3a",
            text_color="white",
            width=200,
            height=40,
            command=login
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
            command=""
        )
        btn_register.pack(pady=10)




if __name__ == "__main__":
    app = Aplication()
    app.mainloop()