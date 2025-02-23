import datetime

ARG_VERSION_LONG = '--version'
ARG_VERSION_SHORT = '-v'
ARG_PRINTERS_PAGES_COUNTER_LONG = '--saveprncntrs'
ARG_PRINTERS_PAGES_COUNTER_SHORT = '-spc'
ARG_PRINTERS_PAGES_REPORT_LONG = '--repprncntrs'
ARG_PRINTERS_PAGES_REPORT_SHORT = '-rpc'
ARG_PRINTERS_PAGES_TEST_LONG = '--testprncntrs'
ARG_PRINTERS_PAGES_TEST_SHORT = '-tpc'
ARG_SEND_EMAIL_LONG = '--sendemail'
ARG_SEND_EMAIL_SHORT = '-se'

DRIVER_WAIT = 30

DB_NAME = 'it-tools_dev'
DB_USER = 'pgroot'
DB_PASS = 'nhbvbnbk'
DB_HOST = '192.168.22.45'

MAIL_LOGIN     = 'alerts@toyota-ufa.ru'
MAIL_PASSWORD  = 'CjkywtDc[jlbnYfDjcnjrt'
MAIL_SMTP_HOST = 'mx.alfateam.info'
MAIL_SUBJECT   = f'Report'
MAIL_PORT      = 587
MAIL_TO        = 'dkorablev@toyota-ufa.ru'

DEVICE_TYPE_PRINTER = 1
DEVICE_TYPE_MFU     = 2

LOG_LEVEL_EMERGENCY  = 0
LOG_LEVEL_CRITICAL   = 1
LOG_LEVEL_ALERT      = 2
LOG_LEVEL_ERROR      = 3
LOG_LEVEL_WARNING    = 4
LOG_LEVEL_NOTICE     = 5
LOG_LEVEL_INFO       = 6
LOG_LEVEL_DEBUG      = 7
LOG_TO_EMAIL         = True

REP_NAMES = ('short','long','over')