#!/usr/bin/env python
# encoding: utf-8
import datetime
import json
import base64
from time import sleep

import pymongo
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WeiBoAccounts = [
    {'username': 'Letloving@163.com', 'password': '1234567'}
]

cookies = []
client = pymongo.MongoClient("localhost", 27017)
db = client["YouTube"]
Cookies = db["Cookies"]


def get_cookie_from_weibo(username, password):
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/watch?v=qeau7UWjEms&list=PLScC8g4bqD461pCfNojDx0fVxjGl7Og_4')
    sleep(25)
    # login_name = driver.find_element_by_name("username")
    # login_password = driver.find_element_by_name("password")
    # login_name.send_keys(username)
    # login_password.send_keys(password)
    # login_button = driver.find_element_by_class_name('W_login_form').find_element_by_link_text('log in')
    # login_button.click()
    # # sleep for 10 seconds to see if the Chrome started successfully, if not, log in manually.
    # sleep(20)
    cookie = driver.get_cookies()
    driver.close()
    return cookie




def init_cookies():
    for cookie in Cookies.find():
        cookies.append(cookie['cookie'])


if __name__ == "__main__":
    try:
        Cookies.drop()
    except Exception as e:
        pass

    for account in WeiBoAccounts:
        cookie=get_cookie_from_weibo(account["username"], account["password"])
        if cookie!=None:
            Cookies.insert_one({"cookie": cookie})