"""
회귀방정식에서 기울기(slope)와 절편(intercept) 식
    기울기 = Cov(x,y) / Sxx(x의 편차 제곱 평균)
    절편   = y_mu - (slope * x_mu)
"""
from scipy import stats
import pandas as pd
import numpy as np

galton = pd.read_csv('../../../data/galton.csv')

x = galton['parent']
y = galton['child']

model = stats.linregress(x, y)
# print(model)
# slope=0.6462905819936423, intercept=23.941530180412748,
# rvalue=0.4587623682928238, pvalue=1.7325092920142867e-49, stderr=0.04113588223793335

# y = x * a + b
y_pred = x * model.slope + model.intercept
print(y_pred)

# 예측치 vs 관측치
print(abs(y_pred - y).mean())


# 1. 기울기 계산식(수작업)
# 기울기 = Cov(x,y) / Sxx(x의 편차 제곱 평균)
cov_xy = sum((x - x.mean()) * (y - y.mean())) / len(x)
print(cov_xy)

Sxx = ((x - x.mean()) ** 2).mean()
slope = cov_xy / Sxx
print(slope)  # 0.6462905819936413


# 2. 절편 계산식
# 절편   = y_mu - (slope * x_mu)
intercept = y.mean() - (slope * x.mean())
print(intercept)  # 23.94153018041171


# 3. 설명력(rvalue)
print(galton.corr())
'''        child    parent
child   1.000000  0.458762 <- parent, child 설명력
parent  0.458762  1.000000                     '''
