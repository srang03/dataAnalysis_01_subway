# 1차원 배열 사칙연산
# array는 +, -, *, / 에 대한 기본 연산을 지원한다.

import numpy as np

x = np.arange(4)

print(x+5)

print(x-5)

print(x*5)

print(x/5)

# 2차원 배열 사칙연산

array = np.array([1,2,3,4,5])

# Q5. array에 array2를 더한 값을 출력해보세요.    
array2 = np.array([5,4,3,2,1])
print(array + array2)


# Q6. array에 array2를 뺀 값을 출력해보세요.
print(array - array2)