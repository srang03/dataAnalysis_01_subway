import pandas as pd;

# 코로나 데이터를 불러오기
data_path = './data/corona_data.xlsx'
corona_data = pd.read_excel(data_path)

# loc 메서드를 활용하여 7월 30일의 사망자 데이터를 추출한다.
death_0730 = corona_data.loc[corona_data['날짜'] == '2020-07-30', '사망자']
print(death_0730)