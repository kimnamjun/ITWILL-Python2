"""
집단 변수 기준 자료 분석
- subset 생성
- group 객체 생성
- 시각화
"""
import pandas as pd

# 1. dataset load
wine = pd.read_csv("../../../data/winequality-both.csv")

# 컬럼명 변경 : 공백 -> '_' 교체
wine.columns = wine.columns.str.replace(' ', '_')

# 집단 변수 확인
wine['type'].unique()
wine['quality'].unique()


# 2. subset 생성

# 1) type 컬럼 : DataFrame
red_wine = wine.loc[wine['type'] == 'red']  # 열은 생략 가능

# 2) type(행) vs quality(열) : Series(1차원)
red_quality = wine.loc[wine['type'] == 'red', 'quality']
print(type(red_quality))  # Series : 변수 하나일 때는 시리즈, 리스트 형은 데이터 프레임


# 3. group 객체 생성 : 집단 변수 2개 -> 11변수 그룹화
# 형식) DF.groupby(['컬럼1','컬럼2'])
wine_grp = wine.groupby(['type','quality'])

# 각 그룹의 빈도수
print(wine_grp.size())

# 교차분할표
grp_2d = pd.crosstab(wine['type'], wine['quality'])


# 4. group 객체 시각화
import matplotlib.pyplot as plt
grp_2d.plot(kind='barh', title='type vs quality', stacked=True)


# 5. wine 종류(집단변수) vs 알콜(연속형) 통계량
wine_grp = wine.groupby('type')

wine_grp['alcohol'].describe()
