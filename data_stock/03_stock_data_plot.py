# 이동평균 5일선 시각화하기
# 일자에 따른 이동평균 5일선을 시각화하여 주가의 추세를 확인해보도록 하겠습니다.
# plt.plot() 명령어를 사용하고, 규칙에 따라 열 데이터를 넣으면 데이터를 선 그래프로 시각화할 수 있습니다.
# plt.plot() 명령어의 자세한 사용법은 추후 별도로 다룰 예정이므로, 시각화된 결과물이 어떻게 나타나는지를 집중적으로 확인해봅니다.



from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt


# 주식 데이터 불러오기
df = pd.read_csv('./data/stock.csv') 
print('초기 데이터 확인')
print(df)


# 주식 데이터 전처리하기(이전 문제에서 실행했던 코드)
ma5 = df['Adj Close'].rolling(window=5).mean()
ma20 = df['Adj Close'].rolling(window=20).mean()
ma60 = df['Adj Close'].rolling(window=60).mean()

df.insert(len(df.columns), "MA5", ma5)
df.insert(len(df.columns), "MA20", ma20)
df.insert(len(df.columns), "MA60", ma60)

vma5 = df['Volume'].rolling(window=5).mean()
df.insert(len(df.columns), "VMA5", vma5)


# 이동평균선의 시각화
plt.plot(df.index, df['MA5'], label = "MA5") # 이동평균선 시각화
plt.plot(df.index, df['Adj Close'], label='Adj Close') # 수정 종가 시각화


# 시각화 옵션 코드
# (시각화 강의에서 별도로 다루는 내용입니다)
plt.legend(loc='best')
plt.xticks(rotation = 45)
plt.grid()
plt.savefig("./data/plot.png")