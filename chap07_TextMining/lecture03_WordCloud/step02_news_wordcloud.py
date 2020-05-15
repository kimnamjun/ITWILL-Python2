"""
https://www.lfd.uci.edu/~gohlke/pythonlibs/
wordcloud 찾아서 설치(방법은 lecture02의 jpype와 동일)

1. text file 읽기
2. 명사 추출 : Kkma
3. 전처리 : 단어 길이 제한, 숫자 제외
4. WordCloud
"""
from konlpy.tag import Kkma
from wordcloud import WordCloud
from re import match
from collections import Counter
import matplotlib.pyplot as plt
import pickle

kkma = Kkma()  # 생성자

with open('../data/news_data.pickle', mode='rb') as file:
    news_data = pickle.load(file)  # 11600개의 기사 제목 list
print(news_data)

ex_sent = [kkma.sentences(sent)[0] for sent in news_data]  # 문장 추출

nouns_word = []

for sent in ex_sent:
    for noun in kkma.nouns(sent):
        nouns_word.append(noun)
print(nouns_word)

nouns_count = {}
for noun in nouns_word:
    if len(noun) > 1 and match('^\D', noun):
        nouns_count[noun] = nouns_count.get(noun, 0) + 1

# 진자 -> 확진자
nouns_count['확진자'] = nouns_count.get('진자', 0)
del nouns_count['진자']

print(nouns_count)

word_count = Counter(nouns_count)
top50_word = word_count.most_common(50)
print(top50_word)

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', width=500, height=400, max_words=100,
               min_font_size=4, background_color='white')
wc_result = wc.generate_from_frequencies(dict(top50_word))
plt.imshow(wc_result)
plt.axis('off')
plt.show()
