# Dataframe 값으로 정렬하기!
# 데이터를 처리하다 보면 일정한 기준에 맞추어 정렬하는 일이 빈번하게 발생합니다.
# pandas에서도 데이터를 필요에 맞게 정렬할 수 있습니다.
# 이번 실습에서는 데이터 프레임에 입력되어 있는 값을 오름차순, 내림차순으로 정렬해 봅시다.

import numpy as np
import pandas as pd

print("DataFrame: ")
df = pd.DataFrame({
    'col1' : [2, 1, 9, 8, 7, 4],
    'col2' : ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col3': [0, 1, 9, 4, 2, 3],
})
print(df, "\n")


# 정렬 코드 입력해보기    
# Q1. col1을 기준으로 오름차순으로 정렬하기.
sorted_df1 = df.sort_values('col1') 
print(sorted_df1)


# Q2. col2를 기준으로 내림차순으로 정렬하기.
sorted_df2 = df.sort_values('col2', ascending=False)
print(sorted_df2)


# Q3. col2를 기준으로 오름차순으로, col1를 기준으로 내림차순으로 정렬하기.
sorted_df3 = df.sort_values(['col2', 'col1'], ascending=[True, False])
print(sorted_df3)