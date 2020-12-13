# 데이터셋 나누기
# 충분한 데이터를 구할 수 없을 경우, 효과적인 예측을 위해 데이터셋을 분할한 후 학습을 진행시켜야 합니다.

# 예를 들어 전체 데이터를 50:50으로 A와 B로 랜덤하게 나누어본다고 생각해봅시다. 
# 그리고 전체 데이터 중 A 데이터로만 딥러닝 모델을 학습을 시킵니다. 
# B 데이터는 전혀 사용되지 않았으므로, 이 모델은 B에 대한 아무런 정보도 가지고 있지 않습니다.

# 그런 다음 우리는 이 모델을 가지고 B 범위에 있는 데이터를 예측해봅니다. 
# 만약 우리가 성공적으로 딥러닝 모델을 학습시켰다면, 이 예측 값들은 B 데이터와 비슷하게 나타날 것입니다. 
# 반대로 모델 학습이 제대로 이루어지지 않았다면 B 데이터에 대한 예측 결과는 형편없겠죠.

# 이와 같이 데이터를 학습/테스트 용도로 나누는 것을 데이터셋 분할(split) 이라고 합니다.

# 일반적으로 전체 데이터를 일정 비율로 나눠 학습/테스트/검정용 데이터를 구성하며, 
# 이번 실습에서는 학습/테스트/검정용 데이터를 6:3:1로 나누어 진행하겠습니다.



# 독립변수와 종속변수
# 인공지능은 대개 일반적인 정보만을 활용하여 특정한 목표값을 예측하기 위해 사용합니다. 
# 이 때 일반적인 정보들을 독립변수, 목표값을 종속변수라고 합니다.

# 예컨대 아파트의 위치, 층수, 연식, 한강뷰 여부, 브랜드 등의 정보들을 가지고 매매가를 예측한다고 생각해봅시다. 
# 이 때 입력된 위치, 층수, 연식 등의 데이터가 독립변수, 목표값인 집값이 종속변수가 됩니다.

# 목표값(정답)이 있는 훈련 데이터들을 이용하여 임의의 데이터로부터 예측하고자 하는 값을 
# 올바르게 추측해내는 함수를 학습하는 방법을 지도학습(Supervised Learning)이라고 합니다.



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

# --- 주식 데이터 불러오고 전처리하기(이전 실습에서 진행) --- #
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



# --- 데이터셋 나누기 --- #


# 0~60% 지점까지를 트레인셋(학습 데이터)으로 설정(전체의 60%)
train_size = int(len(output)* 0.6) 

# 60-90% 지점까지를 테스트셋으로 설정(전체의 30%)
test_size = int(len(output)*0.3) + train_size


#train/test 학습 및 라벨 설정
#종가를 예측하기 위해 종가를 label로 설정
train_x = np.array(output[:train_size]) # 트레인셋의 독립변수
train_y = np.array(output['Close'][:train_size]) # 트레인셋의 종속변수
test_x =np.array(output[train_size:test_size]) # 테스트셋의 독립변수
test_y = np.array(output['Close'][train_size:test_size]) # 테스트셋의 종속변수
validation_x = np.array(output[test_size:]) # 트레인셋의 독립변수
validation_y = np.array(output['Close'][test_size:]) # 테스트셋의 종속변수

print('분할 전 전체 데이터의 길이: %s' % len(output))
print('학습 데이터의 길이: %s' % len(train_x))
print('테스트 데이터의 길이: %s' % len(test_x))
print('검증용 데이터의 길이: %s' % len(validation_x))