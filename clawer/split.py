#! /usr/local/bin/env python2.7.5
# -*- coding: utf-8

__author__ = 'tom'

fp = open('mal.txt')
fplist = [line for line in fp]
fp1 = open('mal1.txt', 'w')
fp2 = open('mal2.txt', 'w')
for i in xrange(10000):
    fp1.write(fplist[i])
for i in reversed(xrange(20000)):
    fp2.write(fplist[i])
    i = i-1
    if i < 10000:
        break
fp1.close()
fp2.close()
