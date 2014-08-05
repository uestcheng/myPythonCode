#! /usr/local/bin/env python2.7.5
# -*- coding: utf-8

__author__ = 'tom'

import requests
from bs4 import BeautifulSoup


class ClawerAction(object):
    """爬虫类"""
    def downloadurl(self, url):
        """使用request类获取抓取网页"""
        URL = requests.get(url)
        return URL.content

    def urlananlization(self, urlcontent):
        """从网页内容中解析元素"""
        contents = BeautifulSoup(urlcontent)
        return contents

    def getlinks(self, contents):
        """获取即将爬取的链接地址"""
        return (link.get("href") for link in contents.find_all("a"))

    def download