"""
계층적 군집분석
- 상향식(Bottom-Up)으로 계층적 군집을 형성
- 유클리드안 거리계산식 이용
- 숫자형 변수만 사용 가능
"""
import pandas as pd
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt

# 1. dataset load
iris = load_iris()

X = iris.data
y = iris.target

iris_df = pd.DataFrame(X, columns=iris.feature_names)
sp = pd.Series(y)
iris_df['species'] = sp
print(iris_df)

# 2. 계층적 군집분석
clusters = linkage(iris_df, method='complete', metric='euclidean')
"""
method='single'  : 단순연결
method='complete': 완전연결
method='average' : 평균연결
"""
print(clusters.shape)  # (149, 4)
print(clusters)
# 3. 덴드로그램 시각화
plt.figure(figsize=(10,5))
dendrogram(clusters, leaf_rotation=90, leaf_font_size=10)
plt.show()

# 4. 클러스터 자르기/평가 : 덴드로그램으로 판단
# 1) 클러스터 자르기
cluster = fcluster(clusters, t=3, criterion='distance')  # 거리가 3 이상 인듯
print(cluster)

# 2) DF 칼럼 추가
iris_df['cluster'] = cluster

# 3) 산점도 시각화
plt.scatter(x=iris_df['sepal length (cm)'], y=iris_df['petal length (cm)'], c=iris_df['cluster'], marker='o')
plt.show()

# 4) 관측치 vs 예측치
print(pd.crosstab(index=iris_df['species'], columns=iris_df['cluster']))

# 5) 군집별 특성분석
# DF.groupby('집단변수')
cluster_grp = iris_df.groupby('cluster')
print(cluster_grp.size())
print(cluster_grp.mean())
