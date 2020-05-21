"""
pipe line vs grid search
1. SVM model
2. Pipeline : model workflow : dataset 전처리 -> model -> test
3. Grid Search : model tuning
"""
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

# 1. SVM model
# 1) dataset load
X, y = load_breast_cancer(return_X_y=True)
# print(X.mean(axis=0))
# print(X.min())
# print(X.max())

# 2) X변수 정규화 : 전처리
X_nor = MinMaxScaler(feature_range=(0,1)).fit_transform(X)
# print(X_nor)
# print(X_nor.mean())
# print(X_nor.min())
# print(X_nor.max())

x_train, x_test, y_train, y_test = train_test_split(X_nor, y, test_size=0.3)

# 3) SVM model 생성
svc = SVC(gamma='auto')
model = svc.fit(x_train, y_train)

# 4) model 평가
score = model.score(x_test, y_test)  # 0.9766 (돌릴 때마다 다르며 편차 꽤 있음)
print(score)


# 2. Pipeline : model workflow
# 1) pipeline step : [(step1), (step2), ...]
#                 step1ㄱ                    step2ㄱ
pipe_svc = Pipeline([ ('scaler',MinMaxScaler()), ('svc',SVC(gamma='auto')) ])
#                       ㄴ임의 지정       ㄴ함수

# 2) pipeline model 생성
model = pipe_svc.fit(x_train, y_train)

# 3) pipeline model test
score = model.score(x_test, y_test)  # pipe 없이 할 때와 비슷


# 3. Grid Search : model tuning
# Pipeline -> Grid Search -> model tuning

# 1) params 설정
params = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]

# dict 형식 = {'object(객체명)__C(파라미터명)': params_range} : '_' 두 개임(임의 값이 아니라 형식인 듯)
params_grid = [{'svc__C': params,                     'svc__kernel': ['linear']},    # 선형
               {'svc__C': params, 'svc__gamma': params, 'svc__kernel': ['rbf'] }]  # 비선형

# 2. GridSearchCV 객체
gs = GridSearchCV(estimator=pipe_svc,  # pipeline 객체(?)
                  param_grid=params_grid,  # grid search parameter
                  scoring='accuracy',  # 평가 방법
                  cv=10,  # 교차검정
                  n_jobs=1)  # CPU 수
model = gs.fit(x_train, y_train)
acc = model.score(x_test, y_test)
#             0.9473684210526315 : 그리드 서치 전
print(acc)  # 0.9707602339181286 : 그리드 서치 후
print(model.best_params_)  # {'svc__C': 100.0, 'svc__gamma': 0.01, 'svc__kernel': 'rbf'}
