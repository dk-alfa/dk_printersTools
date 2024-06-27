import argparse
from   controller.device.printer import Printers
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
        parser.add_argument(VARIOR.ARG_PRINTERS_PAGES_COUNTER_SHORT, VARIOR.ARG_PRINTERS_PAGES_COUNTER_LONG, help=MESSAGE.ARG_PRINTERS_PAGES_COUNTER,action="store_true")

        app_args = parser.parse_args()

        if app_args.version: arg_list.append(VARIOR.ARG_VERSION_LONG)
        if app_args.saveprncntrs: arg_list.append(VARIOR.ARG_PRINTERS_PAGES_COUNTER_LONG)

        return  arg_list
    def __execute_app(self,arg_list):
        if VARIOR.ARG_VERSION_LONG in arg_list: print(MESSAGE.APP_VERSION)
        if VARIOR.ARG_PRINTERS_PAGES_COUNTER_LONG in arg_list:
            printers = Printers
            printers.get_counters(self)

