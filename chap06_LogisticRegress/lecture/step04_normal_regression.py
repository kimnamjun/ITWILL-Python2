"""
data scaling(정규화, 표준화) : 이물질 제거
 - 특정 변수의 값에 따라서 model에 영향을 미치는 경우
 - 용도 : 특정 변수의 값에 따라서 model에 영향을 미치는 경우
      ex) 범죄율(-0.1~0.99), 주택가격(99~999)

 - 정규화 : 변수의 값을 일정한 범위로 조정(0~1, -1 ~ 1)
 - 표준화 : 평균과 표준편차 이용(mean 0, std 1)
            표준화 공식 z = (x - mu) / sd
"""
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# 1. dataset load
X, y = load_boston(return_X_y=True)

# 2. data scaling
'''
X : 정규화(0~1)
Y : 표준화(mean 0, std 1)
'''
X.max()   # 711.0
X.mean()  # 70.07396704469443
y.max()   # 50.0
y.mean()  # 22.532806324110677

# 정규화 함수
def normal(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))

# 표준화 함수
def zscore(y):
    return (y - y.mean()) / y.std()

x_nor = normal(X)  # X 변수 정규화
y_nor = zscore(y)  # Y 변수 표준화

# 3. dataset split
x_train, x_test, y_train, y_test = train_test_split(x_nor, y_nor, random_state=123)

# 4. model 생성
model = LinearRegression().fit(x_train, y_train)

# 5. model 평가
y_pred = model.predict(X=x_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('mse :', mse)  # 0.2934 (오류율)
print('r2  :', r2)   # 0.6862 (정확률)
