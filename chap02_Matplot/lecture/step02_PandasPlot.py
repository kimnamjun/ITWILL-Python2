"""
Pandas 객체에서 지원하는 시각화
object.plot(kind)
object : Series or DataFrame
kind : bar, barh, pie, hist, kde(밀도분포곡선), box, scatter
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Series 객체 시각화
ser = pd.Series(np.random.randn(10),
                index=np.arange(0, 100, 10))
print(ser)
ser.plot(color='r')


# 2. DataFrame 객체 시각화
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one','two','three','four'])
print(df)

# 기본 차트
df.plot()

# 세로 막대 차트
df.plot(kind='bar', title='bar plot')

# 가로 막대 차트
df.plot(kind='barh', title='bar plot')

# 가로 막대 차트, 누적형
df.plot(kind='barh', title='bar plot', stacked=True)

# 도수분포(히스토그램)
df.plot(kind='hist', title='hist plot')

'''
tips.csv 적용
'''
tips = pd.read_csv('../../../data/tips.csv')
print(tips)

# 요일(day) vs 파티 규모(size) 범주 확인
tips['day'].unique()
tips['size'].unique()

tab = pd.crosstab(tips['day'], tips['size'])
print(tab)

tab_result = tab.loc[:, 2:5]
print(tab_result)

tab_result.plot(kind='barh', title='day vs size columns plot', stacked=True)


# 3. 산점도 Matrix
iris = pd.read_csv('../../../data/iris.csv')

cols = list(iris.columns)
iris_x = iris[cols[:4]]

pd.plotting.scatter_matrix(iris_x)


# 4. 3d 산점도
from mpl_toolkits.mplot3d import Axes3D
col1 = iris[cols[0]]
col2 = iris[cols[1]]
col3 = iris[cols[2]]

cdata = [idx for x in iris.iloc[:,4] for idx, val in enumerate(iris.iloc[:,4].unique()) if x == val]

fig = plt.figure()
chart = fig.add_subplot(1,1,1, projection='3d')
chart.scatter(col1, col2, col3, c=cdata)
chart.set_xlabel('col1')
chart.set_ylabel('col2')
chart.set_zlabel('col3')
