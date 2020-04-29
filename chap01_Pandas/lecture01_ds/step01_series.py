"""
step01_series.py

Series 객체 특징
- 1차원의 배열 구조
- 수학/통계 함수 제공
- 범위 수정, 블럭 연산
- indexing / slicing 기능
- 시계열 데이터 생성

Jupyter 자동완성 : Tab
Spyder 자동완성 : Ctrl + Space
"""
import pandas as pd
from pandas import Series

# 1. Series 객체 생성

# 1) list 이용
lst = [4000, 3000, 3500, 2000]
ser1 = pd.Series(lst)
print(lst)
print(ser1)
print(ser1[0])
print(ser1.index)
print(ser1.values)

ser1_2 = Series([4000, 3000, 3500, 2000], index=['a','b','c','d'])
print(ser1_2)
print(ser1_2.index)

# 2) dict 이용
person = {'name': '홍길동', 'age': 35, 'addr': '서울시'}
ser2 = Series(person)
print(person)
print(ser2)
print(ser2.index)
print(ser2.values)


# index 사용 : object[인덱스 or 조건식]
print(ser1[2])
print(ser1[ser1 >= 3000])


# 2. indexing : list 동일
ser3 = Series([4, 4.5, 6, 8, 10.5])
print(ser3[0])
print(ser3[:3])
# print(ser[-1])  / Key Error : 이거는 안 됨


# 3. Series 결합과 NA 처리
p1 = Series([400, None, 350, 200], index=['a','b','c','d'])
p2 = Series([400, 150, 350, 200], index=['a','c','d','e'])

# Series 결합
p3 = p1 + p2
# 같은 인덱스끼리 결합, 하나라도 None이면 NaN
print(p3)  # NaN 값이 들어가는 순간 int형에서 float형으로 변환됨


# 4. 결측치 처리 방법(평균, 0, 제거)
p4 = p3.fillna(p3.mean())
print(p4)

p5 = p3.fillna(0)
print(p5)

p6 = p3[pd.notnull(p3)]
print(p6)


# 5. 범위 수정, 블럭 연산
p2[1:3] = 300  # index가 숫자가 아님에도 변경 가능함
print(p2)

print(p2 + p2)
print(p2 - p2)

# broadcast 연산 # vector(1) * scalar(0)
v1 = Series([1,2,3,4])
scalar = 0.5
b = v1 * scalar
print(b)

# 수학 / 통계 함수
print(v1.sum())
print(v1.mean())
print(v1.var())
print(v1.std())
print(v1.max())

# 호출 가능한 멤버 확인
print(dir(v1))
print(v1.size)
print(v1.shape)
