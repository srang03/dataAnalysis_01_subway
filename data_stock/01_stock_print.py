# 주식 데이터 이해하기
# 본격적으로 주식 데이터를 분석하기 전 먼저 주식 데이터의 기본적인 구조 및 정보를 확인해보도록 하겠습니다.

import pandas as pd
from datetime import datetime

# csv 형태의 주식 데이터 파일을 불러오는 코드
df = pd.read_csv('./data/stock.csv')

# 데이터 프레임 출력
# 데이터 프레임은 (행 x 열) 로 이루어진 표 형태의 특수한 데이터 타입
print(df)

# 주식 데이터 살펴 보기
print('\n 주식 데이터 형태를 출력')
print(df.shape)

print('\n주식 데이터 정보를 출력')
print(df.info)

print('\n 주식 데이터의 데이터 타입을 출력')
print(df.dtypes)

print('\n 주식 데이터의 상단 5개 행을 출력')
print(df.head())

print('\n 주식 데이터의 하단 5개 행을 출력')
print(df.tail())

print('\n 주식 데이터의 모든 열을 출력')
print(df.columns)

print('\n 주식 데이터의 요약 통계 자료 출력')
print(df.describe())