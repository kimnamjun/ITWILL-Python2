'''
문02) winequality-both.csv 데이터셋을 이용하여 다음과 같이 처리하시오.
   <조건1> quality, type 칼럼으로 교차분할표 작성 
   <조건2> 교차분할표를 대상으로 white 와인 내림차순 정렬       
   <조건3> red 와인과 white 와인의 quality에 대한 두 집단 평균 검정
           -> 각 집단 평균 통계량 출력
   <조건4> alcohol 칼럼과 다른 칼럼 간의 상관계수 출력  
'''

import pandas as pd
from scipy import stats
