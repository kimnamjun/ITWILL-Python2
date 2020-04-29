'''
문1) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
    <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
    <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
    <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후  5번 칼럼으로 색상 적용 
'''

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("../../../data/iris.csv")
print(iris.info())

col1 = iris.iloc[:,0]
col3 = iris.iloc[:,2]
cdata = [idx for x in iris.iloc[:,4] for idx, val in enumerate(iris.iloc[:,4].unique()) if x == val]

# col5 = iris.iloc[:,4].unique()
# cdata = list()
# for i in iris.iloc[:,4]:
#     for idx, val in enumerate(col5):
#         if i == val:
#             cdata.append(idx)
#             break


plt.scatter(col1, col3, c=cdata)
plt.show()