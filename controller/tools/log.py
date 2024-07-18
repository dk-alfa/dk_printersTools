from controller.database.table_log import TableLog
class Log :
    def create_log(self,id_log_lavel,message,to_email):
        id_log_subject = 1
        query_data = {'message':f"'{message}'",'to_email':to_email,'id_log_level':id_log_lavel,'id_log_subject':id_log_subject}
        table_log = TableLog()
        table_log.create_log_by_dict(query_data)
        # table_log.create_log_by_dict(self,query_data)
        # print(query_data)