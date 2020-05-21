import matplotlib.pyplot as plt
from xgboost import XGBClassifier, XGBRegressor, plot_importance
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. dataset load
boston = load_boston()
X, y = load_boston(return_X_y=True)

x_names = boston.feature_names
# ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']

# 2. split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 3. model
xgb = XGBRegressor()
model = xgb.fit(x_train, y_train)

# 4. 중요변수 시각화
fscore = model.get_booster().get_fscore()
print(fscore)
print(x_names[int(str(max(fscore, key=lambda x: fscore[x]))[1:])])

plot_importance(model)
plt.show()

# 5. model 평가
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
score = r2_score(y_test, y_pred)

print('mse :', mse)
print('score :', score)