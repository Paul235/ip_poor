# ip_poor
爬一些可用的代理ip

ip 来源网站 http://www.xicidaili.com/nn/

##说明
1. download_HTML.py: 把网页源码的ip列表部分下载，以 HTML 格式存进 HTML_file 文件夹中；
2. get_ip.py: 将 ip 地址及端口号从 HTML 文件中抓出来，并验证可用性，可用的存入 ip_list ，并保存为 txt 文本文件；
3. main.py: 主程序，接收爬取页码。
