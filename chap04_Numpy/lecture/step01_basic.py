"""
Numpy 패키지 특징
- 선형대수(벡터, 행렬) 연산 관련 함수 제공
- list 보다 이점 : N차원 배열 생성, 선형대수 연산, 고속 처리
- Series 공통점
    -> 수학/통계 함수 지원
        ex) obj.수학/통계()
    -> 범위수정, 블럭연산
    -> indexing/slicing
- 주요 모듈과 함수
    1. random : 난수 생성 함수
    2. array : N차원 배열 생성(array([[list]]))
    3. sampling
    4. arrange : range() 유사함

https://www.scipy.org
"""
import numpy as np
import pandas as pd

lst = [1, 2, 3]

for i in lst:
    print(i ** 2)

# list -> numpy
arr = np.array(lst)
print(arr)
arr ** 2  # array([1, 4, 9], dtype=int32)

arr = np.array([1, 'two', 3])
arr  # array(['1', 'two', '3'], dtype='<U11')
arr.shape  # (1, 3)


# 1. random : 난수 생성 함수
data = np.random.randn(3, 4)  # 3행 4열

for row in data:
    print('행 단위 합계', row.sum())
    print('행 단위 평균', row.mean())

# 1) 수학과 통계 함수 지원
print(type(data))
print('전체 합계', data.sum())
print('전체 평균', data.mean())
print('전체 분산', data.var())
print('전체 표준편차', data.std())

dir(data)
print(data.shape)
print(data.size)

# 2) 범위 수정, 블럭 연산
data + data
data - data

# 3) indexing
data[0, 0] # 1행 1열
data[0, :] # 1행 전체
data[:, 1] # 2열 전체


# 2. array 함수 : N차원 배열 생성

# 1) 단일 list
lst1 = [3, 5.6, 4, 7, 8]
arr1 = np.array(lst1)
arr1.var()
arr1.std()

# 2) 중첩 list
lst2 = [[1,2,3,4,5],[2,3,4,5,6]]
arr2 = np.array(lst2)
print(arr2)

# index : obj[행 index, 열 index]
arr2[1, :]  # 2행 전체
arr2[:, 1]  # 2열 전체
arr2[:,2:4]  # box 선택

# broadcast 연산
# - 작은 차원이 큰 차원으로 늘어난 후 연산

# 1) scalar vs vector
arr1 * 0.5

# 2) scalar vs matrix
arr2 * 0.5

# 3) vector vs matrix
print(arr1.shape)  # (5, )
print(arr2.shape)  # (2, 5)
arr3 = arr1 + arr2
print(arr3)

# 3. sampling 함수
num = list(range(1, 11))
idx = np.random.choice(a=len(num), size=5, replace=False)
"""
a : 관측치 길이
size : 임의 추출 크기
replace : 복원(기본, True) or 비복원
p : 확률
"""

score = pd.read_csv("C://ITWILL/4_Python-II/data/score_iq.csv")
idx = np.random.choice(a=len(score), size=int(len(score) * 0.3), replace=False)

score_train = score.iloc[idx, :]  # DataFrame Index

# pandas(dataframe) -> numpy(array)
score_arr = np.array(score)
score_train2 = score_arr[idx]

# 4. arragne 함수
zero_arr = np.zeros((3,5))

cnt = 1
for i in np.arange(3):  # 행 인덱스
    for j in range(5):  # 열 인덱스
        zero_arr[i, j] = cnt
        cnt += 1
# range와 np.arange는 기능이 비슷
# np.arange는 값의 범위에 실수도 가능