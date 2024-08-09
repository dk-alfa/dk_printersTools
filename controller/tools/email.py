from controller.tools.log import Log
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header    import Header
from email.mime.multipart import MIMEMultipart
import dictionary.dic_varior as VARIOR
import dictionary.dic_message as MESSAGE

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
            send_str = f'<h2 style="color: SteelBlue;margin-bottom:0px"> Отчет о событиях за {date} </h2>' \
                       f'<hr style="color: CadetBlue;">\n'
            for item in log_for_send:
                if ': [' in str(item['message']) :
                    tmp_str = str(item['message']).replace('\n','\n\t')
                    item['message'] = tmp_str
                send_str += f"\t({item['date_created']}) {item['log_subject']} [{item['lavel']}] {item['message'] }\n"
        self.__send_email(send_str)
    def __send_email(self,message):
        # msg = MIMEText(message,'plain','utf-8')
        msg = MIMEMultipart('alternative')
        msg['Subject'] = Header(VARIOR.MAIL_SUBJECT,'utf-8')
        msg['From'] = VARIOR.MAIL_LOGIN
        msg['To'] = VARIOR.MAIL_TO

        message = message.replace('\n','<br>')

        html = f"""\
        <html>
          <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
          </head>
          <body  style = "font-family:Roboto">
               <span style = "font-size: 14"> {message} </span>          
          </body>
        </html>
        """
        # part1 = MIMEText(message, 'plain')
        part2 = MIMEText(html, 'html')
        # msg.attach(part1)
        msg.attach(part2)


        s = smtplib.SMTP(VARIOR.MAIL_SMTP_HOST, VARIOR.MAIL_PORT, timeout=10)
        try:
            s.starttls()
            s.login(VARIOR.MAIL_LOGIN,VARIOR.MAIL_PASSWORD)
            s.sendmail(msg['From'],msg['To'], msg.as_string())
        finally:
            s.quit()
            print(MESSAGE.EMAIL_MESSAGE_IS_SEND)
