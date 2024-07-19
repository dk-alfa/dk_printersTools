import datetime
import dictionary.dic_error as ERROR
def dk_is_date(str):
    ret = False
    try:
        datetime.datetime.strptime(str , '%Y-%m-%d')
        ret = True
    except:
        print(ERROR.DATE_ERROR)
    return ret