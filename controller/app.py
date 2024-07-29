"""Класс App
Написано Дмитрием Кораблевым инженером отдела IT ООО Альфа-Сервис
Дата первого коммита 2024-07-26

App содержит следующие методы:
    run(self, args)              запуск приложения
    __parse_arguments(self,args) парсинг аргументов
    __execute_app(self,arg_list) выполнение приложения
              метод                     описание                            ключ запуска
    --------------------------------------------------------------------------------------------------

    __run_get_counters           опрос и сохранение счетчиков принтеров -spc (Save Printers Counters)
    __run_report                 сделать отчет                          -rpc (Report Printers Counters)
    __run_test                   запустить тест                         -tpc (Test Printers Counters)
    __run_send_email             отправить логи на e-mail               -se  (Send E-mail)
"""

import argparse
import datetime
import time
import re

from   controller.device.printer import Printers
from   controller.tools.report   import Report
from   controller.tools.test     import Test
from   controller.tools.log      import Log
from   controller.tools.email    import Email
import dictionary.dic_error      as ERROR
import dictionary.dic_varior     as VARIOR
import dictionary.dic_message    as MESSAGE
import controller.tools.over     as over

class App:
    """
    Класс приложение
    """
    def run(self, args):
        """
        Метод: запуск приложения
        Проверка на наличие аргументов, парсинг аргументов, выпонение приложения
        :param args : аргументы командной строки
        :return     : Ничего
        """
        if len(args) == 1:
            print(ERROR.APP_ARG_COUNT)
        else:
            arg_list = self.__parse_arguments(self, args)
            if arg_list: self.__execute_app(self, arg_list)
    def __parse_arguments(self,args):
        """
        Метод: парсинг аргументов
        Создание списка аргументов командной строки для дальнейшей работы с этим списком
        возможные значения:
            -h      help по аргументам
            -v      показать версию приложения
            -spc [options] (Save Printers Counters) сохранить счетчики принтеров
                options:
                    все действия производятся за текщую дату дата в формате 2024-07-26
                    [отсутствуют]: производится сохранение всех счетчиков в таблицу printers_counters
                    [id=] сохранение счетчиков принтера по его id в таблице devices
                    [ip=] сохранение счетчиков принтера по его ip
            -rpc [options] (Report Printers Counters) очеты о счетчиках принтеров
                options:
                    [date start date end] начальная и конечная дата за которые нужно создать отчет
            -tpc [options] (Test Printers Counters) тест таблицы printers_counters на наличие записей обо всех
                           принтерах/МФУ присутствующих в таблице devices
                    [отсутствуют]: тест за текущую дату
                    [date_tpc]  : тест за date test
            -se  [options] (Send E-mail) передать данные из таблицы log за такю то дату на e-mail
                  options:
                    [отсутствуют]: передаются логи за текущую дату
                    [date_se]    : передаются логи за date_se
        :param args : args аргументы командной строки
        :return     : arg_list - список аргументов
        """
        arg_list = []
        parser = argparse.ArgumentParser()
        parser.add_argument(VARIOR.ARG_VERSION_SHORT, VARIOR.ARG_VERSION_LONG, help=MESSAGE.ARG_VERSION_HELP, action="store_true")
        parser.add_argument(VARIOR.ARG_PRINTERS_PAGES_COUNTER_SHORT, VARIOR.ARG_PRINTERS_PAGES_COUNTER_LONG,
                            help=MESSAGE.ARG_PRINTERS_PAGES_COUNTER,nargs='?',metavar=('options'),action="append")

        parser.add_argument(VARIOR.ARG_PRINTERS_PAGES_REPORT_SHORT, VARIOR.ARG_PRINTERS_PAGES_REPORT_LONG,
                            help=MESSAGE.ARG_PRINTERS_PAGES_REPORT, nargs='*', metavar=('{short, long} start_date end_date'), action='append' )

        # parser.add_argument(VARIOR.ARG_PRINTERS_PAGES_REPORT_SHORT, VARIOR.ARG_PRINTERS_PAGES_REPORT_LONG,
        #                     help=MESSAGE.ARG_PRINTERS_PAGES_REPORT, nargs=2, metavar=('start_date','end_date'), action='append' )
        parser.add_argument(VARIOR.ARG_PRINTERS_PAGES_TEST_SHORT, VARIOR.ARG_PRINTERS_PAGES_TEST_LONG,
                            help=MESSAGE.ARG_PRINTERS_PAGES_TEST, nargs='?', metavar=('date_test'), const='now',action="append")
        parser.add_argument(VARIOR.ARG_SEND_EMAIL_SHORT, VARIOR.ARG_SEND_EMAIL_LONG,
                            help=MESSAGE.ARG_SENND_EMAIL, nargs='?', metavar=('date_se'), const='now',action="append")

        app_args = parser.parse_args()

        if app_args.version     : arg_list.append({"arg_name": f"{VARIOR.ARG_VERSION_LONG}"})
        if app_args.saveprncntrs: arg_list.append({"arg_name": f"{VARIOR.ARG_PRINTERS_PAGES_COUNTER_LONG}","option_spc":app_args.saveprncntrs[0]})
        if app_args.repprncntrs : arg_list.append({"arg_name": f"{VARIOR.ARG_PRINTERS_PAGES_REPORT_LONG}","options_rpc":app_args.repprncntrs[0]})
        if app_args.testprncntrs: arg_list.append({"arg_name": f"{VARIOR.ARG_PRINTERS_PAGES_TEST_LONG}","date_tpc":app_args.testprncntrs[0]})
        if app_args.sendemail   : arg_list.append({"arg_name": f"{VARIOR.ARG_SEND_EMAIL_LONG}", "date_se": app_args.sendemail[0]})

        return  arg_list
    def __execute_app(self,arg_list):
        the_arg_list = []
        for item in arg_list:
          the_arg_list.append(item["arg_name"])
        if VARIOR.ARG_VERSION_LONG in the_arg_list:  print(MESSAGE.APP_VERSION)
        if VARIOR.ARG_PRINTERS_PAGES_COUNTER_LONG in the_arg_list: self.__run_get_counters(self,arg_list)
        if VARIOR.ARG_PRINTERS_PAGES_REPORT_LONG  in the_arg_list: self.__run_report(self,arg_list)
        if VARIOR.ARG_PRINTERS_PAGES_TEST_LONG    in the_arg_list: self.__run_test(self,arg_list)
        # Этот пункт всегда должен быть внизу
        if VARIOR.ARG_SEND_EMAIL_LONG             in the_arg_list: self.__run_send_email(self, arg_list)
    def __run_get_counters(self,arg_list):
        option_is_good = False
        the_option = {}
        if 'option_spc' in arg_list[0]:
            if arg_list[0]['option_spc'] == None:
                option_is_good = True
            elif 'id=' in arg_list[0]['option_spc']:
                option = arg_list[0]['option_spc'][3:]
                if str(option).isdigit():
                    option_is_good = True
                    the_option={'id':f'{option}'}
                else: print(ERROR.ARG_PARCE_SPC_ID_ERROR)
            elif 'ip=' in arg_list[0]['option_spc']:
                option = arg_list[0]['option_spc'][3:]
                list_octets = re.findall(r"([0-9]{,3}\.[0-9]{,3}\.[0-9]{,3}\.[0-9]{,3})", option)
                if list_octets:
                    option_is_good = True
                    the_option = {'ip_address': f"'{option}'"}
                else: print(ERROR.ARG_PARCE_SPC_IP_ERROR)
            else: print(ERROR.ARG_PARCE_SPC_ERROR)
            if option_is_good:
                priners = Printers
                priners.get_counters(self,the_option)
    def __run_report(self,arg_list):
        rep_names = VARIOR.REP_NAMES
        parce_options = True
        start_date = f'{str(datetime.date.today())}'
        end_date  = f'{str(datetime.date.today()+datetime.timedelta(days=1))}'

        options = {'type':f'{VARIOR.REP_NAMES[0]}','start_date':f'{start_date}','end_date':f'{end_date}'}
        report_str = 'Нет данных'
        for item in arg_list:
            if 'options_rpc' in item:
                if len(item['options_rpc']) > 3:
                    print('Количество аргументов не должно быть больше 3')
                else:
                    for opt_item in item['options_rpc']:
                        match item['options_rpc'].index(opt_item):
                            case 0:
                                if opt_item in rep_names:
                                    options['type'] = opt_item
                                else:
                                    parce_options = False
                                    print(f'Певый аргумент должен быть {rep_names}')
                            case 1:
                                if over.dk_is_date(opt_item):
                                    date_end = str((datetime.datetime.strptime(opt_item,'%Y-%m-%d')+datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
                                    options['start_date'] = f'{opt_item}'
                                    options['end_date'] = f'{date_end}'
                                else:
                                    parce_options = False
                            case 2:
                                if over.dk_is_date(opt_item):options['end_date'] = f'{opt_item}'
                                else:
                                    parce_options = False
                    if parce_options:
                        report = Report
                        dates = (options['start_date'],options['end_date'])
                        match options['type']:
                            case 'short':
                                report_str = report.get_printers_counts_report_short(self, dates)
                            case 'long':
                                report_str = report.get_printers_counts_report_long(self, dates)
        print(report_str)
        # print(options)
    def __run_test(self,arg_list):
        log_level = VARIOR.LOG_LEVEL_ERROR
        log_message = 'Не удалось запустить тест : ошибка App.__run_test(self,arg_list)'
        for item in arg_list:
            if 'date_tpc' in item and over.dk_is_date(item['date_tpc']):
                test = Test
                log_result = test.test_table_printer_counters(self, item['date_tpc'])
                log_message = ''
                if log_result == None:
                    log_message = f'{MESSAGE.INFO_PRINTERS_COUNTERS_LIST_IS_EMPTY} за {item["date_tpc"]}'
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
    def __run_send_email(self,arg_list):
        for item in arg_list:
            if 'date_se' in item and over.dk_is_date(item['date_se']):
                email = Email()
                email.send_by_date(item['date_se'])




