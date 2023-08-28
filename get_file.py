import requests
import json
import re
from datetime import date


def auth():
    with open('auth.json', 'r', encoding='utf-8') as file1:
        auth1 = json.load(file1)
    return auth1


def get_file():
    auth1 = auth()

    s = requests.Session()
    log = s.post(auth1['path'], data=auth1['log'])

    if 'Прайс' in log.text:
        print('Авторизация прошла успешно!')
    else:
        print('Ошибка авторизации')

    response = s.get(auth1['path'].replace('login.php', 'inc/price.php?fotos&zakup=-1&excel'))
    match = re.search(r"(print/stat/.*?\.xls)", response.text)
    url3 = s.get(auth1['path'].replace('login.php', '') + match.group())

    today = date.strftime(date.today(), "%d-%m-%Y")

    with open(f'files/import_from_site/original/{today}.xls', "wb") as f:
        f.write(url3.content)

    print(f'Файл {match.group()} выгружен')
