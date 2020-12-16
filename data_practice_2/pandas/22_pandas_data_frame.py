import pandas as pd

population = pd.Series([5200, 12718, 141500, 32676], index=['Korea', 'Japan', 'China', 'USA'])

gdp_dict = {
    'korea' : 169320000,
    'japan' : 516700000,
    'china' : 1409250000,
    'usa' : 2041280000
}

gdp = pd.Series(gdp_dict)

country = pd.DataFrame({
    'population':population,
    'gdp':gdp
})

print(country.index)
print(country.columns)

print(country['gdp'])
print(type(country['gdp']))