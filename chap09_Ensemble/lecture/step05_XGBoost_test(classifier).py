"""
XGBoost model

Anaconda Prompt
> pip install xgboost
"""
# import test
from xgboost import XGBClassifier, XGBRegressor
from xgboost import plot_importance
from sklearn.datasets import make_blobs  # 클러스터 데이터셋 생성
from sklearn.metrics import accuracy_score, classification_report  # 모델 평가 도구
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 1. dataset load
X, y = make_blobs(n_samples=2000, n_features=4, centers=2, cluster_std=2.5, random_state=123)
"""
n_samples : 데이터셋 크기
n_features : X변수
centers : Y변수 범주 개수
cluster_std : 클러스터 표준편차(클수록 오분류 커짐)
"""
plt.scatter(x=X[:,0], y=X[:,1], s=100, c=y, marker='o')
plt.show()

# 2. train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 3. model 생성
xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
model  # objective='binary:logistic'

# 4. model 평가
y_pred = model.predict(x_test)
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 5. 중요변수 시각화
fscore = model.get_booster().get_fscore()
print(fscore)
plot_importance(booster=model)
plt.show()

# ------------------------------------------------------------------------ #
# 1. make_blobs에서 centers = 3 이상일 경우(이항분류가 아닌 다항분류일 때)
# 3. model 생성에서 objective='multi:softmax'가 됨
# ------------------------------------------------------------------------ #
