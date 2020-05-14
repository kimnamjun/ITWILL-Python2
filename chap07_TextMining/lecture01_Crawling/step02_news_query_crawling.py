"""
news Crawling : url query
url : 'https://media.daum.net'                                -> [배열 이력]
url : 'https://media.daum.net/newsbox'            -> base url -> [특정 날짜]
url : 'https://news.daum.net/newsbox?regDate=20200505'        -> [특정 페이지]
url : 'https://news.daum.net/newsbox?regDate=20200505&page=2'
"""
import urllib.request as req   # url 요청
from bs4 import BeautifulSoup  # html 파싱

# 1. url query 만들기
"""
date: 2020.02.01 ~ 2020.02.29
page: 1 ~ 10
"""

base_url = 'https://media.daum.net/newsbox?regDate='
date = list(range(20200201,20200230))

url_list = [base_url + str(d) for d in date]
# print(url_list)

# base url + date + page

page = list(range(1,11))
pages = ['&page=' + str(p) for p in page]

final_url = []

for url in url_list:
    for page in pages:
        final_url.append(url + page)
print(final_url)

# crawler 함수 정의
def crawler(url):
    # 1. url 요청
    req_url = req.urlopen(url)
    src = req_url.read()

    # 2. html 파싱
    src = src.decode('UTF-8')
    html = BeautifulSoup(src, 'html.parser')

    links = html.select("a[class='link_txt']")

    crawling_data = list()
    for link in links:
        if link.string is not None:
            crawling_data.append(str(link.string).strip())

    return crawling_data

# 해당 기사 추출
print(crawler(final_url[0])[:40])  # 40 이후로는 뉴스 기사 아님

# 2월(1개월) 전체 news 수집
month_news = []

# 3. crawler 함수 호출
page_cnt = 0
for url in final_url:
    try:
        page_cnt += 1
        one_page = crawler(url)
        print('page :', page_cnt)
        print(one_page)
        month_news.extend(one_page)
    except Exception as err:
        print('해당 url 없음', url)
        raise err

len(month_news)  # 11600 : 29일 * 10페이지 * 40개 기사

# 4. binary file save
import pickle
# 저장
file = open('../data/news_data.pickle', mode='wb')
pickle.dump(month_news, file)
file.close()

# 불러오기
file = open('../data/news_data.pickle', mode='rb')
month_news2 = pickle.load(file)
print(month_news2)
file.close()