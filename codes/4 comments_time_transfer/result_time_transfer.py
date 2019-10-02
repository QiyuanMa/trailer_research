import json
import re
from comments_time_selection.datamanage import DataManager

db = DataManager()


def load_all():
    with open(r'C:\Users\student\Desktop\all_new_movie_trailer_merged_info.json', 'r', encoding='utf8') as trailer:
        trailer_data = json.load(trailer)
        return trailer_data


def load_comments():
    with open(r'C:\Users\student\Desktop\selected_actiontrailersspotlight_textblob.json', 'r', encoding='utf8') as movie:
        movie_data = json.load(movie)
        return movie_data


if __name__ == "__main__":
    all_data = load_all()
    comments_data = load_comments()

    # movie info from new_movie_trailer_merged_info
    Release_Time = []
    movie_transfered_time = []
    title = []

    # trailer comments from youtube_comments_biographicaltrailer
    Title = []
    Title_link = []
    Comments = []
    CommentsTime = []
    CommentsLike = []
    TransferedTime = []
    Comments_sentiment = []
    Comments_subjectivity = []
    Comments_preference = []
    # transfer movie info into all info
    Trailer_title = []
    Trailer_title_link = []
    Trailer_comments = []
    Trailer_comments_time = []
    Trailer_comments_like = []
    Trailer_transfered_time = []
    Trailer_comments_sentiment = []
    Trailer_comments_subjectivity = []
    Trailer_comments_preference = []
    Movie_release_time = []
    Movie_transfered_time = []
    Transfered_time_difference = []

    for i in range(2513):
        # all info from new_movie_trailer_merged_info
        title.append(all_data.get("RECORDS")[i].get("title"))
        Release_Time.append(all_data.get("RECORDS")[i].get("Movie_Release_Time"))
        movie_transfered_time.append(all_data.get("RECORDS")[i].get("Movie_transfered_time"))
    for i in range(109574):
        # trailer info from youtube_comments_biographicaltrailer
        Title.append(comments_data.get("RECORDS")[i].get("Title"))
        Title_link.append(comments_data.get("RECORDS")[i].get("Title_link"))
        Comments.append(comments_data.get("RECORDS")[i].get("Comments"))
        CommentsTime.append(comments_data.get("RECORDS")[i].get("CommentsTime"))
        CommentsLike.append(comments_data.get("RECORDS")[i].get("CommentsLike"))
        TransferedTime.append(comments_data.get("RECORDS")[i].get("TransferedTime"))
        Comments_sentiment.append(comments_data.get("RECORDS")[i].get("Comments_sentiment"))
        Comments_subjectivity.append(comments_data.get("RECORDS")[i].get("Comments_subjectivity"))
        Comments_preference.append(comments_data.get("RECORDS")[i].get("Comments_preference"))
        Trailer_title.append(None)
        Trailer_title_link.append(None)
        Trailer_comments.append(None)
        Trailer_comments_time.append(None)
        Trailer_comments_like.append(None)
        Trailer_transfered_time.append(None)
        Trailer_comments_sentiment.append(None)
        Trailer_comments_subjectivity.append(None)
        Trailer_comments_preference.append(None)
        Movie_release_time.append(None)
        Movie_transfered_time.append(None)
        Transfered_time_difference.append(None)
        # transfer all info into comments info
    #print(movie_transfered_time)
    #for i in range(51630):
        #print(TransferedTime[i])

    for i in range(len(Title)):
        for j in range(len(title)):
            Trailer_title[i] = Title[i]
            Trailer_title_link[i] = Title_link[i]
            Trailer_comments[i] = Comments[i]
            Trailer_comments_time[i] = CommentsTime[i]
            Trailer_comments_like[i] = CommentsLike[i]
            Trailer_transfered_time[i] = TransferedTime[i]
            Trailer_comments_sentiment[i] = Comments_sentiment[i]
            Trailer_comments_subjectivity[i] = Comments_subjectivity[i]
            Trailer_comments_preference[i] = Comments_preference[i]
            if title[j] == Title[i]:
                #print(1)
                Movie_release_time[i] = Release_Time[j]
                if TransferedTime[i] != 'None' and movie_transfered_time[j]!='None':
                    Trailer_transfered_time[i] = int(TransferedTime[i])
                    Movie_transfered_time[i] = int(movie_transfered_time[j])
                    Transfered_time_difference[i] = Trailer_transfered_time[i] - Movie_transfered_time[i]
                #else:
                    #Movie_transfered_time[i] = movie_transfered_time[j]
                    #Transfered_time_difference[i] = None
                # print('%s  %s  %s\n' % (Movie_Title[i], title[i], Movie_Title_link[i]))

        '''
    for i in range(len(Trailer_title)):
        print('%s,%s,%s\n'%
              (
                  Trailer_transfered_time[i], Movie_transfered_time[i], Transfered_time_difference[i]
              ))
        '''

        '''
        print('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' %
              (
                  Trailer_title[i],Trailer_title_link[i],Trailer_comments[i],Trailer_comments_time[i],\
                  Trailer_comments_like[i],Trailer_transfered_time[i],Movie_release_time[i],Movie_transfered_time[i],\
                  Transfered_time_difference[i]
              ))
        '''



        data = (
                  Trailer_title[i],Trailer_title_link[i],Trailer_comments[i],Trailer_comments_time[i],\
                  Trailer_comments_like[i],Trailer_transfered_time[i],Movie_release_time[i],Movie_transfered_time[i],\
                  Transfered_time_difference[i],Trailer_comments_sentiment[i], Trailer_comments_subjectivity[i],Trailer_comments_preference[i]\
              )
        db.save_data(data)


