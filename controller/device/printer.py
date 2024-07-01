from selenium import webdriver    as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import dictionary.dic_message     as MESSAGE
import dictionary.dic_error       as ERROR
import time
import controller.database.table_printer_counters as T_PRINTER_COUNTERS

class Printers:
    def get_counters(self):
        printers_list = Printers.__get_priners_list_test(self)
        if printers_list:
            for printer_info in printers_list:
                try:
                    printer = Printer
                    printer_counters = printer.get_counters(self,printer_info)
                    Printers.__save_printer_counters(self,printer_counters)
                except Exception as _ex:
                    print(f"{ERROR.CANT_CREATE_PRINTER} {_ex}")
        else:
            print(f"{MESSAGE.INFO_PRINTERS_LIST_IS_EMPTY} (Printers.get_counters)")
    def __save_printer_counters(self,printer_counters):
        # print(printer_counters)
        t_printer_counters = T_PRINTER_COUNTERS.table_printer_counters
        fields = 'id_device, print_copy, ' \
                 'print_print, print_fax, ' \
                 'print_sum, scan_copy, ' \
                 'scan_fax, scan_over, ' \
                 'scan_sum, сartridge_filling'
        data = f'{printer_counters["id_printer"]} ,{printer_counters["print_copy"]},' \
               f'{printer_counters["print_print"]},{printer_counters["print_fax"]},' \
               f'{printer_counters["print_sum"]}  ,{printer_counters["scan_copy"]},' \
               f'{printer_counters["scan_fax"]}   ,{printer_counters["scan_over"]},' \
               f'{printer_counters["scan_sum"]}   ,{printer_counters["cartridge_filling"]}'
        t_printer_counters.save_to_table(self, fields, data)
    def __get_priners_list_test(self):
        printers_list = []
        printers_list.append({'ip_address': '172.16.1.226', 'type': '1','login':'Admin','password':'Admin','id_printer':'1'})
        # printers_list.append({'ip_address': '172.16.0.232', 'type': '1','login':'Admin','password':'Admin','id_printer':'2'})
        # printers_list.append({'ip_address': '172.16.0.223', 'type': '1','login':'Admin','password':'Admin','id_printer':'3'})
        return printers_list

class Printer:
    def get_counters(self,printer_info):
        printer_counters = []
        def login(driver):
            frame = driver.find_element(By.NAME, 'wlmframe')
            driver.switch_to.frame(frame)
            driver.find_element(By.ID, 'arg01_UserName').send_keys(printer_info["login"])
            driver.find_element(By.ID, 'arg02_Password').send_keys(printer_info["password"])
            driver.find_element(By.NAME, 'Login').click()
        def exit_from_standby_mode(driver):
            frame = driver.find_element(By.NAME, 'main')
            driver.switch_to.frame(frame)
            driver.find_element(By.NAME,'submit001').click()
        def get_printer_counters(driver):
            ret = None
            frame = driver.find_element(By.NAME, 'deviceconfig')
            driver.switch_to.frame(frame)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            content_table = soup.find(id='contentrow')
            content_table_td = soup.find_all('td')

            ret = {'print_copy' :f'{content_table_td[15].text}',
                        'print_print':f'{content_table_td[22].text}',
                        'print_fax'  :f'{content_table_td[28].text}',
                        'print_sum'  :f'{content_table_td[35].text}'}
            driver.switch_to.parent_frame()
            return ret
        def get_scaner_counters(driver):
            ret = None
            frame = driver.find_element(By.XPATH,'//iframe[@id="deviceabout"]')
            driver.switch_to.frame(frame)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            content_table = soup.find(id='contentrow')
            content_table_td = soup.find_all('td')
            ret = {'scan_copy':f'{content_table_td[8].text}',
                   'scan_fax' :f'{content_table_td[14].text}',
                   'scan_over':f'{content_table_td[20].text}',
                   'scan_sum' :f'{content_table_td[26].text}'}
            driver.switch_to.parent_frame()
            return ret

        url = f'http://{printer_info["ip_address"]}'
        driver = wd.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)
        ##Иногда принтер находится в режиме энергосбережения, в этом случае проверяем этот факт, и выводим его из этого режима
        try: exit_from_standby_mode(driver)
        except: pass

        login(driver)
        driver.find_element(By.ID, 's81').click()
        ret = {'id_printer': f'{printer_info["id_printer"]}'}
        pr_cnt = get_printer_counters(driver)
        cp_cnt = get_scaner_counters (driver)
        # print(cp_cnt)
        ret.update(pr_cnt)
        ret.update(cp_cnt)
        ret.update({'cartridge_filling':'0'})
        return ret




