'''
1. news crawling
    url = 'https://media.daum.net'
2. pickle save
    binary file save
'''
import urllib.request as req   # url 요청
from bs4 import BeautifulSoup  # html 파싱

url = 'https://media.daum.net'

# 1. url 요청
req_url = req.urlopen(url)
src = req_url.read()

# 2. html 파싱
src = src.decode('UTF-8')
html = BeautifulSoup(src, 'html.parser')
# print(html)

links = html.select("a[class='link_txt']")
# print(links)

crawling_data = list()
for link in links:
    if link.string is not None:
        crawling_data.append(str(link.string).strip())

print(crawling_data)

# 4. pickle file save
import pickle

with open('../data/news_crawling.pickle', mode='wb') as file:
    pickle.dump(crawling_data, file)
