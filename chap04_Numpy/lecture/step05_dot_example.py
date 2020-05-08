"""
신경망에서 행렬곱 적용 예
- 은닉층(h) = [입력(X) * 가중치(w)] + 편향(b)
"""
import numpy as np

# 1. ANN model
# input : image(28 * 28) (gray), hidden node 32개 - > weight[?, ?]

# 2. input data : image data
X_img = np.random.randint(0, 256, size=784)

# 이미지 정규화
X_img = X_img / 255
X_img2d = X_img.reshape(28, 28)

# 3. weight data
weight = np.random.randn(28, 32)

# 4. hidden layer
hidden = np.dot(X_img2d, weight)
print(hidden)  # (28, 32)