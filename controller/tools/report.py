import controller.database.table_printer_counters as T_PRINTER_COUNTERS
import datetime

class Report:
    def get_printers_counts_report_short(self, dates):
        ret = None
        try:
            t_printer_counters = T_PRINTER_COUNTERS.TablePrinterCounters
            delimiter = '---------------------------------------------------------------------------------------------------------------------------------\n'
            report_query = t_printer_counters.get_report_by_two_dates(self,dates)
            ret_str_header = f'Отчет о счетчиках принтеров за период с {dates[0]} по {dates[1]} ' \
                             f'дата генерации отчета {str(datetime.datetime.now())[:-10]}\n' \
                             f'{delimiter}' \
                             f'id  |Название                   |ip адрес       |п.к. |п.п. |п.с. |c.к. |с.д. |с.с. |Примечание\n' \
                             f'{delimiter}'
            ret_str_body = ''
            sum1 = 0
            sum2 = 0
            sum3 = 0
            sum4 = 0
            sum5 = 0
            sum6 = 0


            print(report_query[0])
            for item in report_query:
                name = f'{item[18]}_{item[17]}'
                sum1 = sum1+ int(item[4] - item[3])
                sum2 = sum2+ int(item[6] - item[5])
                sum3 = sum3+ int(item[8] - item[7])
                sum4 = sum4+ int(item[10] - item[9])
                sum5 = sum5+ int(item[12] - item[11])
                sum6 = sum6+ int(item[14] - item[13])

                ret_str_body = f'{ret_str_body} {str(item[0]).ljust(3)}|' \
                               f'{name.ljust(27)}|' \
                               f'{item[16].ljust(15)}|' \
                               f'{str(item[4]-item[3]).ljust(5)}|' \
                               f'{str(item[6]-item[5]).ljust(5)}|' \
                               f'{str(item[8]-item[7]).ljust(5)}|' \
                               f'{str(item[10]-item[9]).ljust(5)}|' \
                               f'{str(item[12]-item[11]).ljust(5)}|' \
                               f'{str(item[14]-item[13]).ljust(5)}|' \
                               f'{item[15]}' \
                               f'\n' \
                               f'{delimiter}'
            ret_str_footer = f'                                        ИТОГО:  ' \
                             f'|{str(sum1).ljust(5)}|{str(sum2).ljust(5)}|{str(sum3).ljust(5)}|' \
                             f'{str(sum4).ljust(5)}|{str(sum5).ljust(5)}|{str(sum6).ljust(5)}|\n'
            ret_str_footer = ret_str_footer + \
                             '* п.к: принтер копирование, п.п.: принтер печать, п.с: принтер суммарно \n' \
                             '  с.к: сканер  копирование, с.д.: сканер другое,  с.с: сканер суммарно '
            ret = ret_str_header + ret_str_body + ret_str_footer
        except Exception as _ex:
            print(f"[ERROR] Ошибка в модуле [(report.py) get_printers_counts_report_short(self, dates) "
                  f"не удалось создать таблицу {_ex}")
        return ret
    def get_printers_counts_report_long(self, dates):
        ret = None
        return ret
