# 문자열 데이터를 조건으로 검색
# 문자열이라면 다른 방식으로도 조건 검색이 가능하다.

# 아래의 메서드들을 활용해서 해당 열의 데이터가 원하는 값인지 확인 후 맞으면 True와 틀리면 False를 출력한다.

# ① df['열 이름'].str.contains('데이터 값')
# ② df.열이름.str.match('데이터 값')
# ③ df['열이름'] == '데이터 값'




import pandas as pd

df = pd.DataFrame({
    'name': ['Tom', 'Ian', 'Kevin', 'Steve'],
    'age' : [25, 26, 23, 31]
})

print(df['name'].str.contains('Tom'))
print(df.name.str.match('Tom'))

print(df['name'] == 'Tom')