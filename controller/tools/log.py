from controller.database.table_log import TableLog
class Log :
    def create_log(self,id_log_lavel,message,to_email):
        id_log_subject = 1
        query_data = {'message':f"'{message}'",'to_email':to_email,'id_log_level':id_log_lavel,'id_log_subject':id_log_subject}
        table_log = TableLog()
        table_log.create_log_by_dict(query_data)
    def read_log_by_date(self,date):
        table_log = TableLog()
        log_by_date = table_log.read_log_by_date(date)
        # print(log_by_date)
        return log_by_date
