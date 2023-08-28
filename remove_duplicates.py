import pandas as pd
import OleFileIO_PL
from datetime import date


def remove_duplicates():
    today = date.strftime(date.today(), "%d-%m-%Y")

    with open(f'files/import_from_site/original/{today}.xls', 'rb') as file:
        ole = OleFileIO_PL.OleFileIO(file)
        if ole.exists('Workbook'):
            d = ole.openstream('Workbook')
            excel = pd.read_excel(d, engine='xlrd')

    excel.drop_duplicates(subset=['ID'], inplace=True)

    excel.sort_values(by=['Категория', 'Бренд', 'Модель'], inplace=True)

    excel.to_excel(f'files/import_from_site/new/{today}.xlsx', index=False)
