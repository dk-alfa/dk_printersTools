import sys
APP_VERSION     = 'dk_printersTools 1.0.1 2024.07.12 Writen by Dmitry Korablev'
ARG_VERSION_HELP= 'Показать версию'
ARG_PRINTERS_PAGES_COUNTER = 'Сохранить счетчики принтеров'
ARG_PRINTERS_PAGES_REPORT = f'Создать отчет пример: python {sys.argv[0]} -rpc 2024-07-09 2024-07-10'
ARG_PRINTERS_PAGES_TEST = f'Тест таблицы "счетчики принтеров"  пример: python {sys.argv[0]} -tpc 2024-07-09 , если аргумента нет, то выбирается текщая дата'
INFO_PRINTERS_LIST_IS_EMPTY = '[INFO] Список принтеров пуст'
