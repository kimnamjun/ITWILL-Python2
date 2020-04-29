"""
DataFrame 자료구조 특징
- 2차원 행렬구조(table 유사함)
- 열 단위 데이터 처리 용이
- Series의 모음 -> DataFrame
"""
import pandas as pd
from pandas import Series, DataFrame

# 1. DataFrame 생성

# 기본 자료구조(list, dict) 이용
name = ['hong','lee','kang','yoo']
age = [35, 45, 55, 25]
pay = [250, 350, 450, 200]
addr = ['서울','부산','대전','인천']

data = {"name": name, "age": age, "pay": pay, "addr": addr}
# columns 옵션 : 열 위치 지정
frame = pd.DataFrame(data=data, columns=['name','age','addr','pay'])
print(frame)

age = frame['age']
print(type(age))  # type: Series

# 새 컬럼 추가
gender = Series(['남','남','남','여'])
frame['gender'] = gender

# numpy 이용 : 선형대수 관련 함수
import numpy as np
frame2 = DataFrame(np.arange(12).reshape(3, 4), columns=['a','b','c','d'])
print(frame2)

# 행/열 통계
print(frame2.mean(axis=0)) # 행축 : 열단위 (기본값)
print(frame2.mean(axis=1)) # 열축 : 행단위


# 2. DataFrame 컬럼 참조
print(frame2.index)   # 행 이름
print(frame2.values)  # 값

# emp.csv
emp = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\\\emp.csv", encoding="UTF-8")
print(emp.info())

emp.head()

# 단일 컬럼 선택
print(emp['No'])
print(emp.No)  # 컬럼명에 . 포함된 경우 사용 불가

# 특정 원소 선택
print(emp.No[1])
print(emp.No[1:])

# 복수 컬럼 선택 : 중첩 리스트
print(emp[['No','Pay']])
emp[['No','Pay']].plot()


# 3. subset 만들기 : old DF = new DF

# 특정 열 선택
emp.info()
subset1 = emp[['Name','Pay']]
print(subset1)

# 특정 행 제외
subset2 = emp.drop(0)
print(subset2)

# 조건식으로 행 선택
subset3 = emp[emp['Pay'] > 350]
print(subset3)

# columns
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\iris.csv")
print(iris)

cols = list(iris.columns)
print(cols)

iris_x = cols[:4]
iris_y = cols[-1]

# x, y 변수 선택
x = iris[iris_x]
y = iris[iris_y]
x.shape  # (150, 4) : 2차원
y.shape  # (150, )  : 1차원


# 4. DataFrame 행렬 참조 : DF[row, col]

# 1) DF.loc[row, col] : 콜론 끝부분도 포함
print(emp.loc[1:3, "No":"Pay"])
print(emp.loc[1:3])
print(emp.loc[:,"No":"Name"])

# 2) DF.iloc[row, col] : (index) 콜론 끝부분 미포함
print(emp.iloc[1:3])
print(emp.iloc[1:3, :2])
print(emp.iloc[1:3, [0, 2]])  # 불연속

#######################
# DF 행렬참조 example #
#######################
iris.shape  # (150,5)

from numpy.random import choice

row_idx = choice(a=len(iris), size=int(len(iris)*0.7), replace=False)
print(row_idx)

# train dataset
train_set = iris.iloc[row_idx]
print(train_set)

# test dataset
test_idx = [i for i in range(len(iris)) if i not in row_idx]
print(test_idx)

test_set = iris.iloc[test_idx]
print(test_set)

# x, y 변수 분리
cols = list(iris.columns)
x = cols[:4]
y = cols[-1]
iris_test_x = iris.loc[test_idx, x]
iris_test_y = iris.loc[test_idx, y]
