#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
import urllib.request
import urllib
import random

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if(attr[0] == "src"):
                print(attr[1])
                fileName = "./img/" + str(random.randint(1,10000000)) + ".jpg"
                try:
                    urllib.request.urlretrieve(attr[1], fileName)
                except Exception as e:
                    print("error")

with urllib.request.urlopen("http://wallpaperfolder.com/wallpapers/simple+girl") as url:
    s = str(url.read())
    parser = MyHTMLParser()
    parser.feed(s)
