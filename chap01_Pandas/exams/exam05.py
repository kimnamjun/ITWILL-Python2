'''   
문5) iris.csv 파일을 읽어와서 다음과 같이 처리하시오.
   조건1> 1~4 칼럼 대상 vector 생성(col1, col2, col3, col4)    
   조건2> 1,4 칼럼 대상 합계, 평균, 표준편차 구하기 
   조건3> 1,2 칼럼과 3,4 칼럼을 대상으로 각 df1, df2 데이터프레임 생성
   조건4> df1과 df2 칼럼 단위 결합 iris_df 데이터프레임 생성      
'''

import pandas as pd

iris = pd.read_csv('C:\\ITWILL\\4_Python-II\\data\\iris.csv')
print(iris.info())

#1
col1 = iris.iloc[:,0]
col2 = iris.iloc[:,1]
col3 = iris.iloc[:,2]
col4 = iris.iloc[:,3]

#2
sum1 = col1.sum()
avg1 = col1.mean()
std1 = col1.std()

sum4 = col4.sum()
avg4 = col4.mean()
std4 = col4.std()

#3
df1 = iris.iloc[:,0:2]
df2 = iris.iloc[:,2:4]

#4
iris_df = pd.concat([df1, df2], axis=1)
