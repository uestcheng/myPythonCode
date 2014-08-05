#! /usr/local/bin/env python2.7.5
# -*- coding: utf-8

__author__ = 'tom'
#TODO (tom) 为ClawerAction加入重复判断功能 before 2014-08-06
#TODO (tom) 为ClawerAction加入代理功能     before 2014-08-06

import time
import requests
from requests.exceptions import SSLError
from requests.exceptions import ConnectionError


class ClawerAction(object):
    """使用requests库爬取对应的网页, 并进行解析
    参数：
        target:待爬取的url地址
        targetdict: 爬取的url字典
        header:伪造的header头
        url：固定的获取信息网址
        content:返回内容的response部分
    """

    def __init__(self):
        """初始化URL和header"""
        self.url = "https://www.virustotal.com/zh-cn/url/submission/"
        self.header = {"referer":"https://www.virustotal.com/zh-cn/"}
        self._INTERVAL = 3

    def requestpost(self, target, url=None, header=None):
        """发送伪造的协议获取返回值，返回值为字符串"""
        targetdict = {"url": target}
        try:
            r = requests.post(self.url, data=targetdict, headers=self.header)
        except SSLError:
            print "download %s again " % target
        except ConnectionError:
            print "download %s again " % target
        except UnboundLocalError:
            print "download %s again " % target
        else:
            return r.content

    def pageextra(self, content):
        """把返回的字符串进行格式化生成字典"""
        value = content.replace("true", "True")
        return eval(value)


def getthetarget(filepath):
    """读取文件进行文档解析出爬取目标:target和类型:target,返回值为生成式"""
    fp = open(filepath)
    urllist = [line for line in fp]
     #按照制表符进行分割,返回生成式
    urllist = [urllist[i].split('\t') for i in xrange(len(urllist))]
    return urllist


if __name__ == '__main__':
    ca = ClawerAction()
    fp = getthetarget("malDomains.txt")
    fp1 = open("malurl.txt", 'w')
    count = 0
    for url in fp:
        print "get the %s" % url[0]
        content = ca.requestpost(url[0])
        if type(content) == str:
            contentdict = ca.pageextra(content)
        else:
            continue
        if "positives" in contentdict.keys() and "total" in contentdict.keys():
            possibility = "%s/%s" % (contentdict["positives"], contentdict["total"])
            fp1.write(url[0])
            fp1.write(",")
            fp1.write(possibility)
            fp1.write('\n')
        else:
            fp1.write("response error! \n")
        count = count + 1
        print "the %dth page is over " % count
    fp1.close()