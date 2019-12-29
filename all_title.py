from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}


page = 8660
for i in range(0,10):
    url = 'https://www.ptt.cc/bbs/movie/index%s.html'%(page)

    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(res, 'html.parser')

    title = soup.select('div[class="title"] a')

    for each_title in title:
        print(each_title.text)
        try:
            print('https://www.ptt.cc' + each_title['href'])
        except KeyError as e:
            print(e.args)
        print()

    page -= 1