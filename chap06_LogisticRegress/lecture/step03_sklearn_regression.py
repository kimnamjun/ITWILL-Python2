"""
sklearn 관련 Linear Regression
"""
from sklearn.linear_model import LinearRegression         # model object
from sklearn.model_selection import train_test_split      # train/test split
from sklearn.metrics import mean_squared_error, r2_score  # model 평가
from sklearn.datasets import load_diabetes                # 실습용 dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

############
# diabetes #
############
# 단순선형회귀 : x(1) -> y

# 1. dataset load
X, y = load_diabetes(return_X_y=True)

# x(bmi : 비만도 지수) -> y
x_bmi = X[:, 2]  # x 변수로 설정할 컬럼 선택
x_bmi = x_bmi.reshape(442, 1)  # x 변수는 2차원이어야 함

# 3. model 생성 : object -> training -> model
obj = LinearRegression()   # 생성자
model = obj.fit(x_bmi, y)  # model 생성

y_pred = model.predict(x_bmi)  # 예측치

# 4. model 평가 : MSE(정규화 된 경우), r2_score(비정규화 된 경우에도)
MSE = mean_squared_error(y, y_pred)
score = r2_score(y, y_pred)
print(f"MSE     : {MSE}")
print(f"r2score : {score}")

# 5. dataset split (70 : 30)
x_train, x_test, y_train, y_test = train_test_split(x_bmi, y, test_size=0.3)
model = obj.fit(x_train, y_train)

y_pred = model.predict(x_test)
MSE = mean_squared_error(y_test, y_pred)
score = r2_score(y_test, y_pred)
print(f"MSE     : {MSE}")
print(f"r2score : {score}")
print(y_test[:10])
print(y_pred[:10])

df = pd.DataFrame({'y_true': y_test, 'y_pred': y_pred})
cor = df['y_true'].corr(df['y_pred'])
print(cor)

plt.plot(x_test, y_test, 'ro')  # red  'o'
plt.plot(x_test, y_pred, 'b-')  # blue '-'
plt.show()

print('\n'+'-'*80+'\n')
############
# iris.csv #
############
# 다중회귀모델 x(2~4) -> y(1)
iris = pd.read_csv('../../../data/iris.csv')
x = iris.iloc[:, 1:4]
y = iris.iloc[:, 0]

# 핵심 코드                                                              random seed
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)  # size_default : 0.25
model = LinearRegression().fit(x_train, y_train)
y_pred = model.predict(x_test)

df = pd.DataFrame({'y_true': y_test, 'y_pred': y_pred})
df = df.sort_index()
print(df)
MSE = mean_squared_error(y_test, y_pred)
score = r2_score(y_test, y_pred)
print(f"MSE     : {MSE}")
print(f"r2score : {score}")
print(y_pred)
print(y_test)

fig = plt.figure(figsize=(10,5))
chart = fig.subplots()
chart.plot(list(y_test), color='b', label='real values')
chart.plot(y_pred, color='r', label='fitted values')
plt.legend()
plt.show()