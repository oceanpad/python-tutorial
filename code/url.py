#coding=utf-8
import urllib3
http = urllib3.PoolManager()

'''
r = http.request('get', 'http://oceanpad.github.io')

with open('page_source.html', 'w') as fid:
    fid.write(str(r.data))
'''
r = http.request('GET', 'http://www.baidu.com/')
print(r.status)
print(r.headers['server'])
