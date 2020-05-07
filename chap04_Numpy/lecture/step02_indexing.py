"""
indexing / slicing
- 1차원 indexing : list 동일함
- 2, 3차원 indexing
- boolean indexing
"""
import numpy as np

# 1. indexing
"""
1차원 : obj[index]
2차원 : obj[행 index, 열 index]
3차원 : obj[면 index, 행 index, 열 index]
"""

# 1) list 객체
ldata = [0,1,2,3,4,5]
ldata[:]
ldata[2:]
ldata[:3]
ldata[-1]

# 2) numpy 객체
arr1d = np.array(ldata)
arr1d.shape
arr1d[2:]
arr1d[:3]
arr1d[-1]


# 2. slicing
arr = np.array(range(1, 11))

arr_s1 = arr[4:8]
arr_s1[:] = 50  # 블럭 수정


# 2, 3차원 indexing
arr2d = np.array([[1,2,3],[2,3,4],[3,4,5]])

# 행 index : default
arr2d[1]  # [2,3,4]
arr2d[:,1:]

# [면, 행, 열]
arr3d = np.array([ [ [1,2,3], [4,5,6], [7,8,9] ],
                   [ [10,11,12], [13,14,15], [16,17,18] ] ])
print(arr3d)
arr3d[0]  # 1면

arr3d[0, 2]  # 면 -> 행 index

arr3d[1, 2, 2]  # 면 -> 행 -> 열 index

print(arr3d[1,1:,1:])  # box


# 4. boolean indexing : 조건 인덱싱
dataset = np.random.randint(1, 10, size=100)

dataset2 = dataset[dataset >= 5]
print(dataset2)

# 이런건 안됨
# dataset[5 <= dataset and dataset <= 8]
# dataset[5 <= dataset <= 8]
print(dataset[np.logical_and(5 <= dataset, dataset <= 8)])
# np.logical_and, or, not, xor