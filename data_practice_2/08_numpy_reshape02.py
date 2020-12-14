# Reshape & 이어붙이고 나누기

# array의 모양을 바꿔보는 reshape()함수에 대해 배워봅시다.

# reshape()함수는 배열의 속성 중 하나인 shape를 변경할 수 있게 하는 함수입니다.

# reshape() 함수를 사용하면 1차원 배열을 2차원 배열로 바꾸거나, 2차원 배열의 열과 행의 개수를 조절할 수 있습니다.

import numpy as np

print("array")
array = np.arange(8)
print(array)
print("shape : ", array.shape, "\n")

# Q1. array를 (2,4) 크기로 reshape하여 matrix에 저장한 뒤 matrix와 그의 shape를 출력해보세요.
print("# reshape (2, 4)")
matrix = array.reshape(2,4)


print(matrix)
print("shape : ", matrix.shape)

