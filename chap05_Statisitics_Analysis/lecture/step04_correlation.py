"""
공분산 vs 상관관계(correlation)
- 공통점 : 변수 간의 상관성 분석

1. 공분산 : 두 확률변수 간의 분산(평균에서 퍼짐정도)를 나타내는 통계
 - 두 확률 변수 : X, Y -> X 표본평균(ux), Y 표본평균(uy)
 Cov(X,Y) = sum((X - ux) * (Y - uy)) / n

 Cov(X,Y) > 0 : X 증가하면 Y도 증가
 Cov(X,Y) < 0 : X 증가하면 Y는 감소
 Cov(X,Y)가 0에 가까우면 두 변수는 선형관계가 아님
 문제점 : 값이 큰 변수에 영향을 크게 받는다.

2. 상관계수 : 공분산을 각각의 표준편차로 나누어서 정규화한 통계
 - 부호는 공분산과 동일하고, 절대값이 1을 넘지 않음
 - Cor(X,Y) = Cov(X,Y) / (std(X) * std(Y))
"""
import numpy as np
import pandas as pd

score_iq = pd.read_csv('../../../data/score_iq.csv')
cor = score_iq.corr()
print(cor)

"""
1. 공분산
- score vs iq
- score vs academy

 Cov(X,Y) = sum((X - ux) * (Y - uy)) / n
"""
def Cov(X, Y):
    ux = X.mean()
    uy = Y.mean()
    cov_ret = sum((X - ux) * (Y - uy)) / len(X)
    return cov_ret


X = score_iq['score']
Y1 = score_iq['iq']
Y2 = score_iq['academy']

cov1 = Cov(X, Y1)
cov2 = Cov(X, Y2)
print(cov1, cov2)


"""
2. 상관계수

Cor(X,Y) = Cov(X,Y) / (std(X) * std(Y))
"""
def Cor(X, Y):
    cov = Cov(X, Y)
    std_x = X.std()
    std_y = Y.std()
    cor_ret = cov / (std_x * std_y)
    return cor_ret

cor1 = Cor(X, Y1)
cor2 = Cor(X, Y2)
print(cor1, cor2)

# 특정 두 컬럼의 상관계수를 보고 싶을 때 : 위에서 했던 것과 값이 살짝 다름
print(score_iq['score'].corr(score_iq['iq']))