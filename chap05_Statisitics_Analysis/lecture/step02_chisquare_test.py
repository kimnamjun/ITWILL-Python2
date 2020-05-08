"""
카이제곱 검정
- 일원 카이제곱, 이원 카이제곱
"""
from scipy import stats
import numpy as np
import pandas as pd

# 1. 일원 카이제곱 검정
real_data = [4,6,17,16,8,9]  # 관측치
exp_data = [10,10,10,10,10,10]  # 기대치
chis = stats.chisquare(real_data, exp_data)
print(f'statistic = {chis[0]}, pvalue = {chis[1]}')
# chis[0] : 카이값, 기대비율,  'χ2 = Σ (관측값 - 기댓값)2 / 기댓값'

real_arr = np.array(real_data)
exp_arr = np.array(exp_data)

chis2 = sum((real_arr - exp_arr) **2 / exp_arr)  # chis2와 chis[0]과 같음


# 2. 이원 카이제곱 검정
"""
교육수준 vs 흡연유무 독립성 검정
귀무가설 : 교육수준과 흡연유무 간의 관련성이 없다.
"""
smoke = pd.read_csv("C:/ITWILL/4_Python-II/data/smoke.csv")

# DF -> vector
education = smoke['education']
smoking = smoke['smoking']

# cross table
tab = pd.crosstab(education, smoking)
print(tab)

chis = stats.chisquare(education, smoking)
print(f'statistic = {chis[0]}, pvalue = {chis[1]}')


"""
예제) 성별 vs 흡연뮤우 독립성 검정
"""
tips = pd.read_csv("C:/ITWILL/4_Python-II/data/tips.csv")

sex = tips['sex']
smoker = tips['smoker']

print(pd.crosstab(sex, smoker))

# Yes or No, Male or Female과 같이 str 타입은 안됨
# dummy 변수 생성 : 0은 들어오면 안됨
# 1 or 2로 변환 예정
sex = [1 if s == 'Male' else 2 for s in sex]
smoker = [1 if s == 'No' else 2 for s in smoker]

chis = stats.chisquare(sex, smoker)
print(f'statistic = {chis[0]}, pvalue = {chis[1]}')
