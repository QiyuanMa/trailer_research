import json
from textblob import TextBlob

def load_comments():
    with open(r'C:\Users\student\Desktop\thriller.json', 'r', encoding='utf8') as comments:
        comments_data = json.load(comments)
        return comments_data

if __name__ == "__main__":
    data = load_comments()
    # trailer comments from youtube_comments_biographicaltrailer
    Title = []
    Comments = []
    CommentsLike = []
    Polarity = []
    Subjectivity = []
    Preference = []
    for i in range(126980):
        # trailer info from youtube_comments_biographicaltrailer)
        Title.append(data.get("RECORDS")[i].get("Title"))
        Comments.append(data.get("RECORDS")[i].get("Comments"))
        CommentsLike.append(data.get("RECORDS")[i].get("CommentsLike"))


    for i in range(len(Comments)):
        analysis = TextBlob(Comments[i])
        Polarity.append((round(analysis.sentiment.polarity,3)))
        Subjectivity.append(round(analysis.sentiment.subjectivity,3))
    for i in range(len(Comments)):
        if int(CommentsLike[i]) != 0:
            Preference.append(round(float(CommentsLike[i])*float(Polarity[i]),3))
        else:
            Preference.append(Polarity[i])

    for i in range(len(Comments)):
        #print(Polarity[i])
        print(Preference[i])

    '''
    polartity_new = open(r"Rolarity.txt", "w", encoding="utf8")
    for i in Polarity:
        #polartity_new.write(i)
        polartity_new.write(i)
        polartity_new.write('\n')
    polartity_new.close()
    '''
    '''
    strlist2 = "\n".join(Subjectivity)
    polartity_new = open("Subjectivity.txt", "w", encoding="utf8")
    polartity_new.write(strlist2)
    polartity_new.close()
    strlist3 = "\n".join(Preference)
    polartity_new = open("Preference.txt", "w", encoding="utf8")
    polartity_new.write(strlist3)
    polartity_new.close()
    '''
