"""
1. csv file read
2. csv file write
3. random sampling
"""
import pandas as pd

# 1. csv file read
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\iris.csv")

# 컬럼명 : 특수문자 or 공백 -> _ 문자 변경
iris.columns = iris.columns.str.replace('.','_')
print(iris.head())

print(iris.Sepal_Length)

# 컬럼명이 없는 경우
st = pd.read_csv('C:\\ITWILL\\4_Python-II\\data\\student.csv', header=None)
print(st)

col_names = ['학번','이름','키','몸무게']
st.columns = col_names
print(st)

# 행 이름 변경
# st.index = ['A','B','C','D']

# 비만도 지수(BMI)
# BMI = 몸무게(kg) / 키(m) ** 2
BMI = [st.loc[i,'몸무게'] / (st.loc[i,'키'] * 0.01) ** 2 for i in range(len(st))]
st['BMI'] = BMI
st['BMI'] = st['BMI'].round(2)
print(st)


# 2. csv file write
st.to_csv("C:\\ITWILL\\4_Python-II\\data\\student_df.csv", index=None, encoding="UTF-8")


# 3. random sampling
wdbc = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\wdbc_data.csv")
print(wdbc)

wdbc_train = wdbc.sample(400)
wdbc_train.head()
