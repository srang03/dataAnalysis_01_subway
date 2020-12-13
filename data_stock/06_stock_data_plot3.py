# 변동률 시각화하기
# 주가의 변동률을 시각화해보도록 하겠습니다.

from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt


# 주식 데이터 불러오기
df = pd.read_csv('./data/stock.csv') 
print('초기 데이터 확인')
print(df)


# 주식 데이터 전처리하기(이전 문제에서 실행했던 코드)
df['tomorrow Adj Close']= df['Adj Close'].shift(-1) # 당일 종가가 아니라 다음 날 종가를 새로운 컬럼으로 추가하기
df['Fluctuation']= df['tomorrow Adj Close'] - df['Adj Close'] # 주가 변동 데이터(다음날 종가 - 오늘 종가)
df['Fluctuation Rate']= df['Fluctuation']/df['Adj Close'] # 주가 변동률 데이터(변동 / 오늘 종가)


# 변동률의 시각화
plt.figure(figsize=(12,8)) # 표현할 그래프의 크기 설정
plt.plot(df.index, df['Fluctuation Rate']) # 변동률 데이터 시각화
plt.axhline( y = 0, color = 'red', ls = '--') # 변동률 폭을 관찰하기 위한 기준 수평선 추가


# 시각화 옵션 코드
# (시각화 강의에서 별도로 다루는 내용입니다)
plt.legend(loc='best')
plt.grid()
plt.savefig("./data/plot_1.png")



# 그래프 해석
# 빨간 0 선을 기준으로 아래위로 출렁이는 변동률을 볼 수 있습니다. 
# 이와 같이 시간의 속성을 가지고 있는 데이터를 흔히 ‘시계열 데이터(Time Serise Data)’라고 부릅니다.

# 이번에는 변동률의 분포를 확인해봅시다. 시각적으로 분포를 살펴보니 -0.01과 +0.00~0.01 등락율 분포가 가장 많습니다.
#  -0.04 로 하락하거나 +0.04로 상승하는 경우는 거의 없음을 볼 수 있습니다.

# 이는 이 기업의 주가에서 급락 또는 급상승이 거의 없다는 것을 파악할 수 있습니다. 
# 삼성전자는 우리나라의 대표적인 대형주이기 때문에 변동폭이 그리 크지 않은 것으로 유추됩니다.

# 주식 투자의 단타족(단기에 높은 수익을 얻고자하는 주식투자자들을 일컫는 말입니다.)에게는 선호되지 않는 형태의 주식입니다.
