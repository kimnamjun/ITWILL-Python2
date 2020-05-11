'''
문1) score_iq.csv 데이터셋을 이용하여 단순선형회귀모델을 생성하시오.
   <조건1> y변수 : score, x변수 : academy      
   <조건2> 회귀모델 생성과 결과확인(회귀계수, 설명력, pvalue, 표준오차) 
   <조건3> 회귀선 적용 시각화 
   
문2) irsi.csv 데이터셋을 이용하여 다중선형회귀모델을 생성하시오.
   <조건1> 칼럼명에 포함된 '.' 을 '_'로 수정
   iris = pd.read_csv('../data/iris.csv')
   iris.columns = iris.columns.str.replace('.', '_')
   <조건2> y변수 : 1번째 칼럼, x변수 : 2~4번째 칼럼    
   <조건3> 회귀계수 확인 
   <조건4> 회귀모델 세부 결과 확인  : summary()함수 이용 
'''

from scipy import stats
import pandas as pd
import statsmodels.formula.api as sm
from statsmodels.formula.api import ols
from pylab import plot, legend, show

# 문1)
score_iq = pd.read_csv('../../../data/score_iq.csv')
X = score_iq['academy']
Y_true = score_iq['score']

model = stats.linregress(X, Y_true)
# slope=4.847829398324446
# intercept=68.23926884996192
# rvalue=0.8962646792534938
# pvalue=4.036716755167992e-54
# stderr=0.1971936807753301
Y_pred = X * model.slope + model.intercept

plot(X, Y_true, 'bo')   # 산점도
plot(X, Y_pred, 'r.-')  # 회귀선
legend(['x, y scatter', 'regress model line'])
show()

# 문2)
iris = pd.read_csv('../../../data/iris.csv')
iris.columns = iris.columns.str.replace('.','_')
cols = iris.columns

formula = f"{cols[0]} ~ {cols[1]} + {cols[2]} + {cols[3]}"
model = ols(formula, data=iris).fit()
print(model.summary())

"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           Sepal_Length   R-squared:                       0.859
Model:                            OLS   Adj. R-squared:                  0.856
Method:                 Least Squares   F-statistic:                     295.5
Date:                Mon, 11 May 2020   Prob (F-statistic):           8.59e-62
Time:                        15:44:18   Log-Likelihood:                -37.321
No. Observations:                 150   AIC:                             82.64
Df Residuals:                     146   BIC:                             94.69
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        1.8560      0.251      7.401      0.000       1.360       2.352
Sepal_Width      0.6508      0.067      9.765      0.000       0.519       0.783
Petal_Length     0.7091      0.057     12.502      0.000       0.597       0.821
Petal_Width     -0.5565      0.128     -4.363      0.000      -0.809      -0.304
==============================================================================
Omnibus:                        0.345   Durbin-Watson:                   2.060
Prob(Omnibus):                  0.842   Jarque-Bera (JB):                0.504
Skew:                           0.007   Prob(JB):                        0.777
Kurtosis:                       2.716   Cond. No.                         54.7
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""
y_pred = model.fittedvalues
y_true = iris['Sepal_Length']

plot(y_pred, 'r-')
plot(y_true, 'b-')
show()
