"""
SVD 알고리즘 적용 - 추천 시스템

설치 : 관리자 권한으로 아나콘다 프롬프트
conda install -c conda-forge scikit-surprise

"""
import pandas as pd
from surprise import SVD, accuracy  # 모델 생성/평가
from surprise import Reader, Dataset  # Dataset 생성

# 1. 데이터 가져오기
ratings = pd.read_csv("../../../data/movie_rating.csv")

# 2. rating dataset 생성
reader = Reader(rating_scale=(1, 5))  # 평점은 1~5점 사이
dataset = Dataset(reader).load_from_df(ratings[['critic','title','rating']], reader)

# train/test
train = dataset.build_full_trainset()
test = train.build_anti_testset()

svd = SVD()
model = svd.fit(train)

# 3. 전체 사용자 대상 예측치
pred = model.test(test)  # test : 전체 사용자용, predict : 개별 사용자용(아래 참고)
print(pred)
# uid='Jack'              : 사용자
# iid='Just My'           : 영화
# r_ui=3.225806451612903  : 실제 평점
# est=3.021874398277401   : 예측치 평점

print(pd.DataFrame(pred), end='\n\n')
"""    uid        iid      r_ui       est                    details   Toby 기준
0     Jack    Just My  3.225806  3.028019  {'was_impossible': False}
1  Claudia       Lady  3.225806  3.278626  {'was_impossible': False}
2     Toby       Lady  3.225806  3.186572  {'was_impossible': False} : 추천 2위
3     Toby  The Night  3.225806  3.360705  {'was_impossible': False} : 추천 1위
4     Toby    Just My  3.225806  2.828769  {'was_impossible': False} : 추천 3위
"""

# 4. 개별 사용자 대상 예측치
user_id = 'Toby'
items_id = ['Lady', 'The Night', 'Just My']
actual_rating = 0

for item in items_id:
    print(model.predict(user_id, item, actual_rating))
