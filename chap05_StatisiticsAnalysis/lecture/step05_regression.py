"""
scipy 패키지의 stats 모듈의 함수
- 통계적인 방식의 회귀분석
1. 단순선형회귀모델
2. 다중선형회귀모델
"""
from scipy import stats
import pandas as pd

# 1. 단순선형회귀모델
score_iq = pd.read_csv('../../../data/score_iq.csv')

x = score_iq['iq']
y = score_iq['score']

# 회귀모델 생성
model = stats.linregress(x, y)
print(model)
# slope=0.6514309527270075       : 기울기
# intercept=-2.8564471221974657  : 절편
# rvalue=0.8822203446134699      : 설명력
# pvalue=2.8476895206683644e-50  : x의 유의성 검정
# stderr=0.028577934409305443    : 표본 오차

# Y = X * a + b
X = 140
Y = X * model.slope + model.intercept
print(Y)

###############
# product.csv #
###############
product = pd.read_csv('../../../data/product.csv')
# X : 제품적절성 -> Y : 제품만족도
model2 = stats.linregress(product['b'], product['c'])
print(model2)

X = product['b']
Y_true = product['c']
Y_pred = X * model2.slope + model2.intercept
err = abs(Y_pred - Y_true)
print(err)


# 2. 회귀모델 시각화
from pylab import plot, legend, show
plot(X, Y_true, 'b.')   # 산점도
plot(X, Y_pred, 'r.-')  # 회귀선
legend(['x, y scatter', 'regress model line'])
show()


# 다중 선형회귀모델
from statsmodels.formula.api import ols  # function
wine = pd.read_csv('../../../data/winequality-both.csv')

wine.columns = wine.columns.str.replace(' ', '_')

# quality vs other
cor = wine.corr()
print(cor['quality'])
formula ="quality ~ alcohol + chlorides + volatile_acidity"

model = ols(formula, data=wine).fit()
print(model)
print(model.summary())
# Adj, R-squared : 설명력(예측력)
# F-statistic
# Prob (F-statistic)
# X의 유의성 검정

# 기울기, 절편
print(model.params)

# y의 예측치 vs 관측치
y_pred = model.fittedvalues
y_true = wine['quality']

err = (y_true - y_pred) ** 2
print(err)


# 차트 확인
import matplotlib.pyplot as plt
plt.plot(y_true[:10], 'b', label='real values')
plt.plot(y_pred[:10], 'r', label='prediction')
plt.yticks(range(0, 10))
plt.legend(loc='best')
plt.show()