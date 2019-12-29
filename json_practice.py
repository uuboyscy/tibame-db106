import requests
import json
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os

if not os.path.exists(r'./dcard_img'):
    os.mkdir(r'./dcard_img')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232762503'
res = requests.get(url, headers=headers)
# print(res.text)
tmp_json = json.loads(res.text)

for each_title in tmp_json:
    article_title = each_title['title'].replace('/', '')
    if not os.path.exists(r'./dcard_img/%s'%(article_title)):
        os.mkdir(r'./dcard_img/%s'%(article_title))
    print(article_title)
    print('https://www.dcard.tw/f/photography/p/' + str(each_title['id']))
    for img_url_dict in each_title['mediaMeta']:
        img_url = img_url_dict['url']
        try:
            request.urlretrieve(img_url, r'./dcard_img/%s/%s'%(article_title, img_url.split('/')[-1]))
        except:
            pass
        print('\t%s'%(img_url))

    print()
