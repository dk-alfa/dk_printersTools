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
    def save_to_table(self, fields, data):

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
        # print(f'{fields} {data}')
        # conn = v_reg_tmp.__init_table()
        # if conn:
        #     with conn.cursor() as cursor:
        #         for item in cam_list:
        #             sql_str = f"INSERT INTO v_reg_tmp ({field_list}) VALUES ({item[0]},'{item[1]}',{item[2]},'{item[3]}','{item[4]}','{item[6]}','{item[7]}');"
        #             try:
        #                 cursor.execute(sql_str)
        #             except Exception as _ex:
        #                 print(f"[ERROR] Ошибка в модуле [(table_v_reg_tmp.py) v_reg_tmp.save_to_table()"
        #                           f"] не удалось выполнить запрос {sql_str} : {_ex}")