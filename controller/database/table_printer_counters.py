import dictionary.dic_varior as VARIOR
import psycopg2

class table_printer_counters:
    def __init_table():
        connection = None
        try:
            connection = psycopg2.connect(
                dbname=VARIOR.DB_NAME,
                user=VARIOR.DB_USER,
                password=VARIOR.DB_PASS,
                host=VARIOR.DB_HOST)
            connection.autocommit = True
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) table_printer_counters.__init_table()] {_ex}")
        # finally: print(f"[INFO] (table_v_reg_tmp.py) v_reg_tmp.__init_table() соединение с базой установлено")
        return connection
    def save_to_table_by_fields_data(self, fields, data):

        try:
            connection = table_printer_counters.__init_table()
            if connection :
                with connection.cursor() as cursor:
                    sql_str = f'INSERT INTO printer_counters ({fields}) VALUES ({data});'
                    try:
                        cursor.execute(sql_str)
                    except Exception as _ex :
                        print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) "
                              f"table_printer_counters.save_to_table()] не удалось выполнить запрос {sql_str} {_ex}")

        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) table_printer_counters.save_to_table()] {_ex}")
    def save_to_table_by_dict(self,dict):
        fields = ''
        data   = ''
        for item in dict.keys():
            fields = fields + f'{item},'
        fields = fields[:-1]
        for item in dict.values():
            data = data + f'{item},'
        data = data[:-1]
        sql_str = f'INSERT INTO printer_counters ({fields}) VALUES ({data});'
        try:
            connection = table_printer_counters.__init_table()
            if connection:
                with connection.cursor() as cursor:
                    try:
                        cursor.execute(sql_str)
                    except Exception as _ex:
                        print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) "
                              f"table_printer_counters.save_to_table_by_dict()] не удалось выполнить запрос {sql_str} {_ex}")
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) table_printer_counters.save_to_table_by_dict()] {_ex}")
