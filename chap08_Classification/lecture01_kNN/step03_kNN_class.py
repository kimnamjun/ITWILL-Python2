import numpy as np
from workspace.chap08_Classification.lecture01_kNN.step01_kNN_data import data_set


class KNN_Classify:
    def knn_classify(self, known, unknown, category, k=3):
        diff = known - unknown
        square_diff = diff ** 2
        sum_square_diff = square_diff.sum(axis=1)
        distance = np.sqrt(sum_square_diff)

        sort_dist = distance.argsort()

        self.class_result = {}
        for i in range(k):
            key = category[sort_dist[i]]
            self.class_result[key] = self.class_result.get(key, 0) + 1

        return self.class_result

    def vote(self):
        vote_re = max(self.class_result)
        print("분류결과 :", vote_re)
        return vote_re


known, unknown, cate = data_set()
knn = KNN_Classify()
knn.knn_classify(known, unknown, cate)
knn.vote()