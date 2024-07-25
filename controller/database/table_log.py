import dictionary.dic_varior as VARIOR
import psycopg2
import datetime

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
    def read_log_by_date(self,date):
        ret = []
        date_from = f'{date} 00:00'
        date_to   = f'{date} 23:59'
        sql_str = f"SELECT " \
                  f"l.message, " \
                  f"s.name log_subject, " \
                  f"ll.name log_level, " \
                  f"l.date_created " \
                  f"FROM " \
                    f"log l " \
                  f"JOIN log_subject s ON l.id_log_subject = s.id " \
                  f"JOIN log_level ll ON l.id_log_level = ll.id " \
                  f"WHERE " \
                    f"l.to_email and " \
                    f"l.date_created " \
                    f"BETWEEN " \
                    f"to_timestamp('{date_from}','YYYY-MM-DD HH24:MI') and " \
                    f"to_timestamp('{date_to}','YYYY-MM-DD HH24:MI') " \
                    f"ORDER BY l.date_created" \
                  f";"
        if self.__connection:
            try:
                with self.__connection.cursor() as cursor:
                    try:
                        cursor.execute(sql_str)
                        query_list = cursor.fetchall()
                        for record in query_list:
                            ret.append({'message': f'{record[0]}','log_subject':f'{record[1]}','lavel':f'{record[2]}',
                                        'date_created':f'{str(record[3])[:-10]}'})
                    except Exception as _ex:
                        print(f"[ERROR] Ошибка в модуле [(table_log.py) "
                              f"table_log.create_log_by_dict()] не удалось выполнить запрос {sql_str} {_ex}")
            except Exception as _ex:
                print(f"[ERROR] Ошибка в модуле [((table_log.py) table_log.read_log_by_date] {_ex}")
        else: print(f"[ERROR] Ошибка в модуле [((table_log.py) table_log.read_log_by_date] Нет соединения с таблицей log")
        return ret

