# 주가, 이동평균선 시각화하기
# 이전 실습에서는 5일 이동평균선을 구해보았습니다. 이번 실습에서는 이를 응용하여 5일 이동평균선과 더불어 20일선, 60일선을 같이 시각화해보도록 하겠습니다.

# 데이터 시각화 코드 plt.plot() 여러 개를 동시에 사용하면, 여러 데이터를 하나의 시각화 자료에 동시에 겹쳐 볼 수 있습니다. 여러 지표의 전체적인 추이를 동시에 비교하여 분석할 때 유용하게 사용되는 방법입니다.


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


# 이동평균선 시각화
plt.plot(df['Adj Close'], label="Adj Close") # 수정 종가
plt.plot(df['MA5'], label="MA5") # 종가 5일 이동평균
plt.plot(df['MA20'], label="MA20") # 종가 20일 이동평균
plt.plot(df['MA60'], label="MA60") # 종가 60일 이동평균


# 시각화 옵션 코드
# (시각화 강의에서 별도로 다루는 내용입니다)
plt.legend(loc='best')
plt.grid()
plt.savefig("./data/plot_.png")