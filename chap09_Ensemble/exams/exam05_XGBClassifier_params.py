# -*- coding: utf-8 -*-
"""
문) wine dataset을 이용하여 다음과 같이 다항분류 모델을 생성하시오. 
 <조건1> tree model 200개 학습
 <조건2> tree model 학습과정에서 조기 종료 100회 지정
 <조건3> model의 분류정확도와 리포트 출력   
"""
from xgboost import XGBClassifier # model
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine # 다항분류
from sklearn.metrics import accuracy_score, classification_report


#################################
## 1. XGBoost Hyper Parameter
#################################

# 1. dataset load
X, y = load_wine(return_X_y=True)

# 2. train/test 생성 
x_train, x_test, y_train, y_test = train_test_split(X, y)

# 3. model 객체 생성
xgb = XGBClassifier(n_estimators=200)

# 4. model 학습 조기종료 
eval_set = [(x_test, y_test)]
model_early = xgb.fit(x_train, y_train, eval_set=eval_set, eval_metric='merror', early_stopping_rounds=100, verbose=True)

# 5. model 평가 
score = model_early.score(x_test, y_test)
print(score)  # 0.9778
