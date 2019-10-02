# Mysql Database，PORT：3306，Assure the client is activated
# install pymysql：pip install pymysql(or File->Setting->Project Interpreter->add...)
import pymysql
import threading
from settings import MYSQL_HOST ,MYSQL_DB ,MYSQL_PWD ,MYSQL_USER
class DataManager():
    # The singleton mode ensures that an object is called every instantiation(Don't need care)
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(DataManager ,"_instance"):
            with DataManager._instance_lock:
                DataManager._instance = object.__new__(cls)
                return DataManager._instance
        return DataManager._instance

    def __init__(self):
        # Create Connection
        self.conn = pymysql.connect(MYSQL_HOST ,MYSQL_USER ,MYSQL_PWD ,MYSQL_DB)
        # Create Cursor
        self.cursor = self.conn.cursor()

    def save_data(self ,data):
        # Database Operation
        # Define a formatted sql statement
        sql = 'insert into new_hotdocs ' \
              '(Trailer_title, Trailer_title_link, Trailer_comments, Trailer_comments_time,\
                  Trailer_comments_like, Trailer_transfered_time, Movie_release_time, Movie_transfered_time,\
                  Transfered_time_difference)' \
              ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'


        # Operation
        try:
            self.cursor.execute(sql ,data)
            self.conn.commit()
        except Exception as e:
            print('Data Insert Failed' ,e)
            self.conn.rollback()  # 回滚

    def __del__(self):
        # Close Cursor
        self.cursor.close()

        # Close Connection
        self.conn.close()




