# 주가 변동률 계산
# 다음 날 종가를 계산하여 새로운 데이터에 추가하고, 이를 이용해 주가 변동률을 계산할 수 있습니다.
# 변동 = 다음날 종가 - 오늘 종가

# 주가 변동률 = 변동 / 오늘 종가

from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt

# 주식 데이터 불러오기
df = pd.read_csv('./data/stock.csv') 
    

# 당일 종가가 아니라 다음 날 종가를 새로운 컬럼으로 추가하기
# shift(-1) 옵션을 사용하여 데이터를 하루씩 밀어서 삽입
df['tomorrow Adj Close']= df['Adj Close'].shift(-1)


# 주가 변동 및 변동률(%) 추가하기 - 기대 수익률 계산 가능
df['Fluctuation'] = df['tomorrow Adj Close'] - df['Adj Close'] # 주가 변동 데이터(다음날 종가 - 오늘 종가)
df['Fluctuation Rate'] = df['Fluctuation'] / df['Adj Close'] # 주가 변동률 데이터(변동 / 오늘 종가)


# 데이터 보기
print(df)

# .shift(n): 데이터를 행 단위로 n칸씩 밀어낸다는 뜻입니다. 
# 하루씩 밀어낸 종가 데이터에서 원래의 종가 데이터를 빼기 위해 사용되었습니다.