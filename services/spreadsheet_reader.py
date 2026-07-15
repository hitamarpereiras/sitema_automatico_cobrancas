import pandas as pd
import os
from time import sleep


class ExcelService:
    def __init__(self, path_xlsx):
        self.df = pd.read_excel(path_xlsx)

        self.df["Data_Vencimento"] = pd.to_datetime(
            self.df["Data_Vencimento"]
        )

    def clientes(self):

        return self.df.iterrows()

excel = ExcelService(os.path.join("database", "clientes_.xlsx"))

for _, cliente in excel.clientes():
    print(cliente["Nome"])
    print(cliente["Data_Vencimento"])
