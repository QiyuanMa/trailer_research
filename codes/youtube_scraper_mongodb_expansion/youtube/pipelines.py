# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
import time

from youtube.items import *


class MongoDBPipeline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["YouTube"]
        self.VideoInfo = db["VideoInfo"]
        self.UserInfo = db["UserInfo"]


    def process_item(self, item, spider):
        """ judge the type of item, and deal with it accordingly, then save into database """
        if isinstance(item, VideoItem):
            try:
                # self.Videoes.save(dict(item))
                self.VideoInfo.insert(dict(item))
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), "counts: ",
                      self.VideoInfo.count() + self.UserInfo.count())
            except Exception:
                pass
        elif isinstance(item, UserItem):
            try:
                self.UserInfo.insert(dict(item))
                # print(self.Users.count())
            except Exception:
                pass
        return item
