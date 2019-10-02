# -*- coding: UTF-8 -*-
# This file using Google API(YouTube Data API v3) to scrape data.
# What you only need to do is create a api key at https://console.developers.google.com/
# Limit of Queries per day is 10,000
# Google api instructions: https://developers.google.com/youtube/v3/docs/channels
import time
import json
import datetime
import requests
import urllib.request
import random
import socket





from datamanage import DataManager
db = DataManager()
def getDataFormList(temp_list):
    if len(temp_list) > 0:
        return temp_list[0].strip()
    else:
        return ''


channel = "FRESH Movie Trailers"  # Channel Name
#channel_id = 'UCmLPdGLdejJnb79EPit7cZg'
channel_id = 'UCzNWVDZQ55bjq8uILZ7_wyQ'
#channel_id = 'UCi8e0iOVk1fEOogdfu4YgfA'  # Channel ID

#User-Agent, imitating chrome to visit website, which could avoid being blocked(Don't need care)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}



class YoukuCrawler:
    def __init__(self):
        self.video_ids = []
        self.maxResults = 50  # Number of results returned each time
        # api_key, you must create an api key and change it. (If meet Error:...[item]... , means api key invalid)
        self.app_key = 'AIzaSyD7eEe20XWT2gtha8Eon-CX1XbkVMuZz9I'
        #API key is as below:
        #AIzaSyDuX6VHCt7uS7SdrZ2gJYPXfz2EBaWa_QE
        #AIzaSyD7eEe20XWT2gtha8Eon-CX1XbkVMuZz9I

        #Below you can see two time: "publishedAfter" and "publishedBefore", without them, all your would be repeated. set the duration to get data at specific period.
        self.channel_api = 'https://developers.google.com/apis-explorer/#p/youtube/v3/youtube.channels.list?part=snippet,contentDetails&publishedAfter=2011-01-01T00:00:00Z&publishedBefore=2016-04-07T00:00:00Z&id=' + channel_id + '&key=' + self.app_key
        # self.info_api = 'https://www.googleapis.com/youtube/v3/videos?maxResults=50&part=snippet,statistics' + '&key=' + self.app_key
        self.info_api = 'https://www.googleapis.com/youtube/v3/videos'
        now = time.mktime(datetime.date.today().timetuple())

    def get_all_video_in_channel(self, channel_id):
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        # set the duration to get data at specific period.(Same as above)
        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&publishedAfter=2011-01-01T00:00:00Z&publishedBefore=2016-04-07T00:00:00Z&order=date&maxResults=25'.format(
            self.app_key, channel_id)
        url = first_url

        while True:
            print
            url

            custom_settings = {
                "RANDOM_DELAY": 3,
                "DOWNLOADER_MIDDLEWARES": {
                    "middlewares.random_delay_middleware.RandomDelayMiddleware": 999,
                }
            }

            response = requests.get(url=url,headers = headers)


            page = response.content
            result = json.loads(page, encoding="utf-8")
            #print(page)

            for i in result['items']:
                try:
                    self.video_ids.append(i['id']['videoId'])  # Get Video ID
                except:
                    pass

            try:

                next_page_token = result['nextPageToken']  # Get Next Page
                url = first_url + '&pageToken={}'.format(next_page_token)

            except:
                print
                "no nextPageToken"
                break

    def main(self):
        self.get_all_video_in_channel(channel_id)
        return self.get_videos_info()

    def get_videos_info(self):  # Get Information of Each Video
        url = self.info_api
        query = ''
        count = 0
        f = open(channel_id + '.txt', 'w', encoding="utf-8")
        print
        len(self.video_ids)
        for i in self.video_ids:
                count += 1
                query = i
                results = requests.get(url,
                                       params={'id': query, 'maxResults': self.maxResults, 'part': 'snippet,contentDetails,statistics',
                                               'key': self.app_key})
                page = results.content
                videos = json.loads(page, encoding="utf-8")['items']

                for video in videos:

                    try:
                        like_count = int(video['statistics']['likeCount'])
                    except KeyError:
                        like_count = 0
                    try:
                        dislike_count = int(video['statistics']['dislikeCount'])
                    except KeyError:
                        dislike_count = 0
                    try:
                        comment_count=int(video['statistics']['commentCount'])
                    except KeyError:
                        comment_count = 0

                    #Publish Time
                    temp = time.mktime(time.strptime(video['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%S.000Z"))
                    dateArray = datetime.datetime.utcfromtimestamp(int(temp))
                    otherStyleTime = dateArray.strftime("%Y-%m-%d")

                    print
                    otherStyleTime, count
                    # set the duration to get data at specific period.(Same as above)
                    if (otherStyleTime >= '2011-07-01' and otherStyleTime <= "2016-04-07"):

                        print

                        otherStyleTime,video['snippet']['channelId'],\
                        video['snippet']['title'],video['snippet']['description'],video['snippet']['categoryId'],\
                        video['contentDetails']['duration'],\
                        video['statistics']['viewCount'],like_count,dislike_count,video['statistics']['favoriteCount'],comment_count

                        # Write data to txt.(if you can't see data at database but could see it at txt, that means mistakes in database.)
                        f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
                            otherStyleTime, video['snippet']['channelId'],\
                            video['snippet']['title'], video['snippet']['description'], video['snippet']['categoryId'], \
                            video['contentDetails']['duration'],\
                            video['statistics']['viewCount'], like_count,dislike_count,video['statistics']['favoriteCount'],comment_count
                            ))

                        # Save data to mysql database
                        data = (otherStyleTime, video['snippet']['channelId'], \
                            video['snippet']['title'], video['snippet']['description'], video['snippet']['categoryId'], \
                            video['contentDetails']['duration'],\
                            video['statistics']['viewCount'], like_count,dislike_count,video['statistics']['favoriteCount'],comment_count
                            )
                        db.save_data(data)

                    # set the duration to get data at specific period.(Same as above)
                    if otherStyleTime <= '2011-01-01':
                        return 1

        return 1


if __name__ == "__main__":
    c = YoukuCrawler()
    c.main()
