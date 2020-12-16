# 이어 붙이고 나누기
# 이번에는split() 함수를 이용하여 array를 axis를 기준으로 나누어보도록 하겠습니다.
# 앞서 실습해 본 concatenate() 함수와는 달리 split() 함수는 하나의 배열과 방향을 지정하여 두 개의 배열로 나누어줍니다.

# 지시사항
# Q1. 주어진 matrix를 3번째 행에서 axis 0을 기준으로 나누고, 그 결과를 각각 a, b란 변수에 저장합시다.
# a와 b를 각각 출력해보세요.

# Q2. 주어진 matrix를 1번째 열에서 axis 1을 기준으로 나누고, 그 결과를 각각 c, d란 변수에 저장합시다.
# c와 d를 각각 출력해보세요.

import numpy as np

print("matrix")
matrix = np.array([[ 0, 1, 2, 3],
                   [ 4, 5, 6, 7],
                   [ 8, 9,10,11], 
                   [12,13,14,15]])
print(matrix, "\n")

# Q1. matrix를 [3] 행에서 axis 0으로 나누기

'''
[[0  1   2  3]
 [4  5   6  7]
 [8  9  10 11]],

 [12 13 14 15]
'''
a, b = np.split(matrix, [3], axis=0)

print(a, "\n")
print(b, "\n")


# Q2. matrix를 [1] 열에서 axis 1로 나누기
'''
[[ 0]
 [ 4]
 [ 8]
 [12]],

[[ 1  2  3]
 [ 5  6  7]
 [ 9 10 11]
 [13 14 15]]
'''

c, d = np.split(matrix, [1], axis=1)

print(c, "\n")
print(d)
