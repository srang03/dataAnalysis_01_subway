import math
from data.data import data

def reduce_by_year(data):
    '''
    {날짜: 온도} 형식의 data 딕셔너리를 매개변수로 받아, 온도를 연도 별로 정리하여 {연도: [온도]} 형식의 딕셔너리를 반환합니다.
    
    (dict(str, float)) -> dict(int, list(float))
    
    >>> reduce_by_year({'2017-01-01': -1.3, '2017-01-02': 2.5})
    {2017: [-1.3, 2.5]}
    '''
    
    result = {}
    for date, temperature in data.items():
        year = int(date.split('-')[0])
        if year in result:
            result[year].append(temperature)
        else:
            result[year] = [temperature]
            
    return result


def average_by_year(data):
    '''
    {연도: [온도]} 형식의 딕셔너리를 매개변수로 받아, 연도 별 평균 기온을 계산하여 {연도: 온도} 형식의 딕셔너리를 반환합니다.
    
    (dict(int, list(float))) -> dict(int, float)
    
    >>> average_by_year({2017: [-1.3, 2.5]})
    {2017: 0.6}
    '''
    
    result = {}
    for year, temperatures in data.items():
        sum_temperature = 0
        for temperature in temperatures:
            sum_temperature += temperature
        result[year] = round(sum_temperature / len(temperatures), 2)
    return result

reduced = reduce_by_year(data)
print(average_by_year(reduced))