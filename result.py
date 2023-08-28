import pandas as pd
from datetime import date, timedelta
import os


def find_date():
    today = date.strftime(date.today(), "%d-%m-%Y")
    file2_path = f"files/import_from_site/new/{today}.xlsx"
    file_names = os.listdir("files/import_from_site/new")
    file1_path = ''

    i = 1
    while True:
        if f'{date.strftime(date.today() - timedelta(days=i), "%d-%m-%Y")}.xlsx' not in file_names:
            i += 1
            if i >= 365:
                raise ValueError("Ты забил болт? нужны свежие файлы")
            continue
        else:
            file1_path = f"files/import_from_site/new/{date.strftime(date.today() - timedelta(days=i), '%d-%m-%Y')}.xlsx"
            break

    print(file1_path)
    print(file2_path)
    return file1_path, file2_path


def result():
    file2_path, file1_path = find_date()

    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    # Сравнение и создание списков новых товаров
    new_in_file1 = df1[~df1['ID'].isin(df2['ID'])]
    new_in_file2 = df2[~df2['ID'].isin(df1['ID'])]
    new_in_file3 = df1[df1['Цена'] % 10 < 9]

    # Создание новых листов
    with pd.ExcelWriter('files/результат.xlsx') as writer:
        insert_index = df1.columns.get_loc('Цена') + 1
        df1.insert(insert_index, 'ОК-Цена', df1['Цена'] % 10)
        df1.insert(df1.columns.get_loc('Ц.пост.2') + 1, 'Сумма', df1['Ц.пост.2'] * df1['Кол.'])
        df1.to_excel(writer, sheet_name='Общий список', index=False)
        new_in_file2.to_excel(writer, sheet_name='Продано', index=False)
        new_in_file1.to_excel(writer, sheet_name='Новое', index=False)
        new_in_file3.to_excel(writer, sheet_name='Расценка', index=False)
