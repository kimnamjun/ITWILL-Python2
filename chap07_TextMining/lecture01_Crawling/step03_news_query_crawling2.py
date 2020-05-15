"""
방법2) url query 이용 : 연도별 뉴스 자료 수집
    ex) 2015.01.01 ~ 2020.01.01
        page: 1 ~ 5
"""
import urllib.request as req
from bs4 import BeautifulSoup
import pandas as pd
import re

# 1. 수집 연도 생성 : 시계열 date 이용
date = pd.date_range('2015-01-01', '2020-01-01')
print(len(date))  # 1827

sdate = [re.sub('-','',str(d))[:8] for d in date]

# 2. crawler 함수
def news_crawler(date, pages=5):
    crawling_data = list()

    for page in range(1, pages+1):
        url = f'https://news.daum.net/newsbox?regDate={date}&page={page}'
        try:
            # 1. url 요청
            req_url = req.urlopen(url)
            src = req_url.read()

            # 2. html 파싱
            src = src.decode('UTF-8')
            html = BeautifulSoup(src, 'html.parser')

            links = html.select("a[class='link_txt']")

            for link in links[:40]:
                if link.string is not None:
                    crawling_data.append(str(link.string).strip())

        except Exception as err:
            print(f'오류 발생 : {date} : {page}')

    return crawling_data

# 3. crawler 함수 호출
year5_news_date = [news_crawler(date)[:1] for date in sdate]
