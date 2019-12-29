from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = 'http://8f7c891f.ngrok.io/hello_get?name=Allen'
url2 = 'https://www.ptt.cc/bbs/joke/index.html'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

res = request.urlopen(url)

req = request.Request(url=url2, headers=headers)
res2 = request.urlopen(req)

# print(res.read().decode('utf8'))
print(res2.read().decode('utf8'))

