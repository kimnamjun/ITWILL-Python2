"""
피벗 테이블(pivot table)
- 사용자가 행, 열 그리고 교차셀에 변수를 지정하여 테이블 생성
"""
import pandas as pd

pivot_data = pd.read_csv("../../../data/pivot_data.csv")

"""
교차셀 : 매출액(price)
행 : 년도(year), 분기(quarter)
열 : 매출 규모(size)
셀에 적용할 통계 : sum
"""
ptable = pd.pivot_table(pivot_data, values='price', index=['year', 'quarter'], columns='size', aggfunc='sum')
ptable.plot(kind='barh', title='2016 vs 2017')


# movie_ration.csv
# 행 : 평가자
# 열 : 영화 제목
# 셀 : 평점
# 함수 : sum

movie = pd.read_csv("../../../data/movie_rating.csv")
ptable2 = pd.pivot_table(movie, values='rating', index='critic', columns='title', aggfunc='sum')
ptable2
