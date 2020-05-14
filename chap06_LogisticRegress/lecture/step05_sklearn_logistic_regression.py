"""
sklearn 로지스틱 회귀모델
- y변수가 범주형인 경우
"""
from sklearn.datasets import load_breast_cancer, load_iris, load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
####################
# 1. 이항분류 모델 #
####################

# 1. dataset load
breast = load_breast_cancer()
X = breast.data
y = breast.target


# 2. model 생성
lr = LogisticRegression(random_state=123)
model = lr.fit(X=X, y=y)
# help(LogisticRegression)
"""
random_state=None  : 난수 seed값 지정
solver='lbfgs'     : 알고리즘
max_iter=100       : 반복학습 횟수
multi_class='auto' : 다항분류, class type 자동 지정

적용 예)
일반 데이터, 이항분류 : default
일반 데이터, 다항분류 : multi_class='multinomial'
빅데이터,    이항분류 : solver='sag' or 'saga'
빅데이터,    다항분류 : solver='sag' or 'saga', multi_class='multinomial'
"""


# 3. model 평가
# 1) 분류 정확도 구하기1 (기존)
y_pred = model.predict(X)
acc = accuracy_score(y, y_pred)
print('accuracy =', acc)

# 2) 분류 정확도 구하기2 (간편)
acc = model.score(X, y)

# 3) 분류 정확도 구하기3 (수동1)
con_mat = confusion_matrix(y, y_pred)
# print(con_mat)  # type : numpy.ndarray
'''
           pred
         0   1
true 0 [193  19]
     1 [ 11 346]
'''
acc = ((con_mat[0,0] + con_mat[1,1]) / con_mat.sum())

# 4) 분류 정확도 구하기4 (수동2)
tab = pd.crosstab(y, y_pred, rownames=['관측치'], colnames=['예측치'])
acc = (tab.loc[0,0]+tab.loc[1,1]) / len(y)


####################
# 2. 다항분류 모델 #
####################

# 1. dataset load
iris = load_iris()
iris.target_names  # array(['setosa', 'versicolor', 'virginica'], dtype='<U10')
X, y = load_iris(return_X_y=True)

# 2. model
lr = LogisticRegression(random_state=123, multi_class='multinomial')
# multi_class='multinomial' : softmax 활용함수 이용 -> 다항분류
'''
sigmoid_function : 0 ~ 1 확률값 -> cutoff = 0.5 -> 이항분류
softmax function : 0 ~ 1 확률값 -> 전체합 = 1   -> 다항분류
'''
model = lr.fit(X,y)
y_pred = model.predict(X)       # class
y_prob = model.predict_proba(X) # 확률값
print(y_pred)
print(y_prob)

# 3. model 평가
acc = accuracy_score(y, y_pred)  # 0.9733

con_mat = confusion_matrix(y, y_pred)
# [[50  0  0]
#  [ 0 47  3]
#  [ 0  1 49]]

plt.figure(figsize=(6,6))
sn.heatmap(con_mat, annot=True, fmt=".3f", linewidths=.5, square=True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
all_sample_title = f'Accuracy Score: {format(acc)}'
plt.title(all_sample_title, size=18)
plt.show()


########################
# digits : multi class #
########################

digits = load_digits()
digits.target_names  # [0 1 2 3 4 5 6 7 8 9]

X = digits.data  # (1797, 64)
y = digits.target

img_train, img_test, label_train, label_test = train_test_split(X, y, random_state=123, test_size=0.25)
img2d_train = img_train.reshape(-1, 8, 8) # (전체이미지, 세로, 가로)
# plt.imshow(img2d_train[0])
# plt.title(label_test[0])
# plt.show()

lr = LogisticRegression(random_state=123, solver='lbfgs', multi_class='multinomial')
model = lr.fit(img_train, label_train)

label_pred = model.predict(img_test)
acc = accuracy_score(label_test, label_pred)  # 0.9644

# con_mat = confusion_matrix(label_test, label_pred)
# print(con_mat)
tab = pd.crosstab(label_test, label_pred, rownames=['관측치'], colnames=['예측치'])
print(tab)

result = label_test == label_pred
false_img = img_test[result == False]

N = 4
M = 10
fig = plt.figure(figsize=(10,5))
plt.subplots_adjust(top=1, bottom=0, hspace=0, wspace=0.05)
help(plt.imshow)
for i in range(N):
    for j in range(M):
        k = i * M + j
        ax = fig.add_subplot(N, M, k+1)
        ax.imshow(digits.images[k], cmap=plt.cm.bone, interpolation='none')
        ax.grid(False)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        plt.title(digits.target_names[digits.target[k]])
plt.tight_layout()
plt.show()

# for img in false_img:
#     img2d = img.reshape(8,8)
#     plt.imshow(img2d)
#     plt.show()
#
# plt.figure(figsize=(6,6))
# sn.heatmap(tab, annot=True, fmt=".3f", linewidths=.5, square=True)
# plt.ylabel('Actual label')
# plt.xlabel('Predicted label')
# all_sample_title = f'Accuracy Score: {acc}'
# plt.title(all_sample_title, size=18)
# plt.show()
