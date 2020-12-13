# 변동률 분포 시각화하기
# 히스토그램은 대략적인 데이터의 분포를 알 수 있도록 특정 구간별로 얼마나 많은 데이터가 있는지를 나타내주는 그래프입니다. 데이터의 분포를 알면 값이 어떤 값에 치중되어 있는지, 
# 이상치(outlier)가 있는지 등을 직관적으로 파악할 수 있습니다.

# 또한, 히스토그램과 함께 커널 밀도 추정(KDE) 그래프로도 표현해보도록 하겠습니다. 지금 단계에서 커널 밀도 추정의 수학적 정의를 내리는 것은 어려우므로, 
# 히스토그램을 조금 더 부드럽게 바꾸어주는 개념 정도로 이해하시고 넘어가시면 될 것 같습니다.


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


# 히스토그램을 이용해 분포 살펴보기
df['Fluctuation Rate'].plot.hist()
plt.title('Fluctuation Rate Histogram')


# 현재까지 그려진 그래프를 보여줌
plt.savefig("./data/plot_2.png")
plt.cla() #그래프를 그린 후 초기화


# 커널 밀도함수를 이용해 분포 살펴보기
df['Fluctuation Rate'].plot.kde()
plt.title('Fluctuation Rate KDE plot')


# 현재까지 그려진 그래프를 보여줌
plt.savefig("./data/plot_3.png")

# 그래프 해석
# 이전과 마찬가지로 시각적으로 데이터의 분포를 살펴보니 -0.01과 +0.00~0.01 등락율 분포가 가장 많습니다. 
# -0.04로 하락하거나 +0.04로 상승하는 경우는 거의 없음을 볼 수 있습니다.