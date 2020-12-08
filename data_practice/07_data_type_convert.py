# 데이터 분석 응용
# data.txt파일을 읽고 (단어, 빈도수) 튜플로 구성된 리스트를 반환하는 import_as_tuple() 함수를 구현하시오.
file_name = './data/06_data.txt'

def import_as_tuple(filename):
    with open(filename) as file:
        list = []
        for line in file:
            split = line.strip().split(',')
            word = split[0]
            freq = split[1]

            _tuple = (word, freq)
            list.append(_tuple)
        return list


print(import_as_tuple(file_name))

# 데이터 형태 변환하기
# 튜플(tuple)은 리스트와 비슷한 데이터 구조로, 여러 값을 모아서 저장할 수 있다.
# 리스트와 다르게 () 안에 요소가 입력되며 한 번 생성한 튜플은 값을 변경할 수 없다.
