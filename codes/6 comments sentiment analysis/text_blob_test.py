import json
from textblob import TextBlob

def load_comments():
    with open(r'C:\Users\student\Desktop\youtube_comments_biographicaltrailer.json', 'r', encoding='utf8') as comments:
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
    for i in range(51630):
        # trailer info from youtube_comments_biographicaltrailer)
        Title.append(data.get("RECORDS")[i].get("Title"))
        Comments.append(data.get("RECORDS")[i].get("Comments"))
        CommentsLike.append(data.get("RECORDS")[i].get("CommentsLike"))
    for i in range(len(Comments)):
        analysis = TextBlob(Comments[i])
        Polarity.append(analysis.sentiment.polarity)
        Subjectivity.append(analysis.sentiment.subjectivity)
    for i in range(len(Comments)):
        print("%s\n %f\n %f\n" %(Comments[i], Polarity[i], Subjectivity[i]))

'''

text = "The movie is so white."
analysis = TextBlob(text)
print(analysis.sentiment.polarity)
print(analysis.semtiment.subjectivity)
'''
'''
Observation: We can see the output is categorized between two — Polarity and Subjectivity.
Polarity is a float value within the range [-1.0 to 1.0] where 0 indicates neutral, +1 indicates a very positive sentiment and -1 represents a very negative sentiment.
Subjectivity is a float value within the range [0.0 to 1.0] where 0.0 is very objective and 1.0 is very subjective. Subjective sentence expresses some personal feelings, views, beliefs, opinions, allegations, desires, beliefs, suspicions, and speculations where as Objective sentences are factual.
'''