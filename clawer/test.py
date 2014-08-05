#! /usr/local/bin/env python2.7.5
# -*- coding: utf-8

__author__ = 'tom'
import time
import requests
import random


fp = open('mal.txt')
URL = "https://www.virustotal.com/zh-cn/url/submission/"
HEADER = {"referer":"https://www.virustotal.com/zh-cn/"}
urllist = [line for line in fp]
fp1 = open('malurl.txt', 'a')
num = len(urllist)
count = 0
for i in xrange(len(urllist)):
    #INTERVAL = random.randint(1, 5)

    data = "http://%s" % urllist[i]

    datadict = {"url":data}
    print "%s is over" % data
    print r.content
    content = r.content.replace("true", "True")
    newcontent = eval(content)
    #print newcontent
    possibility = "%d / %d" % (newcontent["positives"], newcontent["total"])
    exists = "%d" % newcontent["url_exists"]
    fp1.write(data)
    fp1.write(",")
    fp1.write(possibility)
    fp1.write(",")
    fp1.write(exists)
    fp1.write("\n")
    num = num - 1
    count = count + 1
    print "there is %d urls left" % num
    #print "waiting %d seconds" % INTERVAL
    print "%d" % count
    #time.sleep(INTERVAL)
fp1.close()

