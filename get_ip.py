# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import urllib2


# 验证ip可用性，可用就加入ip_list
def isAlive(ip):
    proxy_support = urllib2.ProxyHandler({'http': ip})
    opener = urllib2.build_opener(proxy_support)
    # 定制opener
    opener.add_handler = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
    # add_handler给加上伪装
    urllib2.install_opener(opener)
    url = "http://www.baidu.com/"

    try:
        # timeout 设置为5，如果不能忍受你的代理延时超过5，就修改timeout的数字
        resp = urllib2.urlopen(url, timeout=5)

        if resp.code == 200:
            print "\tWork"
            ip_list.append(ip)
            return True

        else:
            print "\tNot work"
            return False
    except:
        print "\tNot work"
        return False

# 获取文件中所有ip
def get_ip_list(data):
    global sum

    for li in data.items():
        sum += 1

        temp2 = li.html()

        p = pq(temp2)
        ip = p('td').eq(1).text()
        port = p('td').eq(2).text()
        proxy = ip + ':' + port
        print 'No: %d\t\t' % sum + proxy
        isAlive(proxy)

# 保存可用ip
def save_ip(ip):
    f1 = open('ip_list.txt', 'w')
    f1.write(str(ip))
    f1.close()


def alive_ip(page):
    for i in xrange(1, int(page) + 1):
        f2 = open('HTML_file/temp%d.html' % i)
        temp1 = f2.read()
        f2.close()
        # print temp1

        d = pq(temp1)
        content = d('tr')

        get_ip_list(content)
        save_ip(ip_list)

    num = len(ip_list)
    print ip_list
    print 'Total: %d\n' % sum + 'Work: %d' % num
    print '-*-*-*-*-*-Complete-*-*-*-*-*-'


ip_list = []
sum = 0

# 在python的函数中和全局同名的变量，如果你有修改变量的值就会变成局部变量，在修改之前对该变量的引用
# 自然就会出现没定义这样的错误了，如果确定要引用全局变量，并且要对它修改，必须加上global关键字。
