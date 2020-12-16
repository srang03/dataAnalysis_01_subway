import pandas as pd

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])

# 똑같은 인덱스끼리 연산을 진행하고 일치하지 않는 인덱스는 NaN값으로 생성된다.
print(A + B)


# 똑같은 인덱스끼리 연산을 진행하고 일치하지 않는 인덱스는 원본 데이터 그대로 생성된다.
print(A.add(B, fill_value=0))