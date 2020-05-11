'''
문02) winequality-both.csv 데이터셋을 이용하여 다음과 같이 처리하시오.
   <조건1> quality, type 칼럼으로 교차분할표 작성 
   <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬       
   <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정
           -> 각 집단 평균 통계량 출력
   <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력  
'''

import pandas as pd
from scipy import stats

wine = pd.read_csv('../../../data/winequality-both.csv')

# no1
tab = pd.crosstab(wine['quality'], wine['type'])
print(tab)
print('\n'+'-'*80+'\n')

# no2
tab = tab.sort_values('white', ascending=False)
print(tab)
print('\n'+'-'*80+'\n')

# no3
red = wine[wine['type'] == 'red']
red_quality = red['quality']
white = wine[wine['type'] == 'white']
white_quality = white['quality']

quality_ttest = stats.ttest_ind(red_quality, white_quality)
print(quality_ttest)
print('\n'+'-'*80+'\n')

# no4
# cols = list(wine.columns.unique())
# cols.remove('alcohol')
# cols.remove('type')
# print(cols)
#
# X = wine.loc[:,cols]
# Y = wine.loc[:,'alcohol']
# print(X)
#
# for x in X:
#     print(f"{x}와 alcohol 간의 상관계수 : {X[x].corr(Y)}")
print(wine.corr()['alcohol'])