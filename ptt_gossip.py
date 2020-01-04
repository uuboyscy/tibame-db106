import requests
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
import os

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

ss = requests.session()
ss.cookies['over18'] = '1'

path = r'./res_gossip'
if not os.path.exists(path):
    os.mkdir(path)

for i in range(0,10):
    res = ss.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('div[class="title"] a')

    for each_title in title:
        print(each_title.text)
        try:
            article_url = 'https://www.ptt.cc' + each_title['href']
            print(article_url)
            res_article = ss.get(article_url, headers=headers)
            article_soup = BeautifulSoup(res_article.text, 'html.parser')
            tem_str = article_soup.select('div[id="main-content"]')[0].text.split('--')[0]

            tag_up = 0
            tag_down = 0
            score = 0
            auth = ''
            article_name = each_title.text
            article_date = ''

            with open(path + '/' + each_title.text + '.txt', 'w', encoding='utf8') as f:
                f.write(tem_str)
        except KeyError as e:
            print(e.args)
        except:
            print(each_title.text)
        print()

    url_list = soup.select('div[class="btn-group btn-group-paging"] a[class="btn wide"]')
    url = 'https://www.ptt.cc' + url_list[1]['href']
