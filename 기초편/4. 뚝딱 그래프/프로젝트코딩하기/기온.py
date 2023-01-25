import matplotlib.pyplot as plt
import pandas as pd

# 엑셀 데이터 가져오기
data = pd.read_csv('기온.csv', encoding='cp949')
year = data['일시']
low = data['최저기온']
high = data['최고기온']


# plt.plot(year, low)
plt.plot(year, high)
plt.show()