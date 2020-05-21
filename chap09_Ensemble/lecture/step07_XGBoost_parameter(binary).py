"""
1. XGBoost hyper parameter
2. model 학습 조기종료 : early stopping rounds
3. best hyper parameter : grid search
"""
from xgboost import XGBClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

# 1. XGBoost hyper parameter
X, y = load_breast_cancer(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
print(model)
"""
colsample_bylevel : 트리 모델 생성시 훈련셋의 샘플링 비율 (1 = 100%, 통상 0.6 ~ 1)
learning_rate : 학습률(0.01 ~ 0.1)
max_depth : 트리 깊이, 과적합 영향
min_child_weight : 자식 노드의 분할을 결정하는 최소 가중치 합
objective='binary:logistic' : 이항분류와 다항분류를 결정
"""

# 2. model 학습 조기종료 : early stopping rounds
xgb = XGBClassifier()
eval_set = [(x_test, y_test)]  # 평가셋
model_early = xgb.fit(X, y, eval_set=eval_set, eval_metric='error', early_stopping_rounds=50, verbose=True)
"""
X, y : 훈련셋
eval_set : 평가셋
eval_metric : 평가방법(이항분류: error, 다항분류: merror(multi error), 회귀: rmse)
early_stopping_rounds : 학습조기종료 : n번 더 해보고 값이 좋아지지 않으면 종료
verbose : 학습 -> 평가 출력 여부
"""

# Stopping. Best iteration:
# [15]	validation_0-error:0.00000
score = model_early.score(x_test, y_test)
print(score)

# 3. Best hyper parameter : Grid search
xgb = XGBClassifier()
params = {'colsample_bylevel': [0.6, 0.8, 1], 'learning_rate': [0.01, 0.1, 0.5],
          'max_depth': [3, 5, 7], 'min_child_weight': [1, 3, 5], 'n_estimators': [100, 300, 500]}
gs = GridSearchCV(estimator=xgb, param_grid=params, cv=5)

# 훈련셋 : x_train, y_train // 평가셋: (x_test, y_test)
model = gs.fit(x_train, y_train, eval_set=eval_set, eval_metric='error', verbose=True)

print(model.best_score_)  # 0.9749050632911394
print(model.best_params_)
# {'colsample_bylevel': 1, 'learning_rate': 0.1, 'max_depth': 5, 'min_child_weight': 3, 'n_estimators': 100}