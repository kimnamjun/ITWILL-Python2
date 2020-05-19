'''
문) 다음과 같은 3개의 범주를 갖는 6개의 데이터 셋을 대상으로 kNN 알고리즘을 적용하여 
      특정 품목을 분류하시오.
   (단계1 : 함수 구현  -> 단계2 : 클래스 구현)  
      
    <조건1> 데이터 셋  
    -------------------------
          품목     단맛 아삭거림 분류범주
    -------------------------
    grape   8   5     과일
    fish    2   3     단백질 
    carrot  7   10    채소
    orange  7   3     과일 
    celery  3   8     채소
    cheese  1   1     단백질 
    ------------------------
    
   <조건2> 분류 대상과 k값은 키보드 입력  
   
  <<출력 예시 1>> k=3인 경우
  -----------------------------------
    단맛 입력(1~10) : 8
    아삭거림 입력(1~10) : 4
  k값 입력(1 or 3) : 3
  -----------------------------------
  calssCount: {'과일': 2, '단백질': 1}
   분류결과: 과일
  -----------------------------------
  
  <<출력 예시 2>> k=1인 경우
  -----------------------------------
   단맛 입력(1~10) : 2
   아삭거림 입력(1~10) :3
  k값 입력(1 or 3) : 1
  -----------------------------------
  calssCount: {'단백질': 1}
   분류결과 : 단백질
  -----------------------------------
'''
import numpy as np
import matplotlib.pyplot as plt

def knn(a, b, k):
    grape = [8, 5]
    fish = [2, 3]
    carrot = [7, 10]
    orange = [7, 3]
    celery = [3, 8]
    cheese = [1, 1]
    class_category = ['과일', '단백질', '채소', '과일', '채소', '단백질']

    known = np.array([grape, fish, carrot, orange, celery, cheese])
    unknown = [a,b]

    dist = np.sqrt(((known - unknown) ** 2).sum(axis=1))
    dist = ((known - unknown) ** 2).sum(axis=1)
    print(dist)
    sort_dist = dist.argsort()

    class_result = dict()
    for i in range(k):
        key = class_category[sort_dist[i]]
        class_result[key] = class_result.get(key, 0) + 1

    # vote = max(reversed(list(class_result.items())), key=lambda x: x[1])[0]
    vote = max(class_result, key=class_result.get)
    return vote

a = int(input("단맛 입력(1~10) : "))
b = int(input("아삭거림 입력(1~10) : "))
k = int(input("k값 입력(1 or 3) : "))

print(knn(a, b, k))

# k가 1일 때와 3일 때 결과값 차이 알아보기 테스트
# for x in [1, 3]:
#     matrix = []
#     for i in range(10):
#         row = []
#         for j in range(10):
#             row.append(knn(i+1, j+1, x))
#         matrix.append(row)
#     ret = np.array(matrix)
#
#     if x == 1:
#         ret1 = np.array(matrix)
#     if x == 3:
#         ret3 = np.array(matrix)
#         print(ret3 - ret1)  # 카테고리 숫자로
