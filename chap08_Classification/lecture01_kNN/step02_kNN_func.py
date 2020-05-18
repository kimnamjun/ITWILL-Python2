import numpy as np
from workspace.chap08_Classification.lecture01_kNN.step01_kNN_data import data_set


def knn_classify(known, unknown, category, k=3):
    # 단계 1 : 거리계산식 : 차 > 제곱 > 합 > 제곱근
    diff = known - unknown
    square_diff = diff ** 2
    sum_square_diff = square_diff.sum(axis=1)  # 행 단위 합계
    distance = np.sqrt(sum_square_diff)

    # 거리가 가까운 k개의 점 중 다수의 점과 같은 카테고리로 분류
    # k=3 일 때, 새로운 점은 {A: 1, B: 2}로 분류 -> B로 분류
    # print(distance)  # [0.47169906 0.61846584 0.20615528 0.40311289]
    # print(cate)     # ['A'        'A'        'B'        'B'       ]

    # 단계 2 : 오름차순 정렬 후 인덱싱
    sort_dist = distance.argsort()  # [2 3 0 1]

    # 단계 3 : 최근접 이웃 k개
    class_result = {}

    for i in range(k):
        key = category[sort_dist[i]]
        class_result[key] = class_result.get(key, 0) + 1

    return class_result

if __name__ == "__main__":
    known, unknown, cate = data_set()
    class_result = knn_classify(known, unknown, cate, 3)

    vote_re = max(class_result)
    print("분류 결과 :", vote_re)
