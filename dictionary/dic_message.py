import sys
APP_VERSION     = 'dk_printersTools 1.0.6 2024.10.28 Writen by Dmitry Korablev'
ARG_VERSION_HELP= 'Показать версию'
ARG_PRINTERS_PAGES_COUNTER = f'Сохранить счетчики принтеров пример: [python] {sys.argv[0]} -spc id=28 или [python] {sys.argv[0]} -spc ip=172.16.1.231'
ARG_PRINTERS_PAGES_REPORT = f'Создать отчет пример: [python] {sys.argv[0]} -rpc 2024-07-09 2024-07-10'
ARG_PRINTERS_PAGES_TEST = f'Тест таблицы "счетчики принтеров"  пример: [python] {sys.argv[0]} -tpc 2024-07-09 , если аргумента нет, то выбирается текщая дата'
ARG_SENND_EMAIL = f'Отправить e-mail из таблицы log за дату пример: [python] {sys.argv[0]} -se 2024-07-19 , если аргумента нет, то выбирается текщая дата'

INFO_PRINTERS_LIST_IS_EMPTY = '[INFO] Список принтеров пуст'
INFO_PRINTERS_COUNTERS_LIST_IS_EMPTY = 'Не найдено ни одной записи о счетчиках принтеров'
INFO_PRINTERS_COUNTERS_NOT_FOUND =     'Не найдены записи о счетчиках следующих принтеров:'
INFO_PRINTERS_COUNTERS_ALL_FOUND =     'Найдены записи обо всех счетчиках принтеров'

EMAIL_MESSAGE_IS_SEND = "Сообщение отправлено"
