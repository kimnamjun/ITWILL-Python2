"""
news crawling data -> word vector
문장 -> 단어 벡터 -> 희소행렬
ex) '직업은 데이터 분석가 입니다.' -> '직업 데이터 분석가'
"""

from konlpy.tag import Kkma
from wordcloud import WordCloud
from re import match
from collections import Counter
import matplotlib.pyplot as plt
import pickle

kkma = Kkma()  # 생성자

with open('../data/news_data.pickle', mode='rb') as file:  # 컴파일용
# with open('workspace/chap07_TextMining/data/news_data.pickle', mode='rb') as file:  # 인터프리터용
    news_data = pickle.load(file)  # 11600개의 기사 제목 list
print(news_data)

ex_sent = [kkma.sentences(sent)[0] for sent in news_data]  # 문장 추출

# --------------------------------------------------------------- 위는 전과 동일

# sentence -> word vector
sentence_nouns = []  # 단어 벡터 저장

for sent in ex_sent:
    word_vec = ""
    for noun in kkma.nouns(sent):  # 문장에서 명서 추출
        if len(noun) > 1 and match('^\D', noun):
            word_vec += noun + ' '  # 문장 안의 명사를 공백으로 구분하여 리스트에 append
    sentence_nouns.append(word_vec)

len(sentence_nouns)
sentence_nouns

# file save
import pickle
with open('../data/sentence_nouns.pickle', mode='wb') as file:  # 컴파일용
# with open('workspace/chap07_TextMining/data/sentence_nouns.pickle', mode='wb') as file:
    pickle.dump(sentence_nouns, file)

# file load
with open('../data/sentence_nouns.pickle', mode='rb') as file:  # 컴파일용
# with open('workspace/chap07_TextMining/data/sentence_nouns.pickle', mode='rb') as file:
    word_vector = pickle.load(file)
print(word_vector)