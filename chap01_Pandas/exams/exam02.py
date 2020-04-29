'''
step02 관련문제
문2) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     단계 1 : 파일 가져오기, 정보 확인 
     단계 2 : y변수 : diagnosis 
         x변수 : id 칼럼 제외  나머지 30개 칼럼
'''
import pandas as pd

# 단계 1 : 파일 가져오기, 정보 확인 


# 단계 2 : y변수, x변수 선택

wdbc_data = pd.read_csv("C:\\ITWILL\\4_Python-II\\data\\wdbc_data.csv")
cols = list(wdbc_data.columns)
print(cols)
cols.remove('id')
cols.remove('diagnosis')
x = wdbc_data[cols]
y = wdbc_data['diagnosis']
print(x)
print(y)
