"""
집단 간 평균차이 검정(t-test)
1. 한 집단 평균차이 검정 : stats.ttest_1samp
2. 두 집단 평균차이 검정 : stats.ttest_ind
3. 대응 두 집단 평균차이 검정
"""
from scipy import stats
import numpy as np
import pandas as pd

# 1. 한 집단 평균차이 검정
# 대한민국 남자 평균 키(모평균) : 175.5cm : 임의로 넣은 값
# 모집단 -> 표본 추출(30명)
sample_data = np.random.uniform(low=172, high=180, size=300)
print(sample_data)

# 기술 통계
print(sample_data.mean())

print(stats.ttest_1samp(a=sample_data, popmean=175.5))
# Ttest_1sampResult(statistic=4.044843243496199, pvalue=6.669652055110686e-05)


# 2. 두 집단 평균차이 검정
female_score = np.random.uniform(50, 100, 30)
male_score = np.random.uniform(45, 95, 30)
two_sample = stats.ttest_ind(a=female_score, b=male_score)
print(two_sample)

# csv file load
two_sample = pd.read_csv("../../../data/two_sample.csv")
print(sample_data)

sample_data = two_sample[['method','score']]
print(sample_data['method'].value_counts())

method1 = sample_data[sample_data['method'] == 1]
method2 = sample_data[sample_data['method'] == 2]

score1 = method1.score
score2 = method2.score

score1 = score1.fillna(score1.mean())
score2 = score2.fillna(score2.mean())

two_sample = stats.ttest_ind(score1, score2)
print(two_sample)


# 3. 대응 두 집단 평균차이 검정 : 복용전 65 -> 복용후 60 변환
before = np.random.randint(65, size=30) * 0.5
after = np.random.randint(60, size=30) * 0.5

paired_test = stats.ttest_rel(before, after)
print(paired_test)