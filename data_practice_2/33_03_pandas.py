# 조건으로 검색하기
# 데이터 프레임에서, 각 컬럼마다 조건을 충족하는 값만 추출할 수 있습니다.
# Numpy의 마스킹 연산처럼 조건식을 직접 쓸 수도 있고, query() 함수를 이용하는 방법도 있습니다.
# 데이터 프레임내에서 원하는 데이터를 조건을 주어 검색하는 방법을 배우고, 실습 문제를 해결해봐요.

# 지시사항
# 예시 코드에 컬럼 A, B를 가진 2차원의 데이터프레임을 생성되어 있습니다.
# A컬럼 값이 0.5보다 작고 B컬럼 값이 0.3보다 큰 값들을 구하여 출력해보세요.
# 마스킹 연산과 query 함수를 둘 다 사용해봅시다.

import numpy as np
import pandas as pd

print("Masking & query")
df = pd.DataFrame(np.random.rand(5, 2), columns=["A", "B"])
print(df, "\n")

#데이터 프레임에서 A컬럼값이 0.5보다 작고 B컬럼 값이 0.3보다 큰값들을 구해봅시다.


print(df[(df['A'] < 0.5) & (df['B'] > 0.3)])
print(df.query('A < 0.5 and B > 0.3'))
