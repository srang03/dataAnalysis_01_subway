import numpy as np

# 정수형 배열 생성 (int)
array_int = np.zeros(5, dtype=int)
print(array_int)

# 실수형 배열 생성 (float)
array_float = np.ones((2, 3), dtpye=float) 
print(array_float) 

# 2행 2열의 랜덤한 배열 생성 (float)
array1 = np.random.random((2,2))
print(array1)

# 평균이 0이고 표준편차가 1인 데이터를 2행 2열의 랜덤한 배열 생성
array2 = np.random.normal(0, 1, (2, 2))
print(array2)

# 0부터 10까지의 데이터를 2행 2열의 랜덤한 배열 생성
array3 = np.random.randint(0, 10, (2, 2))
print(array3)

#0부터 5사이 랜덤한 값이 담긴 3x5 array를 만들어 봅시다!
array = np.random.randint(0, 5, (3, 5))
print(array)
