# 브로드캐스팅
# Numpy로 생성한 배열의 크기가 다를 경우 연산을 하게 되면 결과가 어떻게 출력될까요?
# 이럴경우 Numpy에서는 브로드캐스팅이라는 연산 방식으로 처리합니다.
# 두 배열의 변수 이름은 각각 A, B 여야 합니다import numpy as np

import numpy as np
'''
[[0]
 [1]
 [2]
 [3]
 [4]
 [5]] 배열 A와

 [0 1 2 3 4 5] 배열 B를 선언하고, 덧셈 연산해보세요.
'''

A = np.arange(6).reshape(6,1)

B = np.arange(6)

print(A+B)