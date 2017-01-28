# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import urllib2


def save_HTML(num, data):
    f = open('HTML_file/temp%d.html' % num, 'w')
    f.write(str(data))
    f.close()


def get_HTML(page):
    # 伪装成浏览器
    url = 'http://www.xicidaili.com/nn/%s' % page
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    request = urllib2.Request(
        url,
        headers=headers
    )

    temp = urllib2.urlopen(request).read().decode('utf-8')
    d = pq(temp)
    global content
    content = d('tr')

content = ''

def download(end_page):
    for i in xrange(1, int(end_page) + 1):
        try:
            get_HTML(i)
            save_HTML(i, content)
            print 'Page%d downloaded'  % i
        except:
            print 'Fail'