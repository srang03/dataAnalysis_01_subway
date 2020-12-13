# 데이터 전처리
# 데이터 전처리란 효과적인 데이터 분석 및 예측을 위해 입력되는 데이터의 형태 등을 다듬는 것을 말합니다.

# 인공지능을 사용할 때 데이터의 전처리는 가장 중요한 요소 중 하나입니다. 
# 비단 딥러닝 모델 뿐만 아니라 대부분의 머신러닝 모델에서도 데이터를 각각의 모델에 맞게 맞추어주어야 할 때가 많습니다.

# 데이터의 값이 너무 크거나 작으면 제대로 반영되지 않으며, 알고리즘의 계산 과정에서 결과값이 0으로 수렴하거나 
# 값이 너무 커져버리거나 할 수 있기 때문입니다.



# 데이터 스케일링
# 데이터 전처리에는 수많은 방법이 있지만, 이번 실습에서는 그 중 하나인 데이터 스케일링를 실행해보도록 하겠습니다.

# 예컨대 우리가 입력한 데이터 중 첫 번째 특성은 데이터의 범위가 1~8이지만, 
# 두 번째 특성은 데이터의 범위가 3000-3300이라고 생각해봅시다.

# 첫 번째 특성은 최솟값과 최댓값의 차이가 8배나 납니다. 반면 두 번째 특성의 최대값은 최솟값보다 단 10%밖에 크지 않습니다.
# 이처럼 두 번째 특성은 변화 비율이 첫 번째 특성에 비해 훨씬 작지만, 
# 절대적인 크기 변화 자체는 매우 크기 때문에 기계가 두 번째 특성의 변화폭이 더 크다고 오해할 수 있습니다. 
# 이런 문제를 해결하기 위해 각 데이터 열의 데이터의 범위를 맞추어주는 작업을 데이터 스케일링이라고 합니다.


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

pd.set_option('display.max_columns', None)


# --- 주식 데이터 불러오기(이전 실습에서 진행) --- #
df = pd.read_csv('./data/stock.csv') 

# 주가의 중간값 계산하기
high_prices = df['High'].values # 고가
low_prices = df['Low'].values # 저가
mid_prices = (high_prices + low_prices) / 2 # 고가와 저가의 중간값

# 주가 데이터에 중간 값 요소 추가하기
df['Mid'] = mid_prices # df.insert() 대신 이와 같이 사용 가능합니다.

#이동평균값 계산 및 주가 데이터에 추가하기
ma5 = df['Adj Close'].rolling(window=5).mean()
df['MA5'] = ma5

df = df.fillna(0) # 비어있는 값을 모두 0으로 바꾸기
print('전처리 전의 주가 데이터')
print(df)




# --- 데이터 전처리 --- #

# Date 열을 제거합니다.
df = df.drop('Date', axis = 1)


# 데이터 스케일링(MinMaxScaler 적용)
min_max_scaler = MinMaxScaler()
fitted = min_max_scaler.fit(df)
output = min_max_scaler.transform(df)
output = pd.DataFrame(output, columns=df.columns, index=list(df.index.values))


print('\n전처리 후의 주가 데이터')
print(output.head())




# TIP
# Min-Max Scaler(최소-최대 스케일러):
# 각 열의 데이터 중 최소값이 0, 최대값이 1이 되도록 하여, 해당 열의 모든 데이터가 0-1사이에 위치하도록 범위를 조정합니다

