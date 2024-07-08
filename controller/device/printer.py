from selenium import webdriver    as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from lxml import etree
import dictionary.dic_message     as MESSAGE
import dictionary.dic_error       as ERROR
import time
import controller.database.table_printer_counters as T_PRINTER_COUNTERS
import dictionary.dic_varior as VARIOR
import re

class Printers:
    def get_counters(self):
        printers_list = Printers.__get_priners_list_test(self)
        if printers_list:
            for printer_info in printers_list:
                try:
                    printer = Printer
                    printer_counters = printer.get_counters(self,printer_info)
                except Exception as _ex:
                    print(f"{ERROR.CANT_CREATE_PRINTER} {_ex}")
        else:
            print(f"{MESSAGE.INFO_PRINTERS_LIST_IS_EMPTY} (Printers.get_counters)")
    def __get_priners_list_test(self):
        printers_list = []
        printers_list.append({'ip_address': '172.16.1.226', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'1','printer_model':'KYOCERA_ECOSYS_M2735dn','printer_location':'Geely Продавцы справа'})
        printers_list.append({'ip_address': '172.16.0.232', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'2','printer_model':'KYOCERA_ECOSYS_P2040dn','printer_location':'Exeed возле выдачи'})
        printers_list.append({'ip_address': '172.16.0.223', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'3','printer_model':'KYOCERA_ECOSYS_M3040dn','printer_location':'Exeed продавцы возле входа'})
        printers_list.append({'ip_address': '172.16.1.228', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'4','printer_model':'KYOCERA_ECOSYS_M2035dn','printer_location':'Старшие кредитницы'})
        printers_list.append({'ip_address': '172.16.1.248', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'5','printer_model':'KYOCERA_ECOSYS_M2040dn','printer_location':'Бухгалтерия зарплата'})
        printers_list.append({'ip_address': '172.16.1.217', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'6','printer_model':'KYOCERA_ECOSYS_M2135dn','printer_location':'Exeed кредитницы'})
        printers_list.append({'ip_address': '172.16.1.235', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'7','printer_model':'KYOCERA_ECOSYS_M2735dn','printer_location':'ОК Света'})
        printers_list.append({'ip_address': '172.16.1.213', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'8','printer_model':'KYOCERA_ECOSYS_M2135dn','printer_location':'Кредитницы возле Светы'})
        printers_list.append({'ip_address': '172.16.1.215', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'9','printer_model':'KYOCERA_ECOSYS_M2040dn','printer_location':'Феликс'})
        printers_list.append({'ip_address': '172.16.1.220', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'10','printer_model':'KYOCERA_FS_1035MFP'   ,'printer_location':'Стариков'})
        printers_list.append({'ip_address': '172.16.1.250', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'11','printer_model':'KYOCERA_ECOSYS_M2035dn','printer_location':'Журавлева'})
        printers_list.append({'ip_address': '172.16.1.229', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'12','printer_model':'HP_COLOR_LJ_M254nw'    ,'printer_location':'Jeely продавцы слева'})
        printers_list.append({'ip_address': '172.16.1.249', 'type': '1','login':'Admin','password':'Admin',
                               'id_printer':'13','printer_model':'KYOCERA_ECOSYS_M2635dn','printer_location':'Toyota кредитницы'})
        printers_list.append({'ip_address': '172.16.1.234', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'14','printer_model':'KYOCERA_FS_2100DN'    ,'printer_location':'Jeely допники'})
        printers_list.append({'ip_address': '172.16.1.238', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'15','printer_model':'KYOCERA_ECOSYS_M3145dn'    ,'printer_location':'Toyota Ахметдинов'})
        printers_list.append({'ip_address': '172.16.1.240', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'16','printer_model':'KYOCERA_ECOSYS_M3145dn'    ,'printer_location':'Toyota Сервис сзади'})
        printers_list.append({'ip_address': '172.16.1.237', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'17','printer_model':'KYOCERA_ECOSYS_M3145dn'    ,'printer_location':'Toyota Подержанные сзади'})
        printers_list.append({'ip_address': '172.16.1.244', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'18','printer_model':'KYOCERA_ECOSYS_P2040dn','printer_location':'Toyota подержанные РОП'})
        printers_list.append({'ip_address': '172.16.1.236', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'19','printer_model':'KYOCERA_ECOSYS_P3150dn','printer_location':'Toyota подержанные возле ОПРК'})
        printers_list.append({'ip_address': '172.16.1.224', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'20','printer_model':'KYOCERA_ECOSYS_FS_1370dn','printer_location':'Toyota сервис левый'})
        printers_list.append({'ip_address': '172.16.1.239', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'21','printer_model':'KYOCERA_ECOSYS_M2135dn','printer_location':'Toyota сервис правый'})
        printers_list.append({'ip_address': '172.16.1.227', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'22','printer_model':'KYOCERA_ECOSYS_M2735dn','printer_location':'Toyota Алина'})
        printers_list.append({'ip_address': '172.16.1.242', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'23','printer_model':'KYOCERA_FS_1035MFP'   ,'printer_location':'Toyota Callcenter'})
        printers_list.append({'ip_address': '172.16.1.214', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'24','printer_model':'KYOCERA_ECOSYS_M2735dn','printer_location':'Toyota Бухгалтерия ЕА'})
        printers_list.append({'ip_address': '172.16.1.219', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'25','printer_model':'KYOCERA_ECOSYS_M2040dn','printer_location':'Toyota Бухгалтерия Рузана'})
        printers_list.append({'ip_address': '172.16.0.161', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'26','printer_model':'KYOCERA_ECOSYS_M2135dn','printer_location':'Toyota Бухгалтерия Аня'})
        printers_list.append({'ip_address': '172.16.1.233', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'27','printer_model':'KYOCERA_ECOSYS_M3040dn','printer_location':'Toyota Логисты'})
        printers_list.append({'ip_address': '172.16.1.231', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'28','printer_model':'KYOCERA_ECOSYS_P2040dn','printer_location':'Toyota Склад'})
        printers_list.append({'ip_address': '172.16.1.232', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'29','printer_model':'KYOCERA_FS_1035MFP'   ,'printer_location':'Toyota IT отдел'})
        printers_list.append({'ip_address': '172.16.1.241', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'30','printer_model':'KYOCERA_ECOSYS_FS_1370dn','printer_location':'Toyota IT отдел 1с'})
        printers_list.append({'ip_address': '172.16.1.216', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'31','printer_model':'KYOCERA_ECOSYS_P2135dn','printer_location':'Toyota Ремзона мастер'})
        printers_list.append({'ip_address': '172.16.1.243', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'32','printer_model':'KYOCERA_ECOSYS_P5021dn','printer_location':'Toyota Цветной у Кирилла'})
        printers_list.append({'ip_address': '172.16.1.221', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'33','printer_model':'KYOCERA_ECOSYS_M3145dn'    ,'printer_location':'Tank сервис'})
        printers_list.append({'ip_address': '172.16.1.247', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'34','printer_model':'KYOCERA_ECOSYS_M3040dn','printer_location':'Tank ресепшн'})
        printers_list.append({'ip_address': '172.16.1.218', 'type': '1','login':'Admin','password':'Admin',
                              'id_printer':'35','printer_model':'KYOCERA_ECOSYS_M2735dn','printer_location':'Tank кредит'})

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
        if printer_model == 'KYOCERA_ECOSYS_M2135dn':
            Printer.__get_counters_KYOCERA_ECOSYS_M2040dn(self,printer_info)
        if printer_model == 'KYOCERA_FS_1035MFP':
            Printer.__get_counters_KYOCERA_FS_1035MFP(self,printer_info)
        if printer_model == 'KYOCERA_FS_2100DN':
            Printer.__get_counters_KYOCERA_FS_2100DN(self,printer_info)
        if printer_model == 'HP_COLOR_LJ_M254nw':
            Printer.__get_counters_HP_COLOR_LJ_M254nw(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_M2635dn':
            Printer.__get_counters_KYOCERA_ECOSYS_M2735dn(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_M3145dn':
            Printer.__get_counters_KYOCERA_ECOSYS_M3145dn(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_P3150dn':
            Printer.__get_counters_KYOCERA_ECOSYS_P3150dn(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_FS_1370dn':
            Printer.__get_counters_KYOCERA_FS_1370dn(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_P2135dn':
            Printer.__get_counters_KYOCERA_ECOSYS_P2135dn(self,printer_info)
        if printer_model == 'KYOCERA_ECOSYS_P5021dn':
            Printer.__get_counters_KYOCERA_ECOSYS_P5021dn(self,printer_info)
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
    def __init_printer_type_2(self,printer_info):
        driver = Printer.__init_driver(self,printer_info['ip_address'])
        frame = driver.find_element(By.NAME,'main')
        driver.switch_to.frame(frame)
        return driver
    def __init_printer_type_3(self,printer_info):
        driver = Printer.__init_driver(self,printer_info['ip_address'])
        return driver
    def __login_to_printer(self,driver,printer_info):
        driver.find_element(By.XPATH, '//*[@id="arg01_UserName"]').send_keys(printer_info['login'])
        driver.find_element(By.XPATH, '//*[@id="arg02_Password"]').send_keys(printer_info['password'])
        driver.find_element(By.XPATH, '//*[@id="s10"]/table/tbody/tr[2]/td[3]/table/tbody/tr[5]/td/input').click()
    def __get_content(self,driver):
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            dom = etree.HTML(str(soup))
            content = dom.xpath('//*[@id="content"]/table/tbody/tr/td/script[1]/text()')
            content_string = content[0]
            return content_string
    def __get_count(self,content_str, selector):
        # значение счетчика содержится в  sData[x], sData[x] встречается несколько раз
        ret = None
        matches = re.finditer(selector, content_str)
        indices = [match.start() for match in matches]
        for start_position in indices:
            end_position = content_str.find(';', start_position)
            tmp_str = content_str[start_position:end_position]
            mtch = re.finditer('"', tmp_str)
            ind = [match.start() for match in mtch]
            find_str = tmp_str[ind[0] + 1:ind[1]]
            if find_str: ret = find_str  # print(f'[{find_str}]')
        return ret
    def __save_to_table(self,printer_info,pr_counters):
        printer_counters = {'id_device': f'{printer_info["id_printer"]}'}
        printer_counters.update(pr_counters)

        t_printer_counters = T_PRINTER_COUNTERS.table_printer_counters
        t_printer_counters.save_to_table_by_dict(self, printer_counters)
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

        pr_counters = {'print_print':f'{content_table_td[15].text}',
                       'print_sum'  :f'{content_table_td[15].text}'}
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
        try:
            driver.find_element(By.XPATH,'//*[@id="tm2"]/div[1]/span/span').click()
        except:
            driver.find_element(By.XPATH, '//*[@id="tm2"]/div[1]/span').click()

        frame = driver.find_element(By.ID, 'toner')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        dom = etree.HTML(str(soup))
        cartridge_filling = dom.xpath('//*[@id="contentrow"]/tbody/tr[3]/td[3]/text()')[0]
        cartridge_filling = cartridge_filling[:-1]
        if not cartridge_filling : cartridge_filling = '0'
        driver.switch_to.parent_frame()
        driver.find_element(By.XPATH, '//*[@id="s81"]').click()

        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id = 'contentrow')
        content_table_td = soup.find_all('td')
        pr_counters = {'print_copy' :f'{content_table_td[15].text}',
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
        printer_counters.update(pr_counters)
        printer_counters.update(sc_counters)
        printer_counters.update({'сartridge_filling':f'{cartridge_filling}'})

        t_printer_counters = T_PRINTER_COUNTERS.table_printer_counters
        t_printer_counters.save_to_table_by_dict(self,printer_counters)
    def __get_counters_KYOCERA_FS_1035MFP(self,printer_info):
        driver = Printer.__init_printer_type_2(self, printer_info)
        driver.find_element(By.XPATH,'//*[@id="parentcounters"]').click()
        driver.find_element(By.XPATH,'//*[@id="counters"]/div[1]/a').click()

        content_string = Printer.__get_content(self,driver)

        print_copy  = Printer.__get_count(self,content_string, 'sData\\[0\\]')
        print_print = Printer.__get_count(self,content_string, 'sData\\[1\\]')
        print_sum   = Printer.__get_count(self,content_string, 'sData\\[3\\]')

        pr_counters = {'print_copy' :f'{print_copy}',
                      'print_print':f'{print_print}',
                      'print_sum'  :f'{print_sum}'}

        driver.find_element(By.XPATH, '//*[@id="contex"]/a').click()
        content_string = Printer.__get_content(self, driver)

        scan_copy  = Printer.__get_count(self,content_string, 'sData\\[0\\]')
        scan_over  = Printer.__get_count(self,content_string, 'sData\\[1\\]')
        scan_sum   = Printer.__get_count(self,content_string, 'sData\\[3\\]')

        sc_counters = {'scan_copy' :f'{scan_copy}',
                      'scan_over':f'{scan_over}',
                      'scan_sum'  :f'{scan_sum}'}

        pr_counters.update(sc_counters)

        Printer.__save_to_table(self, printer_info, pr_counters)

        # printer_counters.update(pr_counters)
        # printer_counters.update(sc_counters)
        #
        # printer_counters = {'id_device': f'{printer_info["id_printer"]}'}
        #
        #
        # t_printer_counters = T_PRINTER_COUNTERS.table_printer_counters
        # t_printer_counters.save_to_table_by_dict(self,printer_counters)
    def __get_counters_KYOCERA_FS_2100DN(self,printer_info):
        driver = Printer.__init_printer_type_1(self, printer_info)
        Printer.__login_to_printer(self,driver,printer_info)
        driver.find_element(By.XPATH,'//*[@id="settingcolor"]/td[3]/a').click()
        driver.switch_to.default_content()
        frame = driver.find_element(By.NAME, 'main')
        driver.switch_to.frame(frame)
        driver.find_element(By.XPATH, '//*[@id="parentcounters"]').click()
        content_string = Printer.__get_content(self,driver)
        print_print = Printer.__get_count(self,content_string,'sData\\[0\\]')

        pr_counters = {'print_print':f'{print_print}',
                       'print_sum'  :f'{print_print}'}

        Printer.__save_to_table(self, printer_info, pr_counters)
    def __get_counters_HP_COLOR_LJ_M254nw(self,printer_info):
        driver = Printer.__init_printer_type_3(self, printer_info)
        driver.find_element(By.XPATH, '//*[@id="navigationControl"]/div[3]/a').click()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        dom = etree.HTML(str(soup))
        content = dom.xpath('/html/body/div[2]/table/tbody/tr[2]/td[2]/div[7]/table/tbody/tr[1]/td[2]/text()')
        print_print = content[0]

        pr_counters = {'print_print':f'{print_print}',
                       'print_sum'  :f'{print_print}'}

        Printer.__save_to_table(self,printer_info,pr_counters)
    def __get_counters_KYOCERA_ECOSYS_M3145dn(self, printer_info):
        driver = Printer.__init_printer_type_1(self, printer_info)
        driver.find_element(By.XPATH, '//*[@id="tm2"]/div[1]/span').click()
        driver.find_element(By.XPATH, '//*[@id="s81"]').click()

        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')

        pr_counters = {'print_copy' :f'{content_table_td[15].text}',
                      'print_print':f'{content_table_td[22].text}',
                      'print_sum'  :f'{content_table_td[28].text}'}
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

        frame = driver.find_element(By.ID, 'toner')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        dom = etree.HTML(str(soup))
        cartridge_filling = dom.xpath('//*[@id="contentrow"]/tbody/tr[3]/td[3]/text()')[0]
        cartridge_filling = cartridge_filling[:-1]
        if not cartridge_filling : cartridge_filling = '0'
        driver.switch_to.parent_frame()

        pr_counters.update(sc_counters)
        pr_counters.update({'сartridge_filling': f'{cartridge_filling}'})

        Printer.__save_to_table(self, printer_info, pr_counters)
    def __get_counters_KYOCERA_ECOSYS_P3150dn(self, printer_info):
        driver = Printer.__init_printer_type_1(self, printer_info)
        driver.find_element(By.XPATH, '//*[@id="tm2"]/div[1]/span/span').click()
        driver.find_element(By.XPATH, '//*[@id="s81"]').click()

        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')

        pr_counters = {'print_print':f'{content_table_td[15].text}',
                       'print_sum'  :f'{content_table_td[15].text}'}

        Printer.__save_to_table(self, printer_info, pr_counters)
    def __get_counters_KYOCERA_FS_1370dn(self,printer_info):
        driver = Printer.__init_printer_type_2(self, printer_info)
        driver.find_element(By.XPATH, '//*[@id="leftcolmn"]/div/div[11]/a').click()

        content_string = Printer.__get_content(self, driver)
        print_print = Printer.__get_count(self, content_string, 'sName\\[0\\]')

        pr_counters = {'print_print' :f'{print_print}',
                      'print_sum'    :f'{print_print}'}

        Printer.__save_to_table(self, printer_info, pr_counters)
    def __get_counters_KYOCERA_ECOSYS_P2135dn(self,printer_info):
        driver = Printer.__init_printer_type_1(self, printer_info)
        driver.find_element(By.XPATH, '//*[@id="devicestatuscolor"]/td[3]/a/div').click()
        driver.find_element(By.XPATH, '//*[@id="counterdevice"]/div/div[2]/u/a/span').click()

        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')

        pr_counters = {'print_print':f'{content_table_td[23].text}',
                      'print_sum'  :f'{content_table_td[23].text}'}

        Printer.__save_to_table(self, printer_info, pr_counters)
    def __get_counters_KYOCERA_ECOSYS_P5021dn(self, printer_info):
        driver = Printer.__init_printer_type_1(self, printer_info)
        driver.find_element(By.XPATH, '//*[@id="tm2"]/div[1]/span').click()
        driver.find_element(By.XPATH, '//*[@id="s81"]').click()

        frame = driver.find_element(By.NAME, 'toner')
        driver.switch_to.frame(frame)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='tonertab')
        content_table_td = soup.find_all('td')
        сartridge_filling = content_table_td[12].text[:-1]
        driver.switch_to.parent_frame()

        frame = driver.find_element(By.NAME, 'deviceconfig')
        driver.switch_to.frame(frame)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_table = soup.find(id='contentrow')
        content_table_td = soup.find_all('td')

        pr_counters = {'print_print':f'{content_table_td[14].text}',
                       'print_fax'  : f'{content_table_td[15].text}',
                       'print_sum'  :f'{content_table_td[16].text}'}
        pr_counters.update({'сartridge_filling':f'{сartridge_filling}'})
        Printer.__save_to_table(self, printer_info, pr_counters)












