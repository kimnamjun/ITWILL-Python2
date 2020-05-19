"""
비교) NB vs SVM : 희소행렬(고차원)
- 가중치 적용 : Tfidf(Term Frequency - Inverse  Document Frequency)
"""
from sklearn.naive_bayes import MultinomialNB  # NB model
from sklearn.svm import SVC                   # SVC model
import numpy as np  # npy file load : chap07/data/spam_data.npy
from sklearn.metrics import accuracy_score, confusion_matrix

# 1. dataset load
x_train, x_test, y_train, y_test = np.load('../../chap07_TextMining/data/spam_data.npy', allow_pickle=True)
# X 변수들은 data frame, Y 변수들은 list

y_train = np.array(y_train)
y_test = np.array(y_test)


# 2. NB model
nb_model = MultinomialNB().fit(X=x_train, y=y_train)
y_pred = nb_model.predict(X=x_test)
acc = accuracy_score(y_test, y_pred)
con_mat = confusion_matrix(y_test, y_pred)
print("NB model accuracy score :", round(acc, 4))  # 0.9803
print(con_mat)
# [[1441    1]
#  [  32  199]]

# 3. SVM model
svm = SVC(gamma='auto')
svm_model = svm.fit(X=x_train, y=y_train)
y_pred = svm_model.predict(X=x_test)
acc = accuracy_score(y_test, y_pred)
con_mat = confusion_matrix(y_test, y_pred)
print("SVC model(non-linear) accuracy score :", round(acc, 4))  # 0.8619
print(con_mat)
# [[1442    0]
#  [ 231    0]]

svm = SVC(kernel='linear', gamma='auto')
svm_model = svm.fit(X=x_train, y=y_train)
y_pred = svm_model.predict(X=x_test)
acc = accuracy_score(y_test, y_pred)
con_mat = confusion_matrix(y_test, y_pred)
print("SVC model(linear) accuracy score :", round(acc, 4))  # 0.9839
print(con_mat)
# [[1437    5]
#  [  22  209]]