# This file calculates the duration between release time and the data collection time 2019-08-01
# please export the data all_new_movie_trailer_merged_info into json first.
import json
import re
import time
import calendar
from datetime import datetime
def load_all():
    with open(r'C:\Users\student\Desktop\all_new_movie_trailer_merged_info.json', 'r', encoding='utf8') as movie:
        all_data = json.load(movie)
        return all_data


if __name__ == "__main__":
    all_data = load_all()
    # print (movie_data)
    # movie info from imdb_2013trailerlist_info
    title = []
    Movie_UK_Release_Time = []
    Movie_US = []
    TransferedTime = []
    for i in range(2513):
        # movie info from imdb_2013trailerlist_info
        title.append(all_data.get("RECORDS")[i].get("title"))
        Movie_UK_Release_Time.append(all_data.get("RECORDS")[i].get("Movie_UK_Release_Time"))
        Movie_US.append(all_data.get("RECORDS")[i].get("Movie_US"))
    for i in range(len(title)):
        if Movie_UK_Release_Time[i]:
            day = str(Movie_UK_Release_Time[i].split(' ')[0]).zfill(2)
            months = str(list(calendar.month_name).index(Movie_UK_Release_Time[i].split(' ')[1])).zfill(2)
            year = Movie_UK_Release_Time[i].split(' ')[2]
            start_data = '%s-%s-%s'%(year,months,day)
            #print(start_data)
            '''
            end_date = '2019-08-01'
            start_sec = time.mktime(time.strptime(start_data, '%Y-%m-%d'))
            end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
            duration = int((end_sec - start_sec)/(24*60*60))
            '''
            start = datetime(int(year),int(months),int(day))
            print(start)
            end = datetime(2019,8,1)
            duration = end - start
            TransferedTime.append(duration)
        else:
            TransferedTime.append(None)
            print(None)



