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

# object 생성
kkma = Kkma()

# 1. text file 읽기
file = open('../data/text_data.txt', mode='r', encoding='UTF-8')
docs = file.read()
print(docs)

# 2. docs -> sentence
ex_sent = kkma.sentences(docs)
print(ex_sent)

# docs -> nouns
ex_nouns = kkma.nouns(docs)
print(ex_nouns)

# ex_nouns에는 중복이 사라지기 때문에 wordcloud로 적합하지 않음

# 2. 명사 추출 : Kkma
nouns_word = []

for sent in ex_sent:
    for noun in kkma.nouns(sent):
        nouns_word.append(noun)
print(nouns_word)

# 3. 전처리 : 단어 길이 제한(1음절 제거), 숫자 제외
nouns_count = {}
for noun in nouns_word:
    if len(noun) > 1 and match('^\D', noun):
        nouns_count[noun] = nouns_count.get(noun, 0) + 1
print(nouns_count)

# 4. Word Cloud
# 1) top5 word
word_count = Counter(nouns_count)
top5_word = word_count.most_common(5)
print(top5_word)

# 2) word cloud
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',  # 한글인 경우 이 옵션은 필수
               width=500, height=400,
               max_words=100,
               min_font_size=4,
               background_color='white')
wc_result = wc.generate_from_frequencies(dict(top5_word))
plt.imshow(wc_result)
plt.axis('off')  # 축(눈금선) 없애기
plt.show()
