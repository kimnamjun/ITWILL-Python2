# -*- coding: utf-8 -*-
"""
문2) 아래와 같은 단계로 kMeans 알고리즘을 적용하여 확인적 군집분석을 수행하시오.

 <조건> 변수 설명 : tot_price : 총구매액, buy_count : 구매횟수, 
                   visit_count : 매장방문횟수, avg_price : 평균구매액

  단계1 : 3개 군집으로 군집화
 
  단계2: 원형데이터에 군집 예측치 추가
  
  단계3 : tot_price 변수와 가장 상관계수가 높은 변수로 산점도(색상 : 클러스터 결과)
  
  단계4 : 산점도에 군집의 중심점 시각화
"""

import pandas as pd
from sklearn.cluster import KMeans # kMeans model
import matplotlib.pyplot as plt


sales = pd.read_csv("../../../data/product_sales.csv")
print(sales.info())
'''
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
tot_price      150 non-null float64 -> 총구매금액 
visit_count    150 non-null float64 -> 매장방문수 
buy_count      150 non-null float64 -> 구매횟수 
avg_price      150 non-null float64 -> 평균구매금액 
'''
print(sales)
kmeans = KMeans(n_clusters=3)
model = kmeans.fit(sales)
pred = model.predict(sales)
centers = model.cluster_centers_
sales['pred'] = pred
plt.scatter(x=sales['tot_price'], y=sales['avg_price'], c=sales['pred'])
plt.scatter(x=centers[:,0], y=centers[:,3], c='r', marker='d')
plt.show()

""" 상관계수 visit_count  buy_count  avg_price
tot_price       0.817954  -0.013051   0.871754 """
