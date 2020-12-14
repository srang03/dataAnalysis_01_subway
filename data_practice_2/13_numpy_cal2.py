import numpy as np

x = np.arange(8).reshape((2,4))
print(x)

print(np.sum(x)) # 최댓값 구하기

print(np.min(x)) # 최솟값 구하기

print(np.mean(x)) # 평균 구하기

print(np.std(x)) # 표준편차 구하기

# 세로 방향으로 합 구하기
array_01 = np.sum(x, axis=0)

# 가로 방향으로 합 구하기
array_02 = np.sum(x, axis=1)

print(array_01) 
print(array_02) 