# Series 데이터
# Series 데이터란 Numpy array가 보강된 형태로, Data와 index를 가지고 있는 데이터 형식입니다


import pandas as pd

data = pd.Series([1, 2, 3, 4])
print(data)

data = pd.Series([1, 2, 3, 4], index=['a', 'b',' c', 'd'])
print(data['b'])


# 나라별 인구 데이터를 딕셔너리 형태로 저장
population_dict = {
    'Korea' : 5200,
    'Japan' : 12718,
    'China' : 141500,
    'USA' : 32676
}

population = pd.Series(population_dict)
print(population)
print(population.values)

# country 변수로 Series 생성
country_series = pd.Series([5200, 12718, 141500, 32676], index=['Korea', 'Japan', 'China', 'USA'])
print(country_series)