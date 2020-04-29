"""
DataFrame 모양 변경
"""
import pandas as pd

buy = pd.read_csv("../../../data/buy_data.csv")

print(buy)
print(buy.shape)  # 22, 3

# 1. row -> column(wide -> long)
buy_long = buy.stack()
print(buy_long)
print(buy_long.shape)  # 66
print(type(buy_long))
3
# 2. column -> row(long -> wide)
# stack으로 long 된 것만 가능
buy_wide = buy_long.unstack()
print(buy_wide)

# 3. 전치행렬 : (R: t()) -> (Python: .T)
wide_t = buy_wide.T
print(wide_t)

# 4. 중복 행 제거
buy_df = buy.drop_duplicates()
print(buy_df)
