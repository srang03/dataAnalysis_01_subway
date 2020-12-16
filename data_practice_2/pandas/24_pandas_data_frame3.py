# DataFrame
# 시리즈 데이터는 하나의 컬럼 값으로 이루어진 반면 데이터 프레임은 여러 개의 컬럼 값을 가질 수 있습니다.

# 이번 실습에서는 여러 개의 시리즈 데이터를 이용하여 데이터 프레임을 만드는 법을 배워봅니다.

# 오른쪽 예제에 있는 국가별 GDP 시리즈 데이터와, 
# 국가별 인구 시리즈 데이터를 이용하여 GDP와 인구 데이터를 모두 나타내는 데이터 프레임을 만들어 보세요!


# Q1.
# 국가별 인구를 나타내는 시리즈 데이터인 population과 국가별 GDP를 나타내는 시리즈 데이터인 gdp가 있습니다.
#두 시리즈 데이터로 country라는 데이터 프레임을 만드세요. 반드시 population, gdp의 순서로 만들어주셔야 합니다.

# Q2.
# country의 두 컬럼을 이용하여 새로운 컬럼을 만들고자 합니다.
# 1인당 GDP 를 나타내는 새로운 컬럼인 gdp per capita를 데이터 프레임에 추가해보세요.
# 1인당 GDP는 gdp와 population을 나누어 얻을 수 있습니다.
# 완성한 데이터 프레임을 출력해보세요

import numpy as np
import pandas as pd

# 두 개의 시리즈 데이터가 있습니다.
print("Population series data:")
population_dict = {
    'korea': 5180,
    'japan': 12718,
    'china': 141500,
    'usa': 32676
}
population = pd.Series(population_dict)
print(population, "\n")

print("GDP series data:")
gdp_dict = {
    'korea': 169320000,
    'japan': 516700000,
    'china': 1409250000,
    'usa': 2041280000,
}
gdp = pd.Series(gdp_dict)
print(gdp, "\n")


# 이곳에서 2개의 시리즈 값이 들어간 데이터프레임을 생성합니다.
print("Country DataFrame")
country = pd.DataFrame({
'population':population,
'gdp':gdp
})



# 데이터 프레임에 gdp per capita 칼럼을 추가하고 출력합니다.
gdp_per_capita = country['gdp'] / country['population']
country['gdp per capita'] = gdp_per_capita

print(country)

# 데이터 프레임을 만들었다면, index와 column도 각각 확인해보세요.
print(country.index)
print(country.columns)

