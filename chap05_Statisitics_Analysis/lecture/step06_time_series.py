"""
시계열 분석(time series analysis)
1. 시계열 자료 생성
2. 날짜 형식 수정(다국어)
3. 시계열 시각화
4. 이동평균 기능 : 5, 10, 20일 단위 평균 -> 추세선 평활(스뮤딩)
"""
from datetime import datetime    # 날짜형식 수정
import pandas as pd              # csv file read
import matplotlib.pyplot as plt  # 시계열 시각화
import numpy as np               # 수치 자료 생성

# 1. 시계열 자료 생성
time_data = pd.date_range('2017-03-01', '2020-03-30')
print(time_data)
time_data2 = pd.date_range('2017-03-01', '2020-03-30', freq='M')
print(time_data2)

# 월 단위 매출 현황
x = pd.Series(np.random.uniform(10, 100, size=36))
df = pd.DataFrame({"date":time_data2, 'price': x})
plt.plot(df['date'], df['price'], 'g--')
plt.show()


# 2. 날짜형식 수정(다국어)
cospi = pd.read_csv('../../../data/cospi.csv')
date = cospi['Date']

# 날짜 형식 변경 : 26-Feb-16 -> 2016-02-16
kdate = [datetime.strptime(d, '%d-%b-%y') for d in date]
cospi['Date'] = kdate
print(cospi.head())


# 3. 시계열 시각화
cospi.index

new_cospi = cospi.set_index('Date')  # 컬럼을 row의 index로 사용
print(new_cospi)

print(new_cospi['2015'])
print(new_cospi['2015-05':'2015-03'])  # 순서 주의

new_cospi_HL = new_cospi[['High','Low']]
new_cospi_HL['2015'].plot(title='2015 year vs Low')
plt.show()

new_cospi_HL['2016-02'].plot(title='2016-02 year vs Low')
plt.show()