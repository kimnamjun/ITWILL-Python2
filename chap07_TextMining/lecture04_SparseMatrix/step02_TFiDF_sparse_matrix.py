"""
1. csv file read
2. texts, target -> 전처리
3. max features
4. sparse matrix
"""
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 1. csv file read
spam_data = pd.read_csv('../data/temp_spam_data.csv', encoding='UTF-8', header=None)
print(spam_data)

target = spam_data[0]
texts = spam_data[1]

# 2. texts, target 전처리

# 1) target 전처리
target = [1 if t == 'spam' else 0 for t in target]

# 2) texts 전처리
import string # text 전처리
def text_prepro(texts):
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts

texts_re = text_prepro(texts)
print(texts_re)

# 3. max features
'''
사용할 x변수의 개수(열의 차수)
'''
tfidf_fit = TfidfVectorizer().fit(texts_re)
vocs = tfidf_fit.vocabulary_
print(vocs)
# max_features = len(vocs)
max_features = 10  # 이렇게 쓰면 단어 중 10개 단어만 이용

# 4. sparse matrix
sparse_mat = TfidfVectorizer().fit_transform(texts_re)  # max_featrues 설정 가능
sparse_mat2 = TfidfVectorizer(max_features=max_features).fit_transform(texts_re)  # max_featrues 설정 가능

sparse_mat_arr = sparse_mat2.toarray()
print(sparse_mat_arr)