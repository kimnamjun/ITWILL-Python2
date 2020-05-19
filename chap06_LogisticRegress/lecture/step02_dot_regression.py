"""
행렬곱 함수(np.dot) 이용 y 예측치 구하기
y_pred = np.dot(X, a) + b
"""
from scipy import stats
from statsmodels.formula.api import ols
import pandas as pd
import numpy as np

# 1. dataset load
score = pd.read_csv('../../../data/score_iq.csv')

formula = 'score ~ iq + academy'
model = ols(formula, data=score).fit()
print(model.params)

# model 결과 확인
print(model.summary())
'''
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  score   R-squared:                       0.946
Model:                            OLS   Adj. R-squared:                  0.946
Method:                 Least Squares   F-statistic:                     1295.
Date:                Tue, 12 May 2020   Prob (F-statistic):           4.50e-94
Time:                        11:45:37   Log-Likelihood:                -275.05
No. Observations:                 150   AIC:                             556.1
Df Residuals:                     147   BIC:                             565.1
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     25.2291      2.187     11.537      0.000      20.907      29.551
iq             0.3770      0.019     19.786      0.000       0.339       0.415
academy        2.9928      0.140     21.444      0.000       2.717       3.269
==============================================================================
Omnibus:                       36.342   Durbin-Watson:                   1.913
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               54.697
Skew:                           1.286   Prob(JB):                     1.33e-12
Kurtosis:                       4.461   Cond. No.                     2.18e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.18e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
'''

# model 예측치
y_pred = model.fittedvalues
print(y_pred)
x = score[['iq','academy']]
print(x.shape)  # (150, 2)
# a의 shape는 (2, 1)이 되어야 함
#         coef of iq,      academy
a = np.array([[[0.376966],[2.992800]]])

matmul = np.dot(x, a)
b = 25.229141  # 절편
y_pred = matmul + b
y_pred = y_pred.reshape(150)  # 2차원(150,1) -> 1차원(150,)
print(y_pred)  # model.fittedvalues와 결과 동일(type: Series & ndarray)

y_true = score['score']
df = pd.DataFrame({'y_true':y_true, 'y_pred':y_pred, 'error':abs(y_pred-y_true)})
print(df)

print(df.corr())  # df['y_true'].corr(df['y_pred'])
'''       y_true    y_pred : error 제외
y_true  1.000000  0.972779 <- 1에 가까움
y_pred  0.972779  1.000000
'''
