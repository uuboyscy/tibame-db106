from selenium.webdriver import Chrome

driver = Chrome('./chromedriver')

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)

driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()

cookies_dict = driver.get_cookies()
print(cookies_dict)

driver.close()

import requests
from bs4 import BeautifulSoup

ss = requests.session()
for c in cookies_dict:
    ss.cookies.set(c['name'], c['value'])

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

res = ss.get(url)
soup = BeautifulSoup(res.text,'html.parser')
# print(soup.prettify())
print(ss.cookies)