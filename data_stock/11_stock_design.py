# 딥러닝의 입력피쳐 설계
# 이번 시간부터는 본격적인 딥러닝 설계 및 적용을 위한 실습을 진행해보도록 하겠습니다.

# 딥러닝과 같은 머신러닝(인공지능) 기법을 사용하려면 우선 기계가 학습할 수 있는 모델을 만들어야 합니다.

# 이 때, 성능이 좋은 모델을 만드려면 양질의 데이터와 특성이 입력해야 합니다. 
# 예를 들어 컴퓨터에게 고양이가 무엇인지 가르쳐주려면 
# 뾰족한 귀, 큰 눈, 삐쭉한 수염과 같은 고양이에 맞는 데이터와 특성을 가르쳐주어야겠죠.

# 마찬가지로 주가 예측을 위한 딥러닝 모델에는 주가와 관련된 양질의 데이터 구조가 설계되어야 합니다. 
# 이를 입력피쳐(입력특성) 설계라고 합니다.

# 이번 실습에서는 각각의 날짜의 중간값과 중간값의 5일 이동평균 데이터(MA(5))를 입력피쳐로 만들어 데이터에 추가해보도록 하겠습니다.

# 기존에 있는 종가, 고가, 저가 데이터만 활용하더라도 어느정도 효과가 있는 모델을 만들 수 있지만, 
# 위와 같이 유의미한 특성을 적절히 추가해서 컴퓨터에게 가르쳐준다면 더 좋은 성능을 낼 수 있기 때문이죠.




from datetime import datetime #날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense, Activation

# 주식 데이터 불러오기
df = pd.read_csv('./data/stock.csv') 
print('주식 데이터 확인하기')
print(df)

# 주가의 중간값 계산하기
high_prices = df['High'].values # 고가
low_prices = df['Low'].values # 저가
mid_prices = (high_prices + low_prices) / 2 # 고가와 저가의 중간값
print('주가의 중간값:', mid_prices)

# 주가 데이터에 중간 값 요소 추가하기
df['Mid'] = mid_prices # 'Mid' 열을 새로 만들고 mid_prices 데이터를 넣습니다.
print(df)

# 종가의 이동평균값을 계산하고 및 주가 데이터에 추가합니다.
ma5 = df['Adj Close'].rolling(window=5).mean()
df['MA5'] = ma5 # 'MA5' 열을 새로 만들고 ma5 값을 넣습니다.

df = df.fillna(0) # 비어있는 값을 모두 0으로 바꾸기
print(df)