from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.ptt.cc/bbs/joke/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req).read().decode('utf8')

soup = BeautifulSoup(res, 'html.parser')

title = soup.findAll('div', class_='title')
# print(title)

# print(title[0])
# each_title = title[0].findAll('a')
# print(each_title[0].text)

for title_html in title:
    try:
        print(title_html.findAll('a')[0].text)
    except IndexError as e:
        print(e.args)
    print('=========')