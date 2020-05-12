# -*- coding: utf-8 -*-
"""
문01) 이항검정 : 토요일(Sat)에 오는 여자 손님 중 비흡연자가 흡연자 보다 많다고 할 수 있는가?

 # 귀무가설 : 비흡연자와 흡연자의 비율은 차이가 없다.(P=0.5)
"""
import numpy as np
import pandas as pd
from  scipy import stats

tips = pd.read_csv("../../../data/tips.csv")
print(tips.info())
print(tips.head())

day = tips['day']
print(day.value_counts())
'''
Sat     87  -> 토요일 빈도수 
Sun     76
Thur    62
Fri     19
'''

gender = tips['sex']
print(gender.value_counts())
'''
Male      157
Female     87 -> 여자 빈도수
'''
data = tips[np.logical_and(tips['sex']=='Female', tips['day']=='Sat')]
no = len(data[data['smoker']=='No'])

pvalue = stats.binom_test(no, len(data), alternative='greater')
print(pvalue)
print('비흡연자가 많다고 할 수 없다.' if pvalue >= 0.05 else '비흡연자가 많다고 할 수 있다.')