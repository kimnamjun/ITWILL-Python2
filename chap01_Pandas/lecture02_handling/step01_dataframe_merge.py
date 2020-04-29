"""
DataFrame 병합(Merge)
"""
import pandas as pd
from pandas import Series, DataFrame

# 1. Series merge : 1차원
s1 = Series([1, 3], index=['a','b'])
s2 = Series([5, 6, 7], index=['a','b','c'])
s3 = Series([11, 13], index=['a','b'])

# 행 단위 결합 (R: rbind())
s4 = pd.concat([s1,s2,s3])
print(s4)  # 1차원

# 열 단위 결합 (R: cbind())
s5 = pd.concat([s1,s2,s3], axis=1)
print(s5)  # 2차원

# 2. DataFrame 병합 : 공통 컬럼 이용

# 병합 : 공통된 이름을 갖는 컬럼을 기준으로 병합
#      : 공통 컬럼이 없으면 Error
# 결합 : 옆에다 그냥 가져다 붙임
#      : 붙일 데이터를 리스트로 묶어야함, 축 옵션도 조심

wdbc = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\wdbc_data.csv")
wdbc

# DF1(16) + DF2(16)
cols = list(wdbc.columns)
len(cols)  # 32
DF1 = wdbc[cols[:16]]
DF2 = wdbc[cols[16:]]

# - id 컬럼 추가
wdbc_id = wdbc['id']
DF2['id'] = wdbc_id

DF_merge = pd.merge(DF1, DF2)  # 공통 이름 컬럼 기준

# 결합
DF_concat = pd.concat([DF1, DF2], axis=1)
DF_concat
