"""
k means 알고리즘
- 비계층적(확인적) 군집분석
- 군집수(k) 알고있는 경우 이용
"""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. dataset
# test file -> numpy
def dataMat(file):
    dataset = list()  # data mat 저장
    f = open(file, mode='r')
    for line in f.readlines():
        rows = list()
        for col in line.split('\t'):
            rows.append(float(col))
        dataset.append(rows)
    return np.array(dataset)


dataset = dataMat('../../../data/testSet.txt')

# numpy -> pandas
dataset_df = pd.DataFrame(dataset, columns=['x', 'y'])
print(dataset_df)

# 2. k_means model
kmeans = KMeans(n_clusters=4, algorithm='auto')
model = kmeans.fit(dataset_df)
pred = model.predict(dataset_df)
print(pred)

# 각 클러스터의 센터
centers = model.cluster_centers_

# 3. 시각화
dataset_df['cluster'] = pred

plt.scatter(x=dataset_df['x'], y=dataset_df['y'], c=dataset_df['cluster'], marker='o')

# 중심점
plt.scatter(x=centers[:,0], y=centers[:,1], c='r', marker='d')  # red dia
plt.show()

grp = dataset_df.groupby('cluster')
print(grp.mean())