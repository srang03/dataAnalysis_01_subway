

# 집계함수 sum(), min(), max(), mean() 등을 활용하여 배열에 있는 요약 통계를 확인해 봅시다.
# 이 집계함수들은 numpy 패키지 안에 있으며, 
# 함수 안에 배열 이름을 넣으면 해당 배열의 요약 통계량을 구할 수 있습니다.



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