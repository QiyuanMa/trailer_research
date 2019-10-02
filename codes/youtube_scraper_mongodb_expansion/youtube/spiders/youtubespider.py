# -*- coding: utf-8 -*-
from youtube.config import videoID
from scrapy import Request, Spider
from youtube.items import *
import time,datetime
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
import re
import json
from lxml import etree
from scrapy.selector import Selector


class YoutubespiderSpider(Spider):
    apikey='AIzaSyD7eEe20XWT2gtha8Eon-CX1XbkVMuZz9I'
    name = 'youtubespider'
    allowed_domains = ['youtube.com']
    start_urls = ['http://youtube.com/']
    start_videoes = list(set(videoID))
    DEVELOPER_KEY = 'AIzaSyD7eEe20XWT2gtha8Eon-CX1XbkVMuZz9I'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    # video information API
    video_url = 'https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id={vid}&key={key}'
    # user information API
    user_url = 'https://www.googleapis.com/youtube/v3/channels?part=snippet,contentDetails,statistics&id={uid}&key={key}'
    # recommand video API
    recommend_url = 'https://www.googleapis.com/youtube/v3/search?type=video&part=id&maxResults=50pageToken={page}relatedToVideoId={vid}&key={key}'
    # transfer information API
    # transfer_url = 'https://weibo.com/aj/v6/mblog/info/big?ajwvr=6&id={mid}&max_id=None&page={page}'
    # comments API
    '''Get all comments by time by default'''
    # comment_url = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id={mid}&root_comment_max_id={root_comment_max_id}&page={page}&filter=all&from=singleWeiBo'
    '''Get all comments by popularity by default'''
    # comment_url = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id={mid}&filter=hot&from=singleWeiBo'

    def getUserInfo(self,uid):
        # See full sample for function
        # kwargs = remove_empty_kwargs(**kwargs)

        response = self.youtube.channels().list(
            part='snippet,contentDetails,statistics',
            id=uid
        ).execute()
        return response

    def getrelatedvideo(self, relatedToVideoId):
        # return recommended videos for a video 
        nextPageToken = ''
        recommends = []
        while nextPageToken != None:
            response = self.youtube.search().list(
                relatedToVideoId=relatedToVideoId,
                type='video',
                part='id',
                maxResults=50,
                pageToken=nextPageToken
            ).execute()
            try:
                nextPageToken = response["nextPageToken"]
            except:
                nextPageToken = None
            items = response.get('items', [])
            if len(items) != 0:
                for item in items:
                    recommends.append(item['id']['videoId'])
            else:
                break
        return recommends

    def start_requests(self):
        for vid in self.start_videoes:
            yield Request(self.video_url.format(vid=vid,key=self.apikey), callback=self.parse_Video,meta={'vid': vid})

    def parse_Video(self, response):
        """ collect video information """
        videoitem = VideoItem()
        result = json.loads(response.text)
        items = result.get('items')[0]
        snippet = items["snippet"]
        statistics = items["statistics"]
        _id = response.meta.get('vid')
        id = _id
        title = snippet["title"]
        description = snippet["description"]
        channelId = snippet["channelId"]
        channelTitle = snippet["channelTitle"]
        categoryId = int(snippet["categoryId"])
        liveBroadcastContent = snippet["liveBroadcastContent"]
        try:
            viewCount=int(statistics["viewCount"])
        except:
            viewCount=0
        try:
            likeCount=int(statistics["likeCount"])
        except:
            likeCount=0
        try:
            dislikeCount=int(statistics["dislikeCount"])
        except:
            dislikeCount=0
        try:
            favoriteCount=int(statistics["favoriteCount"])
        except:
            favoriteCount=0
        try:
            commentCount=int(statistics["commentCount"])
        except:
            commentCount=0
        try:
            tags = snippet["tags"]
        except:
            tags = []
        comments = []
        recommends = self.getrelatedvideo(id)
        publishedAt = snippet["publishedAt"]
        publishedAt= datetime.datetime.strptime(publishedAt, "%Y-%m-%dT%H:%M:%S.000Z")
        videoitem["_id"] = _id
        videoitem["id"] = id
        videoitem["title"] = title
        videoitem["description"] = description
        videoitem["channelId"] = channelId
        videoitem["channelTitle"] = channelTitle
        videoitem["categoryId"] = categoryId
        videoitem["liveBroadcastContent"] = liveBroadcastContent
        videoitem["viewCount"] = viewCount
        videoitem["likeCount"] = likeCount
        videoitem["dislikeCount"] = dislikeCount
        videoitem["favoriteCount"] = favoriteCount
        videoitem["commentCount"] = commentCount
        videoitem["publishedAt"] = publishedAt
        videoitem["recommends"] = recommends
        videoitem["tags"] = tags
        # yield Request(self.user_url.format(uid=channelId, key=self.apikey), callback=self.parse_User,
        #               meta={'uid': channelId,'recommends':recommends,'videoitem':videoitem}, dont_filter=True)
        yield Request(self.user_url.format(uid=channelId, key=self.apikey), callback=self.parse_User,
                      meta={'uid': channelId}, dont_filter=True)
        yield videoitem
        for vid in recommends:
            yield Request(self.video_url.format(vid=vid, key=self.apikey), callback=self.parse_Video, meta={'vid': vid},dont_filter=True)
    def parse_User(self, response):
        """ collect user information """
        useritem = UserItem()
        result = json.loads(response.text)
        result1 = self.getUserInfo(response.meta.get('uid'))
        items = result.get('items')[0]
        snippet = items["snippet"]
        relatedPlaylists = result1["items"][0]["contentDetails"]["relatedPlaylists"]
        statistics = items["statistics"]
        _id = response.meta.get('uid')
        recommends=response.meta.get('recommends')
        videoitem=response.meta.get('videoitem')
        id = _id
        title = snippet["title"]
        description = snippet["description"]
        try:
            country = snippet["country"]
        except:
            country = "unknown"
        uploads = relatedPlaylists["uploads"]
        try:
            favorites = relatedPlaylists["favorites"]
        except:
            favorites = 0
        viewCount = statistics["viewCount"]
        commentCount = statistics["commentCount"]
        subscriberCount = statistics["subscriberCount"]
        hiddenSubscriberCount = statistics["hiddenSubscriberCount"]
        videoCount = statistics["videoCount"]
        publishedAt = snippet["publishedAt"]
        publishedAt = datetime.datetime.strptime(publishedAt, "%Y-%m-%dT%H:%M:%S.000Z")
        useritem["_id"] = _id
        useritem["id"] = id
        useritem["title"] = title
        useritem["description"] = description
        useritem["country"] = country
        useritem["uploads"] = uploads
        useritem["favorites"] = favorites
        useritem["commentCount"] = commentCount
        useritem["subscriberCount"] = subscriberCount
        useritem["hiddenSubscriberCount"] = hiddenSubscriberCount
        useritem["videoCount"] = int(videoCount)
        useritem["viewCount"] = int(viewCount)
        useritem["publishedAt"] = publishedAt
        yield useritem
