# -*- coding: utf-8 -*-
import download_html
import get_ip
import time
import os

if __name__ == '__main__':
    page = raw_input('Input the end page number:\n')
    download_html.download(page)
    get_ip.alive_ip(page)
