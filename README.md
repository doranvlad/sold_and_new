# Контроль остатков

Контроль остатков на складе для более понятного и эффективного
распоряжения финансовыми ресурсами компании.<br>
Программа сравнивает остатки за прошлый период (прошлая выгрузка остатков не старше 365 дней).<br>
Лично я использую для формирования 4-х листов анализа:
- Общий список - все товары, которые сейчас на остатках
- Продано - товары, которые продались их можно исключить из акции и тд.
- Новое - товары, которые появились на остатках, надо проработать цены, акции и тд.
- Расценка - у меня все товары идут с ценой 9-ка в конце, если ее там нет
то это значит что слетела цена или вообще не трогалась.

## Что умеет

- Логин на сайте, выгрузка файла с остатками - get_file.py
- Удаление дубликатов (особенности импорта) - remove_duplicates.py
- Сравнение периодов, формирование результата анализа