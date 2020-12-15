import numpy as np
import pandas as pd

dataframe = pd.DataFrame(columns=['학번', '이름', '학과'])


print(type(dataframe['이름']))

print(type(dataframe[['학번', '이름', '학과']]))


## Indexing & Slicing
# 데이터 프레임의 값을 참조하기 위해 사용하는 인덱싱과 슬라이싱에는 두 가지 방법이 있습니다.
# 데이터 프레임의 인덱스의 이름으로 직접 참조하거나, 기존의 파이썬에서 배열의 인덱싱을 하는 방법 모두 사용할 수 있습니다.

# 첫번째 컬럼을 인덱스로 country.csv 파일 읽어오기.
print("Country DataFrame")
country = pd.read_csv("./data/country.csv", index_col=0)
print(country, "\n")

# 명시적 인덱싱을 사용하여 데이터프레임의 "china" 인덱스를 출력해봅시다.
print(country.loc['china',:])


# 정수 인덱싱을 사용하여 데이터프레임의 1번째부터 3번째 인덱스를 출력해봅시다.
print(country.iloc[1:4,:])

