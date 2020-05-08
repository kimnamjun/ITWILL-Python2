"""
reshape vs resize
- reshape : 모양 변경
- resize : 크기 변경

image 크기를 120 * 150 등으로 규격화할 때 사용

image 규격화 : 실습
"""
from glob import glob  # 파일 검색 패턴 사용
from PIL import Image  # Python Image Library : image file read
import numpy as np
import matplotlib.pyplot as plt  # 이미지 시각화

path = "../images/"
file = path + "test1.jpg"

# 1개
img = Image.open(file)  # image file read
np.shape(img)  # (360, 540, 3) (세로, 가로, 색상)
plt.imshow(img)

img_re = img.resize((150, 120))  # 가로 세로 : Image 모듈과 가로 세로 방향이 다름
plt.imshow(img_re)

# PIL -> numpy
img_arr = np.asarray(img_re)
img_arr.shape

# 여러 장의 image resize 함수
def imageResize(path):
    img_h = 120
    img_w = 150
    
    image_resize = []
    
    for file in glob(path + '*.jpg'):  # 파일이 오는게 아니고 이름만 넘어 옴
        img = Image.open(file)
        img = img.resize((img_h, img_w))
        img_data = np.asarray(img)
        image_resize.append(img_data)
    
    return np.array(image_resize)

image_resize = imageResize(path)
print(image_resize)