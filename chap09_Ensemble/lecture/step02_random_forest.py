"""
Random Forest Ensemble Model
"""
import numpy as np
from sklearn.ensemble import RandomForestClassifier  # 범주형 랜덤 포레스트
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt


# 1. dataset load
wine = load_wine()
print(wine.feature_names)  # X 변수명
print(wine.target_names)  # y 범주 이름

X = wine.data
y = wine.target

# 2. RF model
rf = RandomForestClassifier()
"""
* n_estimators : integer, optional (default=100) : 트리 수
  criterion : string, optional (default="gini") or "Entropy": 중요변수 선정
* max_depth : integer or None, optional (default=None) : 트리 깊이
  min_samples_split : int, float, optional (default=2) : 노드 분할에 필요한 최소 샘플 수
  min_samples_leaf : int, float, optional (default=1) : 단노드 분할 최소 샘플 수
  max_features : int, float, string or None, optional (default="auto") : 최대 X 변수 사용 수
  n_jobs : int or None, optional (default=None) : CPU 수
  random_state : int, RandomState instance or None, optional (default=None) : 랜덤 seed 값 설정
"""
idx = np.random.choice(a=X.shape[0], size=int(X.shape[0] * 0.7), replace=False)
X_train = X[idx]  # X[idx, :]
y_train = y[idx]

idx2 = [i for i in range(int(X.shape[0] * 0.7)) if i not in idx]
X_test = X[idx2]
y_test = y[idx2]
print(X_train)
print(X_test)

model = rf.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(model.feature_importances_)

# 중요변수 시각화
x_size = X.shape[1]
plt.barh(range(x_size), model.feature_importances_)# (y, x)
plt.yticks(range(x_size), wine.feature_names)
plt.xlabel('importance')
plt.show()