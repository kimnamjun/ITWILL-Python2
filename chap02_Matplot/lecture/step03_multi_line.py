"""
marker, color, line style, label
"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # 차트 격자 제공

# data 생성
data1 = np.random.randn(100) * 0.1 + 0.5  # X * std + avg
data2 = np.random.randn(100) * 0.2 + 0.7
data3 = np.random.randn(100) * 0.1 + 0.9
data4 = np.random.randn(100) * 0.3 + 0.3

fig = plt.figure(figsize=(12, 5))
chart = fig.add_subplot()

chart.plot(data1, marker='o', color='blue', linestyle='-', label='data1')
chart.plot(data2, marker='+', color='red', linestyle='--', label='data2')
chart.plot(data3, marker='*', color='green', linestyle='-.', label='data3')
chart.plot(data4, marker='s', color='yellow', linestyle=':', label='data4')
chart.set_title('Multi-line chart')
chart.set_xlabel('색인')  # 한글 추가 안했더니 깨짐
chart.set_ylabel('random number')
plt.legend(loc='best')
plt.show()