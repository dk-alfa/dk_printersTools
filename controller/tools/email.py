from controller.tools.log import Log
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header    import Header
import dictionary.dic_varior as VARIOR

class Email:

    def send_by_date(self,date_in):
        if date_in == 'now':
            date = datetime.datetime.now()
        else:
            date = datetime.datetime.strptime(date_in, "%Y-%m-%d")
        date = date.strftime("%Y-%m-%d")

        log = Log()
        log_for_send = log.read_log_by_date(date)
        send_str = f'За дату {date} нет сообщений'
        if log_for_send :
            send_str = f'Отчет о событиях за {date} \n\n'
            for item in log_for_send:
                send_str += f"\tСообщение от {item['log_subject']} [{item['lavel']}] {item['message'] }\n"
        self.__send_email(send_str)
    def __send_email(self,message):
        msg = MIMEText(message,'plain','utf-8')
        msg['Subject'] = Header(VARIOR.MAIL_SUBJECT,'utf-8')
        msg['From'] = VARIOR.MAIL_LOGIN
        msg['To'] = VARIOR.MAIL_TO

        s = smtplib.SMTP(VARIOR.MAIL_SMTP_HOST, VARIOR.MAIL_PORT, timeout=10)
        try:
            s.starttls()
            s.login(VARIOR.MAIL_LOGIN,VARIOR.MAIL_PASSWORD)
            s.sendmail(msg['From'],msg['To'], msg.as_string())
        finally:
            s.quit()
            print('Сообщение отправлено')
