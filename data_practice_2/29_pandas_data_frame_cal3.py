# pandas 연산과 함수
# pandas의 데이터 형식은 다양한 연산을 지원합니다.

# 영상을 보고 누락된 데이터 처리, 시리즈와 데이터 프레임의 연산과 집계 함수에 대해서 알아봅시다.

# 그리고 pandas의 데이터 프레임에 여러가지 연산을 활용하여 적용해보세요!

import numpy as np
import pandas as pd


print("A: ")
A = pd.DataFrame(np.random.randint(0, 10, (2, 2)), columns=['A', 'B'])      #칼럼이 A, B입니다.
print(A, "\n")


print("B: ")
B = pd.DataFrame(np.random.randint(0, 10, (3, 3)), columns=['B', 'A', 'C'])     #칼럼이 B, A, C입니다.
print(B, "\n")


# 아래에 다양한 연산을 자유롭게 적용해보세요.

print(A+B)

print(A.add(B, fill_value=0))

