#coding=utf-8
import urllib
import urllib2
import re

url = "https://www.baidu.com"
request = urllib2.Request(url)
page = urllib2.urlopen(url)
html = page.read()
print(html)
