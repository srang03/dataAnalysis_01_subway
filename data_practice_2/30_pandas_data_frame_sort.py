import pandas as pd
import numpy as np

df = pd.DataFrame({
    'c1' : [2, 1, 3, 6, 5],
    'c2' : ['A', 'A', np.nan, 'D', 'C'],
    'c3' : [0, 1, 7, 2, 3]
})
print(df)

# 칼럼 c1 기준으로 데이터의 오름차순 정렬
df.sort_values('c1')

# 칼럼 c1 기준으로 데이터의 내림차순 정렬
df.sort_values('c1', ascending=False)

# 칼럼 c2와 c1을 기준으로 오름차순 정렬
# c2의 데이터에서 동일한 값 발생시 c1을 기준으로 오름차순 정렬을 의미한다.
df.sort_values(['c2', 'c1'])
