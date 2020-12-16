# 이어 붙이고 나누기
# 이번에는concatenate()함수를 이용하여 array를 서로 붙여보도록 하겠습니다.
# concatenate() 함수로 두 배열과 붙이는 방향을 설정하여 하나의 배열로 만들 수 있습니다.
# 열의 개수가 같은 array끼리는 세로(axis 0)로 붙일 수 있고, 
# 행의 개수가 같은 array끼리는 가로(axis 1)로 붙일 수 있습니다.

import numpy as np

print("matrix")
matrix = np.array([[0,1,2,3],
                   [4,5,6,7]])
print(matrix)
print("shape : ", matrix.shape, "\n")

# (아래의 배열 모양을 참고하세요.)
# Q1. matrix 두 개를 세로로 붙이기 
m = np.concatenate([matrix, matrix], axis=0)
print(m)
'''
[[0 1 2 3]
 [4 5 6 7]
 [0 1 2 3]
 [4 5 6 7]]
'''


# Q2. matrix 두 개를 가로로 붙이기
n = np.concatenate([matrix, matrix], axis=1)
print(n)
'''
[[0 1 2 3 0 1 2 3]
 [4 5 6 7 4 5 6 7]]
'''



