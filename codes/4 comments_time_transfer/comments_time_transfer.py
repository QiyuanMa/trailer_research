import unittest
# This program aims at transfeting the youtube commentstime like "1 days ago", "2 months ago", "1 year ago" into int "1", "60", "365".
# I use the transfered number to compare to the movie release time, finally divide comments into pre-release data and post-release data.
import json
import re
#from title_match_749.datamanageoblomovietrailer import DataManager
#db = DataManager()


def load_trailer():
    with open(r'C:\Users\student\Desktop\youtube_comments_selected_actiontrailersspotlight.json', 'r', encoding='utf8') as trailer:
        trailer_data = json.load(trailer)
        return trailer_data


if __name__ == "__main__":
    comments_data = load_trailer()
    # print (movie_data)
    # movie info from imdb_2013trailerlist_info
    Title = []
    Title_link = []
    Comments = []
    CommentsTime = []
    CommentsLike = []
    TransferedTime = []
    for i in range(54787):
        # movie info from imdb_2013trailerlist_info
        Title.append(comments_data.get("RECORDS")[i].get("Title"))
        Title_link.append(comments_data.get("RECORDS")[i].get("Title_link"))
        Comments.append(comments_data.get("RECORDS")[i].get("Comments"))
        CommentsTime.append(comments_data.get("RECORDS")[i].get("CommentsTime"))
        CommentsLike.append(comments_data.get("RECORDS")[i].get("ipl-rating-star__rating"))
    #print(Title)
    '''
    for i in range(len(Title)):
        print(Title[i])
    '''
    for i in range(len(Title)):
        # if hour, then 0+1
        if re.search('hour',CommentsTime[i]) != None:
            TransferedTime.append(1)
        elif re.search('hours',CommentsTime[i]) != None:
            TransferedTime.append(1)
        # if day, then 1~6+1
        elif re.match('1 day ago',CommentsTime[i]) != None:
            TransferedTime.append(2)
        elif re.match('2 days ago',CommentsTime[i]) != None:
            TransferedTime.append(3)
        elif re.match('3 days ago',CommentsTime[i]) != None:
            TransferedTime.append(4)
        elif re.match('4 days ago',CommentsTime[i]) != None:
            TransferedTime.append(5)
        elif re.match('5 days ago',CommentsTime[i]) != None:
            TransferedTime.append(6)
        elif re.match('6 days ago',CommentsTime[i]) != None:
            TransferedTime.append(7)
        # if week, then 7*1~4+6
        elif re.match('1 week ago',CommentsTime[i]) != None:
            TransferedTime.append(13)
        elif re.match('2 weeks ago',CommentsTime[i]) != None:
            TransferedTime.append(20)
        elif re.match('3 weeks ago',CommentsTime[i]) != None:
            TransferedTime.append(27)
        elif re.match('4 weeks ago',CommentsTime[i]) != None:
            TransferedTime.append(34)
        elif re.match('5 weeks ago',CommentsTime[i]) != None:
            TransferedTime.append(41)
        # if month, then 30*1~11+29
        elif re.match('1 month ago',CommentsTime[i]) != None:
            TransferedTime.append(59)
        elif re.match('2 months ago',CommentsTime[i]) != None:
            TransferedTime.append(89)
        elif re.match('3 months ago',CommentsTime[i]) != None:
            TransferedTime.append(119)
        elif re.match('4 months ago',CommentsTime[i]) != None:
            TransferedTime.append(149)
        elif re.match('5 months ago',CommentsTime[i]) != None:
            TransferedTime.append(179)
        elif re.match('6 months ago',CommentsTime[i]) != None:
            TransferedTime.append(209)
        elif re.match('7 months ago',CommentsTime[i]) != None:
            TransferedTime.append(239)
        elif re.match('8 months ago',CommentsTime[i]) != None:
            TransferedTime.append(269)
        elif re.match('9 months ago',CommentsTime[i]) != None:
            TransferedTime.append(299)
        elif re.match('10 months ago',CommentsTime[i]) != None:
            TransferedTime.append(329)
        elif re.match('11 months ago',CommentsTime[i]) != None:
            TransferedTime.append(364)
        # if year, then 364+365*1~8
        elif re.match('1 year ago',CommentsTime[i]) != None:
            TransferedTime.append(729)
        elif re.match('2 years ago',CommentsTime[i]) != None:
            TransferedTime.append(1094)
        elif re.match('3 years ago',CommentsTime[i]) != None:
            TransferedTime.append(1459)
        elif re.match('4 years ago',CommentsTime[i]) != None:
            TransferedTime.append(1824)
        elif re.match('5 years ago',CommentsTime[i]) != None:
            TransferedTime.append(2189)
        elif re.match('6 years ago',CommentsTime[i]) != None:
            TransferedTime.append(2554)
        elif re.match('7 years ago',CommentsTime[i]) != None:
            TransferedTime.append(2919)
        elif re.match('8 years ago',CommentsTime[i]) != None:
            TransferedTime.append(3284)
        else:
            TransferedTime.append(0)
    '''
    for i in range(len(Title)):
        print(TransferedTime[i])
    '''
    txtnew=open(r"TransferedTime.txt","w", encoding="utf8")
    for i in TransferedTime:
        txtnew.write('%d' % i)
        txtnew.write('\n')
    txtnew.close()
