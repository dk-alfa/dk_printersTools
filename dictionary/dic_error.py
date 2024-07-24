import sys

APP_ARG_COUNT       = f'[ERROR] Необходимо запускать скрипт с аргументами: python {sys.argv[0]} -h'
CANT_CREATE_PRINTER = '[ERROR] Не удалось создать объект  Printer'
DATE_ERROR = 'Введите дату в правильном формате: YYYY-MM-DD [2024-07-19]'
ARG_PARCE_SPC_ERROR = 'С аргументом "-spc" нужно использовать опции id=[число] либо ip=[ip адрес] пример -spc id=12, -spc ip=172.16.1.231 '
ARG_PARCE_SPC_ID_ERROR = 'c опцией "id="  нужно использовать число пример id=12'
ARG_PARCE_SPC_IP_ERROR = 'c опцией "ip="  нужно использовать ipv4 адрес правильного формата пример: ip=172.16.1.231'