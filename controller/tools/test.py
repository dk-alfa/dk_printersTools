from controller.database.table_devices import TableDevices
from controller.database.table_printer_counters import TablePrinterCounters
import datetime
import dictionary.dic_varior as VARIOR

class Test:
    def test_table_printer_counters(self,date):
        ret = []

        t_printer_counters = TablePrinterCounters
        id_devices_in_t_printers_counters = t_printer_counters.get_id_devices_by_date(self,date)

        if len(id_devices_in_t_printers_counters):
            device_type = (VARIOR.DEVICE_TYPE_PRINTER, VARIOR.DEVICE_TYPE_MFU)
            t_devices = TableDevices
            id_devices_in_t_devices = t_devices.get_devices_id_by_device_type(self, device_type)
            set_id_devices_in_t_devices = set(id_devices_in_t_devices)
            set_id_devices_in_t_printers_counters = set(id_devices_in_t_printers_counters)

            set_div = set_id_devices_in_t_devices-set_id_devices_in_t_printers_counters
            list_div = list(set_div)

            if list_div:
                list_div.sort()
                tuple_div = tuple(list_div)
                device_list = t_devices.get_devices_list_by_devices_id(self,tuple_div)
                if device_list:
                    for item in device_list:
                        ret.append({
                            'id_device'   : f'{item["id_device"]}',
                            'ip_address'  : f'{item["ip_address"]}',
                            'device_model': f'{item["device_model"]}',
                            'device_name' : f'{item["device_name"]}',
                                    })
        else: ret = None
        return ret
