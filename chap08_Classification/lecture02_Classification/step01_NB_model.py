"""
Naive Bayes 모델
GaussianNB : X 변수가 실수형이고, 정규분포 형태
MultinomialNB : 희소행렬과 같은 고차원 데이터를 이용하여 다항분류
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from scipy import stats  # 정규분포 검정

##############
# GaussianNB #
##############

# 1 dataset load
iris = pd.read_csv('../../../data/iris.csv')

stats.shapiro(iris["Sepal.Width"])  # 정규성 검정
# (0.9849170446395874, 0.10113201290369034)


# 2. x, y 변수 선택
cols = list(iris.columns)

x_cols = cols[:4]
y_col = cols[-1]

# 3. train/test split
train, test = train_test_split(iris, test_size=0.3, random_state=123)

# 4. NB model
nb = GaussianNB()
model = nb.fit(X=train[x_cols], y=train[y_col])

# 5. model 평가
y_pred = model.predict(X=test[x_cols])
y_true = test[y_col]

acc = accuracy_score(y_true, y_pred)
con_mat = confusion_matrix(y_true, y_pred)
f1_score = f1_score(y_true, y_pred, average='micro')  # average='micro'는 다항분류 일 때
# print(acc)
# print(con_mat)
# print(f1_score)


#################
# MultinomialNB #
#################
# 1. dataset load
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
newsgroups = fetch_20newsgroups(subset='all')  # subset='train', 'test'
# Downloading 20news dataset.

print(newsgroups.DESCR)
"""
X 변수 : news 기사 내용(text 자료)
y 변수 : 해당 news의 group(20개)
"""
newsgroups.target_names

cats = newsgroups.target_names[:4]
cats

# 2. text -> sparse matrix : fetch_20newsgroups(subset='train)
news_train = fetch_20newsgroups(subset='train', categories=cats)
news_train.data

# sparse matrix
tfidf = TfidfVectorizer()
sparse_mat = tfidf.fit_transform(news_train.data)
sparse_mat.shape

# 3. model
nb = MultinomialNB()
model = nb.fit(sparse_mat, news_train.target)

# 4. model 평가 : fetch_20newsgroups(subset='test)
news_test = fetch_20newsgroups(subset='test', categories=cats)

sparse_test = tfidf.transform(news_test.data)
# 위의 tfidf와 같은 객체를 사용하되
# 위에서는 fit_transform이었다면
# 여기서는 trainsform임

y_pred = model.predict(X=sparse_test)
y_true = news_test.target

acc = accuracy_score(y_true, y_pred)
con_mat = confusion_matrix(y_true, y_pred)