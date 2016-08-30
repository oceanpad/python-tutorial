# -*- coding:utf-8 -*-
import os
import urllib 
import urllib2
import re 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class Spider:
    def _init_(self):
        self.dirName='MMSpider'
        self.url = 'https://www.douban.com/photos/album/83044911/'

    def getPage(self, pageIndex):
        self.url = 'https://www.douban.com/photos/album/83044911/'
        url = self.url + "?start=" + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')

    def getContents(self, pageIndex, j):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div.class=photo_wrap.*?<a.href="(.*?)".class=photolst.*?<img.src="(.*?)".*?<a.href="(.*?)">.*?</div>', re.S)
        #items = re.findall(pattern, page)
        items = ['https://img3.doubanio.com/view/photo/thumb/public/p2245001200.jpg']
        print("****************")
        print(items)
        print("****************")
        for item in items:
            print u'save photos:', item[1]
            print u'get result......'
            print(item[1])
            info = 'https://img3.doubanio.com/view/photo/thumb/public/p2245001200.jpg'
            #info = str(item[1])
            urllib.urlretrieve(info, '%s.jpg' % j)
            j =j + 1

def start():
        x = 0
        j = 0
        spider = Spider()
        spider.getContents(x, j)
        
start()
