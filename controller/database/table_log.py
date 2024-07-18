import dictionary.dic_varior as VARIOR
import psycopg2

class TableLog:
    __connection = None
    def __init__(self):
        connection = None
        try:
            connection = psycopg2.connect(
                dbname=VARIOR.DB_NAME,
                user=VARIOR.DB_USER,
                password=VARIOR.DB_PASS,
                host=VARIOR.DB_HOST)
            connection.autocommit = True
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_log.py) log.__init__(self)] {_ex}")
        self.__connection = connection
    def create_log_by_dict(self,dict):
        fields = ''
        data   = ''
        for item in dict.keys():
            fields = fields + f'{item},'
        fields = fields[:-1]
        for item in dict.values():
            data = data + f'{item},'
        data = data[:-1]
        sql_str = f'INSERT INTO log ({fields}) VALUES ({data});'

        if self.__connection:
            try:
                with self.__connection.cursor() as cursor:
                    try:
                        cursor.execute(sql_str)
                    except Exception as _ex:
                        print(f"[ERROR] Ошибка в модуле [(table_log.py) "
                              f"table_log.create_log_by_dict()] не удалось выполнить запрос {sql_str} {_ex}")
            except Exception as _ex:
                print(f"[ERROR] Ошибка в модуле [((table_log.py) table_log.create_log_by_dict()] {_ex}")
        else: print(f"[ERROR] Ошибка в модуле [((table_log.py) table_log.create_log_by_dict()] Нет соединения с таблицей log")

