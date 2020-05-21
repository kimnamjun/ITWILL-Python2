"""
1. XGBoost hyper parameter
2. model 학습 조기종료 : early stopping rounds
3. best hyper parameter : grid search
"""
from xgboost import XGBClassifier
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report

# 1. XGBoost hyper parameter
X, y = make_blobs(n_samples=2000, n_features=4, centers=3, cluster_std=2.5, random_state=123)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
xgb = XGBClassifier(colsample_bylevel=1, learning_rate=0.3, max_depth=3, min_child_weight=1, n_estimators=200)
model = xgb.fit(x_train, y_train)

# 2. model 학습 조기종료 : early stopping rounds
xgb = XGBClassifier()
eval_set = [(x_test, y_test)]  # 평가셋
model_early = xgb.fit(X, y, eval_set=eval_set, eval_metric='merror', early_stopping_rounds=100, verbose=True)

score = model_early.score(x_test, y_test)
print(score)

# 3. Best hyper parameter : Grid search
xgb = XGBClassifier()
params = {'colsample_bylevel': [0.7, 0.9], 'learning_rate': [0.01, 0.1],
          'max_depth': [3, 5], 'min_child_weight': [1, 3], 'n_estimators': [100, 200]}
gs = GridSearchCV(estimator=xgb, param_grid=params, cv=5)

# 훈련셋 : x_train, y_train // 평가셋: (x_test, y_test)
model = gs.fit(x_train, y_train, eval_set=eval_set, eval_metric='merror', verbose=True)

print(model.best_score_)  # 0.9228571428571429
print(model.best_params_)
# {'colsample_bylevel': 0.7, 'learning_rate': 0.1, 'max_depth': 3, 'min_child_weight': 3, 'n_estimators': 100}

