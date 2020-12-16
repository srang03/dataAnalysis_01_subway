import pandas as pd

population = pd.Series([5200, 12718, 141500, 32676], index=['Korea', 'Japan', 'China', 'USA'])

gdp_dict = {
    'Korea' : 169320000,
    'Japan' : 516700000,
    'China' : 1409250000,
    'USA' : 2041280000
}

gdp = pd.Series(gdp_dict)

country = pd.DataFrame({
    'population':population,
    'gdp':gdp
})

print(country.index)
print(country.columns)
print(country)

print(country['gdp'])
print(type(country['gdp']))

# 1인당 GDP 구하기
# 1인당 GDP = GDP / 인구
gdp_per_captia = country['gdp'] / country['population']
country['gdp per captia'] = gdp_per_captia
print(country)


country.to_csv('./data/country.csv')
country.to_excel('./data/country.xlsx')

read_file_csv = pd.read_csv('./data/country.csv')
read_file_excel = pd.read_excel('./data/country.xlsx')

print(read_file_csv)
print(read_file_excel)