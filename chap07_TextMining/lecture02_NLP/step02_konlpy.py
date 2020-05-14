"""
anaconda prompt에서 'pip install konlpy'
위 명령어 실행하여 konlpy 설치(다운로드 필요없음)
특이사항 : BeautifulSoap 다운그레이드
    uninstalled beautifulsoup4-4.8.2
    installed beautifulsoup4-4.6.0 konlpy-0.5.2 tweepy-3.8.0

kolnpy : 한글 형태소 분석을 제공하는 패키지
"""
import konlpy
from konlpy.tag import Kkma

kkma = Kkma()  # 생성자
para = "나는 홍길동 입니다. 나이는 23세 입니다. 대한민국 만세 입니다."

# 문단 -> 문장
ex_sent = kkma.sentences(para)
print(ex_sent)

# 문장 -> 단어(명사)
ex_nouns = kkma.nouns(para)
print(ex_nouns)

# 문단 -> 품사(형태소)
ex_pos = kkma.pos(para)
print(ex_pos)

nouns = []  # 명사 저장
for term, wclass in ex_pos:
    if wclass == 'NNG' or wclass == 'NNP' or wclass == 'NP' or wclass == 'NNM':
        nouns.append(term)

print(nouns)