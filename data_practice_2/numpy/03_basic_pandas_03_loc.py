import pandas as pd

# 코로나 데이터 불러오기
data_path = './data/corona_data.xlsx'

corona_data = pd.read_excel(data_path)

# 확진자가 10000명 이상인 모든 데이터를 추출한다.
over_10000 = corona_data.loc[corona_data['확진자'] >= 10000, :]
print(over_10000)