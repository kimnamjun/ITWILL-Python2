"""
문) california 주택가격을 대상으로 다음과 같은 단계별로 선형회귀분석을 수행하시오.
"""

# california 주택가격 데이터셋 
'''
캘리포니아 주택 가격 데이터(회귀 분석용 예제 데이터)

•타겟 변수
1990년 캘리포니아의 각 행정 구역 내 주택 가격의 중앙값

•특징 변수(8) 
MedInc : 행정 구역 내 소득의 중앙값
HouseAge : 행정 구역 내 주택 연식의 중앙값
AveRooms : 평균 방 갯수
AveBedrms : 평균 침실 갯수
Population : 행정 구역 내 인구 수
AveOccup : 평균 자가 비율
Latitude : 해당 행정 구역의 위도
Longitude : 해당 행정 구역의 경도
'''

from sklearn.datasets import fetch_california_housing # dataset load
import pandas as pd # DataFrame 생성 
from sklearn.linear_model import LinearRegression  # model
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import mean_squared_error, r2_score # model 평가
import matplotlib.pyplot as plt
import numpy as np

# 캘리포니아 주택 가격 dataset load 
california = fetch_california_housing()
print(california.DESCR)

# 단계1 : 특징변수와 타켓변수(MEDV)를 이용하여 DataFrame 생성하기
cal_df = pd.DataFrame(california.data, columns=california.feature_names)
cal_df["MEDV"] = california.target
print(cal_df)

# 단계2 : 타켓변수와 가장 상관관계가 높은 특징변수 확인하기
print(cal_df.corr())  # MedInc

# 단계3 : california 데이터셋을 대상으로 1만개 샘플링하여 서브셋 생성하기
cal_df2 = cal_df.sample(n=10000, random_state=123)

# 단계4 : 75%(train) vs 25(test) 비율 데이터셋 split 
x_train, x_test, y_train, y_test = train_test_split(cal_df2['MedInc'], cal_df2['MEDV'], random_state=123)
x_train = x_train.values.reshape(-1, 1)
x_test = x_test.values.reshape(-1, 1)

# 단계5 : 선형회귀모델 생성
model = LinearRegression().fit(x_train, y_train)

# 단계6 : 모델 검정(evaluation)  : 예측력 검정, 과적합(overfitting) 확인  
y_pred1 = model.predict(x_test)
print(r2_score(y_test, y_pred1))  # 0.4761
print(model.score(x_test, y_test))  # 상동

y_pred2 = model.predict(x_train)
print(r2_score(y_train, y_pred2))  # 0.4810
print(model.score(x_train, y_train))  # 상동
# train과 test 비슷한 적합도, 과적합 없음

# 단계7 : 모델 평가(test)

# 조건1) 단계3의 서브셋 대상으로 30% 샘플링 자료 이용
# 조건2) 평가방법 : MSE, r2_score
test_idx = np.random.choice(a=len(cal_df2), size = int(len(cal_df2)*0.3), replace=False)
test_data = cal_df.iloc[test_idx,:]
y_pred = model.predict(test_data.iloc[:,8].values.reshape(-1,1))
y_true = test_data.iloc[:,8]

MSE = mean_squared_error(y_true, y_pred)  # 0.9851
r2score = r2_score(y_true, y_pred)        # 0.9858

# 단계8 : 예측치 100개 vs 정답 100개 비교 시각화 














