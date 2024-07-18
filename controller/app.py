import argparse
from   controller.device.printer import Printers
from   controller.tools.report   import Report
from   controller.tools.test     import Test
from   controller.tools.log      import Log

import dictionary.dic_error      as ERROR
import dictionary.dic_varior     as VARIOR
import dictionary.dic_message    as MESSAGE

class App:
    def run(self, args):
        if len(args) == 1:
            print(ERROR.APP_ARG_COUNT)
        else: self.__run_app(self,args)
    def __run_app(self,args):
        arg_list = self.__parse_arguments(self,args)
        if arg_list: self.__execute_app(self,arg_list)
    def __parse_arguments(self,args):
        arg_list = []
        parser = argparse.ArgumentParser()
        parser.add_argument(VARIOR.ARG_VERSION_SHORT, VARIOR.ARG_VERSION_LONG, help=MESSAGE.ARG_VERSION_HELP, action="store_true")
        parser.add_argument(VARIOR.ARG_PRINTERS_PAGES_COUNTER_SHORT, VARIOR.ARG_PRINTERS_PAGES_COUNTER_LONG,
                            help=MESSAGE.ARG_PRINTERS_PAGES_COUNTER,action="store_true")
        parser.add_argument(VARIOR.ARG_PRINTERS_PAGES_REPORT_SHORT, VARIOR.ARG_PRINTERS_PAGES_REPORT_LONG,
                            help=MESSAGE.ARG_PRINTERS_PAGES_REPORT, nargs=2, metavar=('start_date','end_date'), action='append' )
        parser.add_argument(VARIOR.ARG_PRINTERS_PAGES_TEST_SHORT, VARIOR.ARG_PRINTERS_PAGES_TEST_LONG,
                            help=MESSAGE.ARG_PRINTERS_PAGES_TEST, nargs='?', metavar=('date_test'), const='now',action="append")

        app_args = parser.parse_args()

        if app_args.version     : arg_list.append({"arg_name": f"{VARIOR.ARG_VERSION_LONG}"})
        if app_args.saveprncntrs: arg_list.append({"arg_name": f"{VARIOR.ARG_PRINTERS_PAGES_COUNTER_LONG}"})
        if app_args.repprncntrs : arg_list.append({"arg_name": f"{VARIOR.ARG_PRINTERS_PAGES_REPORT_LONG}","dates":app_args.repprncntrs[0]})
        if app_args.testprncntrs: arg_list.append({"arg_name": f"{VARIOR.ARG_PRINTERS_PAGES_TEST_LONG}","date":app_args.testprncntrs[0]})

        return  arg_list
    def __execute_app(self,arg_list):
        the_arg_list = []
        for item in arg_list:
            the_arg_list.append(item["arg_name"])

        if VARIOR.ARG_VERSION_LONG in the_arg_list:  print(MESSAGE.APP_VERSION)
        if VARIOR.ARG_PRINTERS_PAGES_COUNTER_LONG in the_arg_list: self.__run_get_counters(self)
        if VARIOR.ARG_PRINTERS_PAGES_REPORT_LONG  in the_arg_list: self.__run_report(self,arg_list)
        if VARIOR.ARG_PRINTERS_PAGES_TEST_LONG    in the_arg_list: self.__run_test(self,arg_list)
    def __run_get_counters(self):
        priners = Printers
        priners.get_counters(self)
    def __run_report(self,arg_list):
        for item in arg_list:
            if 'dates' in item:
                report = Report
                # report_str = report.get_printers_counts_report_long(self, item['dates'])
                report_str = report.get_printers_counts_report_short(self, item['dates'])
                print(report_str)
    def __run_test(self,arg_list):
        log_level = VARIOR.LOG_LEVEL_ERROR
        log_message = 'Не удалось запустить тест : ошибка App.__run_test(self,arg_list)'
        for item in arg_list:
            if 'date' in item:
                test = Test
                log_result = test.test_table_printer_counters(self, item['date'])
                log_message = ''
                if log_result == None:
                    log_message = f'{MESSAGE.INFO_PRINTERS_COUNTERS_LIST_IS_EMPTY} за {item["date"]}'
                else:
                    if log_result:
                         if len(log_result):
                             log_message_header = f'{MESSAGE.INFO_PRINTERS_COUNTERS_NOT_FOUND}\n'
                             log_message_body= ''
                             c = 0
                             for item in log_result:
                                 c += 1
                                 log_message_body += f'{c}: [{item["id_device"]}] {item["ip_address"]} {item["device_model"]} {item["device_name"]}\n'
                             log_message = log_message_header + log_message_body
                    else:
                        log_level = VARIOR.LOG_LEVEL_INFO
                        log_message = f'{MESSAGE.INFO_PRINTERS_COUNTERS_ALL_FOUND}'
        print(log_message)
        log = Log
        log.create_log(self,log_level,log_message,VARIOR.LOG_TO_EMAIL)




