"""
TFiDF 단어 생성기 : TfidfVectorizer
  1. 단어 생성기[word tokenizer] : 문장(sentences) -> 단어(word) 생성
  2. 단어 사전[word dictionary] : (word, 고유수치)
  3. 희소행렬[sparse matrix] : 단어 출현 비율에 의해서 가중치 적용[type-TF, TFiDF]
    1] TF : 가중치 설정 - 단어 출현 빈도수
    2] TFiDF : 가중치 설정 - 단어 출현 빈도수 x 문서 출현빈도수의 역수
    - tf-idf(d,t) = tf(d,t) x idf(t) [d(document), t(term)]
    - tf(d,t) : term frequency - 특정 단어 빈도수
    - idf(t) : inverse document frequency - 특정 단어가 들어 있는 문서 출현빈도수의 역수
       -> TFiDF = tf(d, t) x log( n/df(t) ) : 문서 출현빈도수의 역수(n/df(t))
"""
from sklearn.feature_extraction.text import TfidfVectorizer

sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]

# 1. 단어 생성기[word tokenizer]
tfidf = TfidfVectorizer()

# 2. 문장 -> 단어 생성
tfidf_fit = tfidf.fit(sentences)  # 단어들
print(tfidf_fit)  # dict{'word1':고유숫자, 'word2':고유숫자, ...}

# 단어 사전 : 고유숫자(영문 오름차순 결정)
vocs = tfidf_fit.vocabulary_

# 3. 희소행렬(sparse matrix)
sparse_mat = tfidf.fit_transform(sentences)  # 희소행렬 생성
print(sparse_mat)  # type : scipy.sparse.csr.csr_matrix

# scipy -> numpy
sparse_mat_arr = sparse_mat.toarray()
print(sparse_mat_arr)