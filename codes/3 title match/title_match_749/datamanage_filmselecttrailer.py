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
        sql = 'insert into new_filmselecttrailer_movie_trailer_merged_info ' \
              '(time, channelId, title, Trailer_series, description, categoryId,' \
              'duration, viewCount, likeCount, dislikeCount, favoriteCount, commentCount,' \
              'Stars, Directors, ReleaseTime, Synopsis, ' \
              'Movie_Title, Movie_Title_link, Movie_certificate, Movie_content,' \
              'Movie_star_rating, Movie_runtime, Movie_content1, Movie_genre,' \
              'Movie_inline_block, Movie_Gross, Movie_Headline, Movie_Director, Movie_Writers,' \
              'Movie_Stars, Movie_Plot_Keywords, Movie_Genres, Movie_Parents_Guide,' \
              'Movie_Official_Sites, Movie_Country, Movie_Language, Movie_Filming_Locations,' \
              'Movie_Gross_USA, Movie_Cumulative_Worldwide_Gross, Movie_Production_Co, Movie_Sound_Mix,' \
              'Movie_Color, Movie_Aspect_Ratio, Movie_Description, Movie_Trailer, Movie_UK_Release_Time,' \
              'Movie_Budget, Movie_US, Movie_Writers_2, Movie_Stars_2, Movie_Stars_3, Movie_Plot_Keywords_2,' \
              'Movie_Plot_Keywords_3, Movie_Plot_Keywords_4, Movie_Plot_Keywords_5, Movie_Storyline)' \
              ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' \
              ',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'


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




