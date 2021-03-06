﻿'''
TextMining 최종문제  

문) movies.dat 파일의 자료를 이용하여 다음과 같이 단계별로 단어의 빈도수를 구하고,
    단어 구름으로 시각화하시오.
'''

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

# [단계1] 영화 dataset 가져오기  
name = ['movie_id', 'title', 'genres']
# movies = pd.read_csv('workspace/chap07_TextMining/data/movies.dat', sep='::', header=None, names=name)
movies = pd.read_csv('../data/movies.dat', sep='::', header=None, names=name)
# print(movies.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3883 entries, 0 to 3882
Data columns (total 3 columns):
movie_id    3883 non-null int64 -> 각 영화 구분자 
title       3883 non-null object -> 영화 제목 
genres      3883 non-null object -> 영화 장르 : 한 개 이상의 장르(genres) 구성됨  
'''
# print(movies.head())
'''
   movie_id                               title                        genres
0         1                    Toy Story (1995)   Animation|Children's|Comedy
1         2                      Jumanji (1995)  Adventure|Children's|Fantasy
2         3             Grumpier Old Men (1995)                Comedy|Romance
3         4            Waiting to Exhale (1995)                  Comedy|Drama
4         5  Father of the Bride Part II (1995)                        Comedy
'''
# print('전체 영화수 : ', len(movies)) # 전체 영화수 :  3883


# [단계2] zero 행렬 만들기[행수 : 전체 영화수, 열수 : 중복되지 않은 장르 수]  
# 힌트 : 중복되지 않은 장르 수 구하기
# 각 영화의 장르는 구분자(|)에 의해서 1개 이상의 장르로 구성된 문자열이다.
# 따라서 중복되지 않은 장르 수를 구하기 위해서 구분자(|)를 기준으로 split하여 
# 토큰을 생성한 후 중복을 제거한다.
genres = set()
for movie in movies.values:
    gen = movie[2].split('|')
    for g in gen:
        genres.add(g)
zeros = np.zeros([len(movies), len(genres)])


# [단계3] zero 행렬 -> DataFrame 변환(열 제목 = 장르명) 
# 설명 : zero 행렬을 대상으로 열 이름에 장르명을 지정하여 DataFrame을 생성한다.
df = pd.DataFrame(zeros)
df.columns = sorted(genres)
df.index = movies.loc[:,'title']
# print(df)


# [단계4] 희소행렬(Sparse matrix) 생성 
# 설명 : 각 영화별로 해당 장르에 해당하는 교차 셀에 0 -> 1 교체하여 희소행렬을 만든다.
# 힌트 : index와 내용을 반환하는 enumerate() 함수 이용
for index, movie in enumerate(movies.values):
    for g in movie[2].split('|'):
        df.loc[movie[1], g] = 1.0
print(df)

texts = list()
for movie in movies.values:
    texts.append(' '.join(movie[2].split('|')))
sparse_mat = TfidfVectorizer().fit_transform(texts)
# print(sparse_mat)

tfidf_fit = TfidfVectorizer().fit(texts)
vocs = tfidf_fit.vocabulary_
swap_vocs = {value: key for key, value in vocs.items()}


# [단계5] 단어문서 행렬(TDM) 만들기
# 설명 : 희소행렬(Sparse matrix)에 전치행렬을 적용하여 장르명과 영화 축을 교체한다.
# 힌트 : 전치행렬 -> 형식) 데이터프레임객체.T
sparse_mat = sparse_mat.T
# print(sparse_mat)


# [단계6] 장르 빈도수(word count)
# 설명 : 단어문서 행렬(TDM)를 대상으로 행 단위 합계를 계산하여 장르별 출현빈도수를 계산한다.
# 힌트 : dict() 이용하여 장르명과 빈도수를 key : value 형식으로 만든다.
word_count = dict()
total = sparse_mat.sum(axis=1)
print(total)
for idx, val in enumerate(total):
    word_count[swap_vocs[idx]] = val[0, 0]
print(word_count)


# [단계7] 단어 구름 시각화
# 설명 : 장르 빈도수를 Counter 객체를 생성하고, WordCloud 클래스를 이용하여 단어 구름으로 시각화한다.
word_count = Counter(word_count)
print(word_count)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=500, height=400,
               min_font_size=4, background_color='white')
wc_result = wc.generate_from_frequencies(dict(word_count))
plt.imshow(wc_result)
plt.axis('off')
plt.show()