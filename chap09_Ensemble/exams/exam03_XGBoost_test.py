'''
 문) iris dataset을 이용하여 다음과 같은 단계로 XGBoost model을 생성하시오.
'''

import pandas as pd # file read
from xgboost import XGBClassifier # model 생성 
from xgboost import plot_importance # 중요변수 시각화  
import matplotlib.pyplot as plt # 중요변수 시각화 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report # model 평가

# 단계1 : data set load 
iris = pd.read_csv("../../../data/iris.csv")

# 변수명 추출 
cols=list(iris.columns)
col_x=cols[:4] # x변수명 
col_y=cols[-1] # y변수명 

# 단계2 : 훈련/검정 데이터셋 생성
train_set, test_set = train_test_split(iris, test_size=0.25)

# 단계3 : model 생성 : train data 이용
model = XGBClassifier().fit(train_set[col_x], train_set[col_y]) # 다항분류 objective='multi:softmax'

# 단계4 :예측치 생성 : test data 이용  
y_true = test_set[col_y]
y_pred = model.predict(test_set[col_x])
y_pred2 = model.predict_proba(test_set[col_x])
y_pred2_dit = y_pred2.argmax(axis=1)
print(y_pred2_dit)

# 단계5 : 중요변수 확인 & 시각화  
print(classification_report(y_true, y_pred))
plot_importance(booster=model)
plt.show()

# 단계6 : model 평가 : confusion matrix, accuracy, report
print('confusion matrix\n', confusion_matrix(y_true, y_pred))
print('\naccuracy score', accuracy_score(y_true, y_pred))
print(classification_report(y_true, y_pred))