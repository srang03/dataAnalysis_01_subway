# 인공지능으로 주가 예측해보기
# 마지막으로 학습된 모델로부터 데이터를 예측해보고, 
# 실제 주가 데이터와 예측된 결과값이 어떠한지 확인해보도록 하겠습니다.

# 지난 실습까지 하여 모델을 성공적으로 학습시켰다면, 이제는 모델을 예측하는 일만 남았습니다. 
# model.predict() 명령어 한 줄만 쓰면 끝나는 일이죠!

# 이제 model.predit()에 테스트 데이터를 넣어 주가를 예측해보도록 합시다.
 
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense, Activation


# --- 주식 데이터 로드, 전처리, 분할, 모델 학습하기(이전 실습에서 진행) --- #
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

# Keras 모델을 생성합니다.
model = Sequential()

# Keras 딥러닝 모델 학습을 위한 파라미터(옵션값)을 설정합니다.
learning_rate = 0.01
training_cnt = 1000
batch_size = 100 
input_size = 8 

# 생성된 딥러닝 모델에 학습용 데이터(train_x)를 넣습니다.
model.add(Dense(input_size, activation='tanh', input_shape=(train_x.shape[1],))) 
model.add(Dense(input_size * 3,  activation='tanh')) 
model.add(Dense(1, activation='tanh'))

# 데이터를 학습을 진행합니다.
model.compile(optimizer='sgd', loss='mse', metrics=['mae', 'mape','acc'])
model.summary()
history = model.fit(train_x, train_y, epochs=training_cnt,   
                    batch_size=batch_size, verbose=1)
val_mse, val_mae, val_mape, val_acc = model.evaluate(test_x, test_y, verbose=0)
    
    
    
# --- 학습 결과를 그래프로 확인해봅니다 --- #

# 학습된 모델로부터 테스트 데이터를 예측합니다.
pred = model.predict(test_x)

fig = plt.figure(facecolor='white', figsize=(8, 5))
ax = fig.add_subplot(111)
ax.plot(test_y, label='True') # 실제 주가
ax.plot(pred, label='Prediction') # 우리가 만든 딥러닝 모델이 예측한 주가
ax.legend()

# 현재까지 그려진 그래프를 시각화
plt.savefig("./data/plot_predict.png")




 # 예측 결과 확인하기
 # 실행해보았나요? 그리고 결과는 어떠한가요?

# 주가를 100% 동일하게 예측할 수는 없지만, 
# 우리가 만든 모델이 실제 주가와 비슷한 추세를 예측한 것을 확인할 수 있습니다.

# 우리가 학습시킨 모델은 테스트 데이터를 단 한 번도 본 적이 없다는 사실을 기억하면 놀라운 결과죠!

# 일반적으로 딥러닝 모델의 예측 성능을 더 향상 시키기 위해서는
# 1. 양질의 데이터를 입력해야 합니다.
# 2. 더 많은 데이터를 입력해야 합니다.
# 3. 입력 특성을 정교하게 설계해야 합니다.
# 4. 데이터 전처리를 다양한 방법으로 시도해야 합니다.
# 5. 모델 학습 파라미터(옵션)을 최적화해야 합니다.

# 위와 같은 방법을 통해 만들어진 딥러닝 모델은 지금도 여러 곳에서 사용되고 있으며, 
# 실제 산업에서 놀라운 결과를 가져올 때가 많습니다.

### Tips 파란색 선은 실제 주가 데이터, 주황색 선은 우리 만든 모델이 예측한 데이터를 나타냅니다.