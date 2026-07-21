import os
import customtkinter as ctk

from ui.login import LoginFrame
from ui.dashboard import DashboardFrame


ctk.set_appearance_mode("dark")


class Application(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Sistema de Cobranças")

        self.geometry("420x560")

        self.resizable(False, False)

        self.configure(
            fg_color="#6b6d6a"
        )

        self.iconbitmap(
            os.path.join(
                "assets",
                "icon_window.ico"
            )
        )

        self.current_frame = None

        self.show_login()


    # LOGIN


    def show_login(self):

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = LoginFrame(
            self,
            self.show_dashboard
        )


    # DASHBOARD


    def show_dashboard(self, user):

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.geometry("700x650")

        self.current_frame = DashboardFrame(
            self
        )

        # Depois vamos utilizar esse usuário
        # para preencher o último acesso
        self.current_frame.user = user


if __name__ == "__main__":

    app = Application()

    app.mainloop()