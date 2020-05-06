"""
DataFrame 객체 대상 그룹화
- 형식) DF.groupby('집단변수').수학/통계함수()
"""

import pandas as pd

tips = pd.read_csv("../../../data/tips.csv")
tips.info()
print(tips)

# 팁 비율 : 파생 변수
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips)

# 변수 명 바꾸기 : 복제 후 제거
# 변수 복제
tips['gender'] = tips['sex']

# 변수 제거
del tips['sex']


# 1. 집단 변수 1개 -> 전체 컬럼 그룹화
gender_grp = tips.groupby('gender')

# 그룹객체.함수()
print(gender_grp.size())
print(gender_grp.sum())
print(gender_grp.mean())

# 그룹 별 요약 통계량
print(gender_grp.describe())
print(gender_grp.boxplot())  # pycharm에서 안보임


# 2. 집단 변수 1개 -> 특정 컬럼 그룹화
smoker_grp = tips['tip'].groupby(tips['smoker'])
print(smoker_grp.size())
print(smoker_grp.mean())


# 3. 집단 변수 2개 -> 전체 컬럼 그룹화
# 형식) DF.groupby('컬럼1','컬럼2']) 1차: 컬럼1, 2차: 컬럼2
gender_smoker_grp = tips.groupby([tips['gender'],tips['smoker']])

# 그룹 빈도수
print(gender_smoker_grp.size())

# 특정 변수 통계량
print(gender_smoker_grp.describe())
print(gender_smoker_grp['tip'].describe())


# 4. 집단 변수 2개 -> 특정 컬럼 그룹화
gender_smoker_tip_grp = tips['tip'].groupby([tips['gender'],tips['smoker']])

print(gender_smoker_tip_grp.size())
# (4,) 1차원 - vector

print(gender_smoker_tip_grp.sum())

# 1D -> 2D
grp_2d = gender_smoker_tip_grp.sum().unstack()
print(grp_2d)

# 2D -> 1D
grp_1d = grp_2d.stack()
print(grp_1d)

#############
# iris 실습 #
#############

iris = pd.read_csv("../../../data/iris.csv")
grp = iris.groupby(iris['Species'])
print(grp.sum())