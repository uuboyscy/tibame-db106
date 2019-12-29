import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

url = 'https://buzzorange.com/techorange/'
post_url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

# post_data_str = """action: fm_ajax_load_more
# nonce: 0b336c2ae9
# page: 7"""

post_data = {'action': 'fm_ajax_load_more', 'nonce': '0b336c2ae9', 'page': '0'}

# for i in post_data_str.split('\n'):
#     post_data[i.split(': ')[0]] = i.split(': ')[1]
#
# post_data['page'] = '0'
# print(post_data)

for p in range(0,5):
    post_data['page'] = str(p)
    res = requests.post(post_url, headers = headers, data=post_data)
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup)
