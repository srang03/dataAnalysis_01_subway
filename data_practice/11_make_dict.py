# 데이터 분석 이용하기
# 사용자 번호 : 작품 번호로 이루어진 11_examfile.txt을 읽고, 사용자 번호를 키로
# 작품 번호를 값으로 하는 딕셔너리를 생성하는 make_dict() 함수를 완성하시오

_file_name = './data/11_examfile.txt'

def make_dict(filename):
    # 빈 딕셔너리 생성
    user_to_titles = {}
    with open(filename) as file:
        for line in file:
            user, title = line.strip().split(':')
            user_to_titles[user] = title
        
        return user_to_titles

print(make_dict(_file_name))

# 데이터 빠르게 탐색하기
# 딕셔너리는 키와 값이 키:값 형태로 이루어진 데이터 구조이다.
# 키와 값이 쌍으로 이루어져 있기 때문에 키 값을 이용하여 값을 빠르게 찾아낼 수 있다.
# 데이터의 수에 따라서 리스트+for과 딕셔너리의 검색 속도는 수백배까지 차이날 수 있다.