# 새로운 데이터 만들어 삽입하기
# 주식 데이터에 들어있는 기본 데이터들을 가공하여, 이동평균, 거래량이동평균, 이격도 등을 계산하여 데이터프레임에 추가해보도록 하겠습니다.
# 종가: 해당 날짜의 마감 주가
# 이동평균: 해당 날짜 이전 N일 간의 평균치
# 이격도: 주가와 이동평균 간의 차이 비율

from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/stock.csv')

# 수정 종가 이동평균(MA : Moving Average) 값 구하기

# 수정종가 5일 이동평균
ma5 = df['Adj Close'].rolling(window=5).mean()

# 수정 종가 20일 이동평균
ma20 = df['Adj Close'].rolling(window=20).mean()

# 수정 종가 60일 이동평균
ma60 = df['Adj Close'].rolling(window=60).mean()

# df['Adj Close'] : df라는 데이터 프레임에서 'Adj Close' 열만 추출
# .rolling(windows=5) : 데이터를 5개 행씩 묶어서 계산
# .mean() : 값들의 평균을 계산한다.
# df.insert() : 데이터프레임에 새로운 열을 삽입한다.


# MA5라는 열의 이름으로 ma5 값 추가
df.insert(len(df.columns), "MA5", ma5)

# MA20라는 열의 이름으로 ma20 값 추가
df.insert(len(df.columns), "MA20", ma20)

# MA60라는 열의 이름으로 ma60 값 추가
df.insert(len(df.columns), "MA60", ma60)

# 거래량 5일 이동평균 추가
vma5 = df['Volume'].rolling(window=5).mean()
df.insert(len(df.columns), 'VMA5', vma5)

# 이격도 추가
# 수정 종가 데이터를 5일 이동평균 값으로 나눈 비율
disp5 = (df['Adj Close']/df['MA5']*100)

# 이격도 데이터를 Disp5라는 열 이름으로 추가
df.insert(len(df.columns), "Disp5", disp5)



# 데이터 확인
print('이동평균 및 이격도가 추가된 주가 데이터')
print(df)





