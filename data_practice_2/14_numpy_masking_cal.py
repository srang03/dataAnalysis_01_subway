# 집계함수 & 마스킹연산
# 마스킹 연산은 조건식을 통해 배열에서 원하는 값을 추출할 수 있습니다.
# 집계함수와 마스킹연산은 함께 활용되는 일이 많으니 #잘 알아두셔야 합니다.

import numpy as np

matrix = np.arange(8).reshape((2, 4))
print(matrix)

# Q7. std 함수로 matrix의 표준편차를 구해 출력해보세요.
print(np.std(matrix))

# Q8. 마스킹 연산을 이용하여 matrix 중 5보다 작은 수들만 추출하여 출력해보세요.
print(matrix[matrix<5])