"""
Support Vector Machine
- 선형 SVM, 비선형 SVM
- hyper parameter(kernel, C, gamma)
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

# 1 dataset load
iris = pd.read_csv('../../../data/iris.csv')

# 2. x, y 변수 선택
cols = list(iris.columns)

x_cols = cols[:4]
y_col = cols[-1]

# 3. train(60)/test(40) split
train, test = train_test_split(iris, test_size=0.4, random_state=123)

# 4. SVM model 생성
svc = SVC(gamma='auto')  # default = C=1.0, kernel='rbf'(비선형 모델)

model = svc.fit(train[x_cols], train[y_col])

y_pred = model.predict(X=test[x_cols])
y_true = test[y_col]

acc = accuracy_score(y_true, y_pred)
print(acc)

svc2 = SVC(kernel='linear')  # 선형 모델
model2 = svc2.fit(train[x_cols], train[y_col])
y_pred2 = model2.predict(X=test[x_cols])
acc = accuracy_score(y_true, y_pred2)
print(acc)


###############
# Grid Search #
###############

# Cost, gamma
params = [0.001, 0.01, 0.1, 1, 10, 100]
kernel = ['linear', 'rbf']
best_score = 0
best_parameter = {}

for k in kernel:
    print('> k =', k)
    for gamma in params:
        print('>> gamma =', gamma)
        for c in params:
            print('>>> c =', c)
            svc = SVC(kernel=k, gamma=gamma, C=c)  # 선형 모델
            model = svc.fit(train[x_cols], train[y_col])
            y_pred = model.predict(X=test[x_cols])
            acc = accuracy_score(y_true, y_pred)
            if acc > best_score:
                best_score = acc
                best_parameter = {'kernel': k, 'gamma': gamma, 'C': c}
                print('best score = ', best_score)
print(best_parameter)
print(best_score)
