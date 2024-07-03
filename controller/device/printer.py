from selenium import webdriver    as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from lxml import etree
import dictionary.dic_message     as MESSAGE
import dictionary.dic_error       as ERROR
import time
import controller.database.table_printer_counters as T_PRINTER_COUNTERS
import dictionary.dic_varior as VARIOR

class Printers:
    def get_counters(self):
        printers_list = Printers.__get_priners_list_test(self)
        if printers_list:
            for printer_info in printers_list:
                try:
                    printer = Printer
                    printer_counters = printer.get_counters(self,printer_info)
                    # Printers.__save_printer_counters(self,printer_counters)
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
        printers_list.append({'ip_address': '172.16.1.226', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'1','printer_model':'KYOCERA_ECOSYS_M2735dn','printer_location':'Geely Продавцы'})
        printers_list.append({'ip_address': '172.16.0.232', 'type': '1','login':'Admin','password':'Admin',
                               'id_printer':'2','printer_model':'KYOCERA_ECOSYS_P2040dn','printer_location':'Не знаю'})
        printers_list.append({'ip_address': '172.16.0.223', 'type': '1','login':'Admin','password':'Admin',
                               'id_printer':'3','printer_model':'KYOCERA_ECOSYS_M3040dn','printer_location':'Не знаю'})
        printers_list.append({'ip_address': '172.16.1.228', 'type': '1','login':'Admin','password':'Admin',
                               'id_printer':'4','printer_model':'KYOCERA_ECOSYS_M2035dn','printer_location':'Старшие кредитницы'})
        printers_list.append({'ip_address': '172.16.1.248', 'type': '1','login':'Admin','password':'Admin',
                               'id_printer':'5','printer_model':'KYOCERA_ECOSYS_M2040dn','printer_location':'Бухгалтерия зарплата'})
        return printers_list

class Printer:
    def get_counters(self,printer_info):
        #printer_counters = []
        ret = {}
        printer_model = printer_info['printer_model']
        if printer_model == 'KYOCERA_ECOSYS_M2735dn':
            Printer.__get_counters_KYOCERA_ECOSYS_M2735dn(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_P2040dn':
            Printer.__get_counters_KYOCERA_ECOSYS_P2040dn(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_M3040dn':
            Printer.__get_counters_KYOCERA_ECOSYS_M3040dn(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_M2035dn':
            Printer.__get_counters_KYOCERA_ECOSYS_M2035dn(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_M2040dn':
            Printer.__get_counters_KYOCERA_ECOSYS_M2040dn(self,printer_info)

    def __init_driver(self, ip_address):
        driver = None
        url = f'http://{ip_address}'
        driver = wd.Chrome()
        driver.implicitly_wait(VARIOR.DRIVER_WAIT)
        driver.get(url)
        return driver
    def __exit_from_standby_mode(self,driver):
        # Иногда принтер находится в режиме энергосбережения, в этом случае проверяем, и выводим его из этого режима
        driver.implicitly_wait(5)
        frame = driver.find_element(By.NAME, 'main')
        driver.switch_to.frame(frame)
        driver.find_element(By.NAME,'submit001').click()
        driver.implicitly_wait(VARIOR.DRIVER_WAIT)
    def __init_printer_type_1(self,printer_info):
        driver = Printer.__init_driver(self,printer_info['ip_address'])
        try:
            Printer.__exit_from_standby_mode(self,driver)
        except:pass
        frame = driver.find_element(By.NAME, 'wlmframe')
        driver.switch_to.frame(frame)
        return driver
    def __get_counters_KYOCERA_ECOSYS_M2735dn(self,printer_info):
        driver = Printer.__init_printer_type_1(self,printer_info)
        driver.find_element(By.XPATH,'//*[@id="tm2"]/div[1]/span').click()
        driver.find_element(By.XPATH, '//*[@id="s81"]').click()

        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')

        pr_couners = {'print_copy' :f'{content_table_td[15].text}',
                      'print_print':f'{content_table_td[22].text}',
                      'print_fax'  :f'{content_table_td[28].text}',
                      'print_sum'  :f'{content_table_td[35].text}'}
        driver.switch_to.parent_frame()

        frame = driver.find_element(By.XPATH,'//iframe[@id="deviceabout"]')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')
        sc_counters = {'scan_copy':f'{content_table_td[8].text}',
                       'scan_fax' :f'{content_table_td[14].text}',
                       'scan_over':f'{content_table_td[20].text}',
                       'scan_sum' :f'{content_table_td[26].text}'}
        driver.switch_to.parent_frame()

        printer_counters = {'id_device': f'{printer_info["id_printer"]}'}
        printer_counters.update(pr_couners)
        printer_counters.update(sc_counters)

        t_printer_counters = T_PRINTER_COUNTERS.table_printer_counters
        t_printer_counters.save_to_table_by_dict(self, printer_counters)
    def __get_counters_KYOCERA_ECOSYS_P2040dn(self,printer_info):

        driver = Printer.__init_printer_type_1(self,printer_info)
        driver.find_element(By.XPATH,'//*[@id="tm2"]/div[1]/span').click()
        driver.find_element(By.XPATH, '//*[@id="s81"]').click()
        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id = 'contentrow')
        content_table_td = soup.find_all('td')

        pr_counters = {'print_sum':f'{content_table_td[15].text}'}
        printer_counters = {'id_device': f'{printer_info["id_printer"]}'}
        printer_counters.update(pr_counters)

        t_printer_counters = T_PRINTER_COUNTERS.table_printer_counters
        t_printer_counters.save_to_table_by_dict(self, printer_counters)
    def __get_counters_KYOCERA_ECOSYS_M3040dn(self,printer_info):
        driver = Printer.__init_printer_type_1(self, printer_info)
        driver.find_element(By.XPATH,'// *[ @ id = "devicestatuscolor"] / td[3] / a / div').click()
        driver.find_element(By.XPATH, "//div[@id='s81']//td[2]//span").click()

        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')

        pr_couners = {'print_copy' :f'{content_table_td[22].text}',
                      'print_print':f'{content_table_td[29].text}',
                      'print_sum'  :f'{content_table_td[36].text}'}
        driver.switch_to.parent_frame()

        frame = driver.find_element(By.XPATH,'//iframe[@id="deviceabout"]')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')
        sc_counters = {'scan_copy':f'{content_table_td[10].text}',
                       'scan_over':f'{content_table_td[16].text}',
                       'scan_sum' :f'{content_table_td[22].text}'}
        driver.switch_to.parent_frame()
        printer_counters = {'id_device': f'{printer_info["id_printer"]}'}
        printer_counters.update(pr_couners)
        printer_counters.update(sc_counters)

        t_printer_counters = T_PRINTER_COUNTERS.table_printer_counters
        t_printer_counters.save_to_table_by_dict(self, printer_counters)
    def __get_counters_KYOCERA_ECOSYS_M2035dn(self,printer_info):
        Printer.__get_counters_KYOCERA_ECOSYS_M3040dn(self,printer_info)
    def __get_counters_KYOCERA_ECOSYS_M2040dn(self,printer_info):
        driver = Printer.__init_printer_type_1(self, printer_info)
        driver.find_element(By.XPATH,'//*[@id="tm2"]/div[1]/span/span').click()
        frame = driver.find_element(By.ID, 'toner')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        dom = etree.HTML(str(soup))
        cartridge_filling = dom.xpath('//*[@id="contentrow"]/tbody/tr[3]/td[3]/text()')[0]
        cartridge_filling = cartridge_filling[:-1]
        driver.switch_to.parent_frame()
        driver.find_element(By.XPATH, '//*[@id="s81"]').click()

        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id = 'contentrow')
        content_table_td = soup.find_all('td')
        pr_couners = {'print_copy' :f'{content_table_td[15].text}',
                      'print_print':f'{content_table_td[22].text}',
                      'print_sum'  :f'{content_table_td[28].text}'}
        driver.switch_to.parent_frame()

        frame = driver.find_element(By.NAME, 'deviceabout')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')
        sc_counters = {'scan_copy':f'{content_table_td[8].text}',
                       'scan_over':f'{content_table_td[14].text}',
                       'scan_sum' :f'{content_table_td[20].text}'}
        driver.switch_to.parent_frame()

        printer_counters = {'id_device': f'{printer_info["id_printer"]}'}
        printer_counters.update(pr_couners)
        printer_counters.update(sc_counters)
        printer_counters.update({'сartridge_filling':f'{cartridge_filling}'})

        t_printer_counters = T_PRINTER_COUNTERS.table_printer_counters
        t_printer_counters.save_to_table_by_dict(self,printer_counters)



