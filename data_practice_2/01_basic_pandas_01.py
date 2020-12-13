import pandas as pd

# 코로나 엑셀 데이터 파일(.xlsx)이 저장된 경로를 설정한다.
data_path = './data/corona_data.xlsx'

# pandas를 활용하여 엑셀 파일을 불러오고 corona_data에 저장한다.
corona_data = pd.read_excel(data_path)

# corona_data 셋에서 '확진자' 데이터만 추출하여 출력한다.
confirmed = corona_data['확진자']
print(confirmed)


