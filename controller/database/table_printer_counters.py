import datetime
import dictionary.dic_varior as VARIOR
import psycopg2

class TablePrinterCounters:
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
            connection = TablePrinterCounters.__init_table()
            if connection:
                with connection.cursor() as cursor:
                    try:
                        cursor.execute(sql_str)
                    except Exception as _ex:
                        print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) "
                              f"table_printer_counters.save_to_table_by_dict()] не удалось выполнить запрос {sql_str} {_ex}")
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) table_printer_counters.save_to_table_by_dict()] {_ex}")
    def get_report_by_two_dates(self,date):
        ret = None
        try:
            connection = TablePrinterCounters.__init_table()
            if connection:
                with connection.cursor() as cursor:
                    try:
                        sql_str = f"" \
                                  f"SELECT " \
                                    f"p.id_device , " \
                                    f"min(p.date_created), " \
                                    f"max(p.date_created), " \
                                    f"min(p.print_copy), " \
                                    f"max(p.print_copy), " \
                                    f"min(p.print_print), " \
                                    f"max(p.print_print), " \
                                    f"min(p.print_sum), " \
                                    f"max(p.print_sum), " \
                                    f"min(p.scan_copy), " \
                                    f"max(p.scan_copy), " \
                                    f"min(p.scan_over), " \
                                    f"max(p.scan_over), " \
                                    f"min(p.scan_sum), " \
                                    f"max(p.scan_sum), " \
                                    f"max(d.name), " \
                                    f"max(d.ip_address), " \
                                    f"max(m.name)," \
                                    f"max(v.name)," \
                                    f"max(c.name) " \
                                  f"FROM " \
                                    f"printer_counters p " \
                                  f"JOIN device d ON p.id_device = d.id " \
                                  f"JOIN device_model m ON d.id_device_model = m.id " \
                                  f"JOIN device_vendor v ON m.id_device_vendor = v.id " \
                                  f"JOIN printer_cartridge_property c ON m.id_over = c.id " \
                                  f"WHERE p.date_created BETWEEN to_timestamp('{date[0]} 00:00','YYYY-MM-DD HH24:MI') " \
                                    f" and to_timestamp('{date[1]} 23:59','YYYY-MM-DD HH24:MI') " \
                                  f"GROUP BY p.id_device " \
                                  f"ORDER BY p.id_device;"
                        # print(sql_str)
                        cursor.execute(sql_str)
                        response = query_list = cursor.fetchall()
                        if response: ret = response
                        # for item in response:
                        #     print(item)
                            # str1 = item[5].encode('utf8')
                            # print(item[0], f"[{item[1].strftime('%Y-%m-%d %H:%M')}]",f"[{item[2].strftime('%Y-%m-%d %H:%M')}],"\
                            #       f" {item[3]}, {item[4]}, print dif:{item[4] - item[3]}, {item[5]}, {item[6]}, {item[8]}_{item[7]} {item[11]}")
                    except Exception as _ex:
                        print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) "
                              f"table_printer_counters.get_reports_by_two_dates(self,dates)] не удалось выполнить запрос {sql_str} {_ex}")
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) "
                  f"table_printer_counters.get_reports_by_two_dates(self,dates)] {_ex}")
        return ret
    def get_id_devices_by_date(self,date):
        ret = []
        if date == 'now':
            date = datetime.datetime.now()
        else: date = datetime.datetime.strptime(date, "%Y-%m-%d")
        date_from = date.strftime("%Y-%m-%d 00:00")
        date_to  =  date.strftime("%Y-%m-%d 23:59")
        try:
            connection = TablePrinterCounters.__init_table()
            if connection:
                with connection.cursor() as cursor:
                    try:
                        sql_str = f"" \
                                  f"SELECT " \
                                    f"p.id_device " \
                                  f"FROM " \
                                    f"printer_counters p " \
                                  f"WHERE " \
                                    f"p.date_created BETWEEN to_timestamp('{date_from}','YYYY-MM-DD HH24:MI') " \
                                    f"and to_timestamp('{date_to}','YYYY-MM-DD HH24:MI')  " \
                                  f"GROUP BY p.id_device " \
                                  f"ORDER BY p.id_device;"
                        # print(sql_str)
                        cursor.execute(sql_str)
                        query_list = cursor.fetchall()
                        for record in query_list:
                            ret.append(record[0])
                    except Exception as _ex:
                        print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) "
                              f"table_printer_counters.get_id_devices_by_date(self,date)] не удалось выполнить запрос {sql_str} {_ex}")
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_printer_counters.py) "
                  f"table_printer_counters.get_id_devices_by_date(self,date)] {_ex}")
        return ret

