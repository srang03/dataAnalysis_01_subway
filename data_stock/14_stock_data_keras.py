# Keras를 이용한 딥러닝 수행

# 지금까지 우리는 주식 데이터 전처리를 진행해왔습니다. 
# 이제 드디어 이 데이터와 Keras라는 라이브러리로 딥러닝 모델 학습을 진행해보도록 하겠습니다.

# Keras는 최근 가장 많이 사용되는 딥러닝 라이브러리 중 하나로 딥러닝을 구현하는데 
# 필요한 많은 함수와 기능들을 가지고 있습니다.

# 많은 개발자 분들의 노력 덕분에, 
# 우리는 Keras 라이브러리를 불러오기만 하는 것으로 딥러닝을 바로 적용해볼 수 있는 것이죠.

# 러닝 모델 학습은 다음과 같이 진행됩니다.

# 1.전처리된 데이터를 준비
# 2.Keras 모델을 생성
# 3.전처리된 데이터를 Keras 모델에 입력
# 4.Keras 모델이 입력된 데이터를 학습

from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import models # Keras 라이브러리를 불러옵니다
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense, Activation

# --- 주식 데이터 로드, 전처리, 분할하기(이전 실습에서 진행) --- #
df = pd.read_csv('./data/stock.csv') 


# 주가의 중간값 계산하기
high_prices = df['High'].values
low_prices = df['Low'].values
mid_prices = (high_prices + low_prices) / 2

# 주가 데이터에 중간 값 요소 추가하기
df['Mid'] = mid_prices

# 종가의 5일 이동평균값을 계산하고 주가 데이터에 추가하기
ma5 = df['Adj Close'].rolling(window=5).mean()
df['MA5'] = ma5

df = df.fillna(0) # 비어있는 값을 모두 0으로 바꾸기

# Date 열를 제거합니다.
df = df.drop('Date', axis = 1)

# 데이터 스케일링(MinMaxScaler 적용)
min_max_scaler = MinMaxScaler()
fitted = min_max_scaler.fit(df)

output = min_max_scaler.transform(df)
output = pd.DataFrame(output, columns=df.columns, index=list(df.index.values))

# 트레인셋/테스트셋 크기 설정
train_size = int(len(output)* 0.6) # 트레인셋은 전체의 60%
test_size = int(len(output)*0.3) + train_size # 테스트셋은 전체의 30%

#train/test 학습 및 라벨 설정
#종가를 예측하기 위해 종가를 label로 설정
train_x = np.array(output[:train_size])
train_y = np.array(output['Close'][:train_size])
test_x =np.array(output[train_size:test_size])
test_y = np.array(output['Close'][train_size:test_size])
validation_x = np.array(output[test_size:])
validation_y = np.array(output['Close'][test_size:])

# TIP
# learning_rate(학습률): 학습 효율을 얼마나 좋게 할 것인지를 설정합니다. 
# 효율이 크면 좋을 것 같지만, 이 경우 모델이 특정 데이터셋만 과하게 학습하기 때문에 
# 모델이 보지 못한 새로운 데이터가 나타났을 때 제대로 예측하지 못합니다.

# training_cnt(반복횟수): 학습을 얼마나 오래 반복할 것인지를 설정합니다. 
# 일반적으로 학습을 오래 반복할 수록 성능이 좋아지지만, 그만큼 학습 시간이 길어집니다.

# batch_size(회당 학습량): 한 번에 얼마나 많은 데이터를 학습할지를 설정합니다. 
# 높을 수록 좋지만, 그만큼 더 많은 컴퓨터 성능을 요구하며 학습 속도가 느려집니다.