"""
scipy 패키지의 확률분포 거정
1. 정규 분포 검정 : 연속 변수의 확률 분포
    - 연속확률분포 : 정규분포, 균등분포, 카이제곱, T/Z/F 분포

2. 이항 분포 검정 : 두 가지 분포의 확률 분포
    - 이산확률분포 : 베르누이분포, 이항분포, 포아송분포
"""
from scipy import stats  # 확률분포 검정
import numpy as np
import matplotlib.pyplot as plt

# 1. 정규분포 검정
# 1) 정규분포 객체 생성
mu = 0
std = 1
std_norm = stats.norm(mu, std)

# 2) 정규분포 확률변수
N = 1000
norm_data = std_norm.rvs(N)  # 시뮬레이션 : 1000개 난수 생성

# 3) 히스토그램
plt.hist(norm_data)
plt.show()

# 4) 정규성 검정
# 귀무가설(H0) : 정규분포와 차이가 없다.
stat, pvalue = stats.shapiro(norm_data)
# (0.9975658059120178, 0.1442166566848755) : (검정 통계량,  p-value)

# 방법1) stat <= abs(1.96) : 채택역
print(f"검정통계량 : {format(stat, '.5f')}")
# 방법2) pvalue >= 0.05 : 채택역
print(f"p-value : {format(pvalue, '.5f')}")


# 2. 이항분포 검정 : 2가지(성공/실패) 범주의 확률분포 + 가설검정
"""
- 베르누이 분포 : 이항변수(성공 or 실패)에서 성공(1)이 나올 확률분포
- 이항분포 : 베르누이 분포에 시행횟수(N)을 적용한 확률분포(모수 : P, N)

ex) P = 게임에 이길 확률(40%), N = 시행횟수(100) -> 성공횟수(?)
"""
N = 100
P = 0.4

# 1) 베르누이 분포 확률변수
x = stats.bernoulli(P).rvs(N)  # 0(실패) or 1(성공)

# 2) 성공횟수
x_succ = np.count_nonzero(x)
print(x_succ)

# 3) 이항분포 검정 : 이항분포에 대한 가설검정
# 귀무가설 : 게임에 이길 확률은 40%와 다르지 않다.
pvalue = stats.binom_test(x=x_succ, n=N, p=0.4, alternative='two-sided')
print(pvalue)

if pvalue >= 0.05:
    print('게임에 이길 확률은 40%와 다르지 않다.')
else:
    print('게임에 이길 확률은 40%와 다르다고 볼 수 있다.')