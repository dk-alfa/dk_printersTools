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
        # printers_list.append({'ip_address': '172.16.0.232', 'type': '1','login':'Admin','password':'Admin'})
        # printers_list.append({'ip_address': '172.16.0.223',   'type': '1','login':'Admin','password':'Admin'})
        return printers_list

class Printer:
    def get_counters(self,printer_info):
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

        url = f'http://{printer_info["ip_address"]}'
        driver = wd.Chrome()
        driver.implicitly_wait(10)
        driver.get(url)

        ##Иногда принтер находится в режиме энергосбережения, в этом случае проверяем этот факт, и выводим его из этого режима
        try: exit_from_standby_mode(driver)
        except: pass

        login(driver)

        driver.find_element(By.ID, 's81').click()
        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')

        print('---------------')
        print(f'Копирование: {content_table_td[15].text}')
        print('---------------')
        print(f'Принтер: {content_table_td[22].text}')
        print('---------------')
        print(f'Факс: {content_table_td[28].text}')
        print('---------------')
        print(f'Общий: {content_table_td[35].text}')
        print('================')


