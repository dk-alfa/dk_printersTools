import dictionary.dic_varior as VARIOR
import psycopg2

class TableDevices:
    __connection = None
    def __init__(self):
        print('init')
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
    def get_devices_list(self,device_types):
        ret = []
        query_list =  None
        try:
            connection = TableDevices.__init_table()
            if connection:
                with connection.cursor() as cursor:
                    sql_str = f'SELECT ' \
                              f'd.id,d.ip_address, ' \
                              f'a.login, ' \
                              f'a.password, ' \
                              f'm.name, ' \
                              f'v.name ' \
                              f'FROM ' \
                              f'device as d, ' \
                              f'device_auth as a, ' \
                              f'device_model as m, ' \
                              f'device_vendor as v, ' \
                              f'device_type as t ' \
                              f'WHERE ' \
                              f'd.id_device_auth = a.id and ' \
                              f'd.id_device_model = m.id and ' \
                              f'm.id_device_vendor = v.id and ' \
                              f'm.id_device_type = t.id and ' \
                              f'd.enable and ' \
                              f't.id in {device_types} and ' \
                              f'd.networked '\
                              f'order by d.id;'
                    try:
                        cursor.execute(sql_str)
                        query_list = cursor.fetchall()
                        for record in query_list:
                            ret.append({'ip_address': f'{record[1]}','login':f'{record[2]}','password':f'{record[3]}',
                                        'id_device': f'{record[0]}','device_model':f'{record[5]}_{record[4]}'})
                    except Exception as _ex :
                        print(f"[ERROR] Ошибка в модуле [(tabledevices.py) "
                              f"TableDevices.get_devices_list] не удалось выполнить запрос {sql_str} {_ex}")
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_devices.py) TableDevices.get_devices_list()] {_ex}")
        return ret
    def get_devices_id_by_device_type(self,device_types):
        ret = []
        query_list = None
        try:
            connection = TableDevices.__init_table()
            if connection:
                with connection.cursor() as cursor:
                    sql_str = f'SELECT ' \
                              f'd.id ' \
                              f'FROM ' \
                              f'device d ' \
                              f'JOIN device_model m ON d.id_device_model = m.id ' \
                              f'JOIN device_type t ON m.id_device_type = t.id ' \
                              f'WHERE ' \
                              f'd.enable = true and ' \
                              f'm.id_device_type IN {device_types} ' \
                              f'ORDER BY d.id ' \
                              f';'
                    try:
                        cursor.execute(sql_str)
                        query_list = cursor.fetchall()
                        for record in query_list:
                            ret.append(record[0])
                        #     ret.append({'id_device': f'{record[0]}'})
                    except Exception as _ex :
                        print(f"[ERROR] Ошибка в модуле [(table_devices.py) "
                              f"TableDevices.get_devices_list] не удалось выполнить запрос {sql_str} {_ex}")
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(tabledevices.py) TableDevices.get_devices_id_by_device_type()] {_ex}")
        return ret
    def get_devices_list_by_devices_id(self,devices_id):
        ret = []
        query_list = None
        try:
            connection = TableDevices.__init_table()
            if connection:
                with connection.cursor() as cursor:
                    sql_str = f'SELECT ' \
                              f'd.id,d.ip_address, ' \
                              f'a.login, ' \
                              f'a.password, ' \
                              f'm.name, ' \
                              f'v.name, ' \
                              f'd.name ' \
                              f'FROM ' \
                              f'device as d, ' \
                              f'device_auth as a, ' \
                              f'device_model as m, ' \
                              f'device_vendor as v, ' \
                              f'device_type as t ' \
                              f'WHERE ' \
                              f'd.id_device_auth = a.id and ' \
                              f'd.id_device_model = m.id and ' \
                              f'm.id_device_vendor = v.id and ' \
                              f'm.id_device_type = t.id and ' \
                              f'd.enable and ' \
                              f'd.id in {devices_id} and ' \
                              f'd.networked ' \
                              f'order by d.id;'
                    try:
                        pass
                        cursor.execute(sql_str)
                        query_list = cursor.fetchall()
                        for record in query_list:
                            ret.append(
                                {'ip_address': f'{record[1]}', 'login': f'{record[2]}', 'password': f'{record[3]}',
                                 'id_device': f'{record[0]}', 'device_model': f'{record[5]}_{record[4]}','device_name':f'{record[6]}'})
                    except Exception as _ex:
                        print(f"[ERROR] Ошибка в модуле [(tabledevices.py) "
                              f"TableDevices.get_devices_list] не удалось выполнить запрос {sql_str} {_ex}")
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_devices.py) TableDevices.get_devices_list()] {_ex}")
        return ret
    def get_device_by_dic(self,dict):
        in_str = ''
        for item in dict:
            in_str += f' d.{item} = {dict.get(item)} and '
        ret = []
        query_list = None
        try:
            connection = TableDevices.__init_table()
            if connection:
                with connection.cursor() as cursor:
                    sql_str = f'SELECT ' \
                              f'd.id,d.ip_address, ' \
                              f'a.login, ' \
                              f'a.password, ' \
                              f'm.name, ' \
                              f'v.name ' \
                              f'FROM ' \
                              f'device as d, ' \
                              f'device_auth as a, ' \
                              f'device_model as m, ' \
                              f'device_vendor as v, ' \
                              f'device_type as t ' \
                              f'WHERE ' \
                              f'd.id_device_auth = a.id and ' \
                              f'd.id_device_model = m.id and ' \
                              f'm.id_device_vendor = v.id and ' \
                              f'm.id_device_type = t.id and ' \
                              f'{in_str}' \
                              f'd.enable and ' \
                              f'd.networked ' \
                              f'order by d.id;'
                    try:
                        cursor.execute(sql_str)
                        query_list = cursor.fetchall()
                        for record in query_list:
                            ret.append(
                                {'ip_address': f'{record[1]}', 'login': f'{record[2]}', 'password': f'{record[3]}',
                                 'id_device': f'{record[0]}', 'device_model': f'{record[5]}_{record[4]}'})
                    except Exception as _ex:
                        print(f"[ERROR] Ошибка в модуле [(tabledevices.py) "
                              f"TableDevices.get_devices_list] не удалось выполнить запрос {sql_str} {_ex}")
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(table_devices.py) TableDevices.get_devices_list()] {_ex}")
        return ret


