# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from youtube.user_agents import agents
from youtube.cookies import init_cookies,cookies



class UserAgentMiddleware(object):
    """ change User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ change Cookie """

    def __init__(self):
        init_cookies()

    def process_request(self, request, spider):
        url = request.url
        cookie = random.choice(cookies)
        request.cookies = cookie