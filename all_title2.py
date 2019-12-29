from urllib import request
import requests
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'https://www.ptt.cc/bbs/movie/index.html'
for i in range(0,10):
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(res, 'html.parser')

    title = soup.select('div[class="title"] a')

    for each_title in title:
        print(each_title.text)
        try:
            article_url = 'https://www.ptt.cc' + each_title['href']
            print(article_url)
            res_article = requests.get(article_url, headers=headers)
            article_soup = BeautifulSoup(res_article.text, 'htnml.parser')
        except KeyError as e:
            print(e.args)
        print()

    url_list = soup.select('div[class="btn-group btn-group-paging"] a[class="btn wide"]')
    url = 'https://www.ptt.cc' + url_list[1]['href']
