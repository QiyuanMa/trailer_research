# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class VideoItem(Item):
    """Video information """
    _id = Field()
    id = Field() #video id
    title = Field() #video title
    description = Field() #video description
    liveBroadcastContent = Field() #live broadcast content
    categoryId = Field() #category id
    viewCount = Field() #view count
    likeCount = Field() #like count
    dislikeCount = Field() # dislike count
    favoriteCount = Field() 
    commentCount = Field() 
    channelId = Field() #user id
    channelTitle = Field() #user name
    tags = Field() #video tags
    comments = Field() #video comments
    recommends =Field() #video recommends
    publishedAt = Field() #publish time

class UserItem(Item):
    """ Channel信息 """
    _id = Field()
    id = Field() #user id
    title = Field() #user title
    description = Field() #description
    country = Field() #country
    favorites = Field() #facorates id
    uploads = Field() #uploaded video id
    commentCount = Field() #user comment count
    subscriberCount = Field() #subscriber count
    hiddenSubscriberCount = Field() #hidden subscriber count
    viewCount = Field() #total view count
    videoCount = Field() #total video count
    publishedAt = Field() #user publish time