"""
교차검정(CrossValidation)
"""

from sklearn.datasets import load_digits # dataset
from sklearn.ensemble import RandomForestClassifier # model
from sklearn.model_selection import train_test_split, cross_validate # split
from sklearn.metrics import accuracy_score

# 1. dataset load
digit = load_digits()

X = digit.data
y = digit.target

# 2. model
rf = RandomForestClassifier()
model = rf.fit(X, y)

pred = model.predict(X)

pred2 = model.predict_proba(X) # 확률 예측치
# [1.  , 0.  , 0.  , ..., 0.  , 0.  , 0.  ]

# 확률 -> index(10진수)
pred2_dit = pred2.argmax(axis = 1)
# array([0, 1, 2, ..., 8, 9, 8],

acc = accuracy_score(y, pred)
# 0.9444444444444444

acc = accuracy_score(y, pred2_dit)
acc


# 3. CrossValidation
score = cross_validate(model, X, y, scoring='accuracy', cv=5)
score

test_score = score['test_score']

# 산술평균
test_score.mean() # 0.9393608789848346
