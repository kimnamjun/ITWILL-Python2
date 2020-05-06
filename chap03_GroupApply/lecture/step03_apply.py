"""
1. group 객체에 외부 함수 적용
- object.apply(func)
- object.agg([func1, func2) : aggregation(집합)

2. data 정규화
"""

import pandas as pd

# 1. group 객체에 외부 함수 적용
"""
apply vs agg
- 공통점 : 그룹 객체에 외부 함수 적용
- 차이점 : 적용할 함수의 개수 (1개 vs 여러 개)
"""

# apply()
test = pd.read_csv("../../../data/test.csv")
print(test)

grp = test['data2'].groupby(test['key'])
print(grp.size())
print(grp.sum())


# 사용자 정의 함수
def diff(grp):
    result = grp.max() - grp.min()
    return result

print(grp.apply(sum))
print(grp.apply(diff))

# agg
print(grp.agg([sum, diff]))  # 함수에 따옴표 붙여도 되고 안붙여도 됨


# 2. data 정규화 : 다양한 특징을 갖는 변수(x)를 대상으로 일정한 범위로 조정
import numpy as np

# 1) 사용자 함수 : 0 ~ 1
def normal(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x))


x = [10, 20000, -100, 0]
print(normal(x))

# 2) 자연 로그
print(np.log(x))
# [2.30258509 9.90348755        nan       -inf] : 음수 값과 0에 대한 Warning

e = np.exp(1)
print(e)  #2.718281828459045

np.log(10)  # 2.302585092994046
e ** 2.302585092994046  # 10.000000000000002

# 지수 -> 로그값
np.exp(2.302585092994046)  # 10.000000000000002

# 지수와 로그는 역함수 관계

iris = pd.read_csv("../../../data/iris.csv")
cols = list(iris.columns)

iris_x = iris[cols[:4]]
iris_x.shape  # (150, 4)
iris_x.head()

# x변수 정규화
print(iris_x.apply(normal))