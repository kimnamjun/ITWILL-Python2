"""
1. image shape : 3차원(세로, 가로, 컬러)
2. reshape
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 1. image read
file_path = "../images/test1.jpg"
image = imread(file_path)
type(image)
image.shape

print(image)
plt.imshow(image)


# RGB 색상 분류
r = image[:,:,0]  # Red
g = image[:,:,1]  # Green
b = image[:,:,2]  # Blue

# 2. image data reshape
from sklearn.datasets import load_digits  # 아나콘다에서 데이터셋 제공
digit = load_digits()
digit.DESCR  # 설명보기

X = digit.data  # x변수 (입력변수:image)
Y = digit.target  # y변수 (정답:정수)

X.shape  # (1797, 64) 64 = 8 * 8
Y.shape  # (1797,)

img_0 = X[0].reshape(8,8)
plt.imshow(img_0)

X_3d = X.reshape(-1, 8, 8)  # -1 은 전체 이미지 의미
X_3d.shape

X_4d = X_3d[:,:,:,np.newaxis]  # 4번째 축 추가
X_4d.shape  # (1797, 8, 8, 1)


# 3. reshape
"""
전치행렬 : T
swapaxis = 전치행렬
transpose() : 3차원 이상 모양 변경
"""

# 1) 전치행렬
data = np.arange(10).reshape(2, 5)

print(data.T)

# 2) transpose()
"""
1차원 : 효과 없음
2차원 : 전치행렬과 동일
3차원 : (0, 1, 2) -> (2, 1, 0) : 숫자는 축 번호
"""
arr3d = np.arange(1, 25).reshape(4, 2, 3)
arr3d.shape

# (0,1,2) -> (2,1,0)
arr3d.transpose(2,1,0)  # 숫자 지정없으면 reverse
















