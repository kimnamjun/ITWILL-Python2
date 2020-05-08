"""
1. 축(axis) : 행축, 열축
2. 행렬곱 연산 : np.dot()
    회귀방정식 = [X * a] + b : X와 a가 행렬
    X1, X2 -> a1, a2
    model = [X1 * a1 + X2 * a2] + b
    model = np.dot(X, a) + b

    - 신경망에서 행렬곱 예
    [X * w] + b

np.dot(X, a) 전제조건
요약) 행렬 곱이 가능해야함
    1) X, a : 행렬 구조여야 함
    2) 수일치 : X 열 차수 = a 행 차수
"""
import numpy as np

# 1. 축(axis) : 행축, 열축
# 행 축 : 동일한 열의 모음 (axis=0) -> 열 단위
# 열 축 : 동일한 행의 모음 (axis=1) -> 행 단위

arr2d = np.random.randn(5, 4)

print('전체 원소 합계 :', arr2d.sum())
print('행 단위 합계 :', arr2d.sum(axis=1))
print('열 단위 합계 :', arr2d.sum(axis=0))


# 2. 행렬곱 연산 : np.dot()
X = np.array([[2,   3],
              [2.5, 3]])

a = np.array([[0.1],
              [0.5]])

b = 0.1

y_pred = np.dot(X, a) + b


# [실습] p.60
X = np.array([[0.1, 0.2],
              [0.3, 0.4]])  # (2, 2)

w = np.array([[1, 2, 3],
              [2, 3, 4]])  # (2, 3)

h = np.dot(X, w)  # (2, 3)
print(h)