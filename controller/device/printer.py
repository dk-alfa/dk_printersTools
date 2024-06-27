from selenium import webdriver    as wd
from selenium.webdriver.common.by import By
import dictionary.dic_message     as MESSAGE
import dictionary.dic_error       as ERROR
import time
from bs4 import BeautifulSoup

class Printers:
    def get_counters(self):
        printers_list = Printers.__get_priners_list_test(self)
        if printers_list:
            for printer_info in printers_list:
                try:
                    printer = Printer
                    printer.get_counters(self,printer_info)
                except Exception as _ex:
                    print(f"{ERROR.CANT_CREATE_PRINTER} {_ex}")
        else:
            print(f"{MESSAGE.INFO_PRINTERS_LIST_IS_EMPTY} (Printers.get_counters)")
    def __get_priners_list_test(self):
        printers_list = []
        printers_list.append({'ip_address': '172.16.1.226', 'type': '1','login':'Admin','password':'Admin'})
        #printers_list.append({'ip_address': '172.16.0.232', 'type': '1','login':'Admin','password':'Admin'})
        # printers_list.append({'ip_address': '172.16.0.223',   'type': '1','login':'Admin','password':'Admin'})
        return printers_list

class Printer:
    def get_counters(self,printer_info):
        url = f'http://{printer_info["ip_address"]}'
        driver = wd.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)

        ##Иногда принтер находится в режиме экономии энергии, в этом случае проверяем этот факт, и выводим его из этого режима
        # frame = driver.find_element(By.TAG_NAME, 'frame')
        # driver.switch_to.frame(frame)
        # driver.find_element(By.NAME,'submit001').click()
        # time.sleep(5)

        frame =  driver.find_element(By.NAME,'wlmframe')
        driver.switch_to.frame(frame)
        driver.find_element(By.ID, 'arg01_UserName').send_keys(printer_info["login"])
        driver.find_element(By.ID, 'arg02_Password').send_keys(printer_info["password"])
        driver.find_element(By.NAME, 'Login').click()

        time.sleep(10)

        print(f'get_counters{printer_info}')
        print(f'{printer_info["ip_address"]}/')
        print(url)


