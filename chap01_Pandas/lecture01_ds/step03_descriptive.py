"""
DataFrame의 요약통계량
- 상관계수
"""
import pandas as pd

product = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\product.csv")
print(product)

# 요약 통계량
summ = product.describe()
print(summ)

# 행/열 통계
print(product.sum())
print(product.sum(axis=1))

# 산포도 : 분산, 표준편차
print(product.var())
print(product.std())

# 빈도수 : 집단변수
a_cnt = product['a'].value_counts()
print(a_cnt)
# 3    126
# 4     64
# 2     37
# 1     30
# 5      7
# Name: a, dtype: int64

# 유일값 보기
print(product['c'].unique())

# 상관관계
product.corr() # 상관계수 정방행렬


# iris dataset 적용
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\iris.csv")
iris_df = iris.iloc[:,:4]

# 변수 4개 요약 통계량
iris_df.describe()

# 상관계수 행렬
print(iris_df.corr())

# 집단변수
species = iris['Species']
species.value_counts()

print(species.unique())
