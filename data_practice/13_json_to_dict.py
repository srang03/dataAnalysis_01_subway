# 데이터 분석 이용하기
# read()와 write() 메서드를 이용하여 JSON 파일을 딕셔너리로 변환하여 리턴하는 함수
# create_dict()와, 변환된 내용을 파일에 저장하는 함수 create_json() 함수를 완성하시오.

import json

def create_dict(filename):
    with open(filename) as file:
        json_string = file.read()
        
        return json.loads(json_string)


def create_json(dictionary, filename):
    with open(filename, 'w') as file:
        file.write(json.dumps(dictionary))

src = './data/13_netflix.json'
dst = './data/new_netflix.json'

netflix_dict = create_dict(src)
print('원래 데이터 : ', str(netflix_dict))

netflix_dict['Dark Knight'] = 39217
create_json(netflix_dict, dst)
update_dict = create_dict(dst)
print('수정된 데이터 : ', str(update_dict))

# JSON 데이터 읽고 생성하기
# JSON(JavaScript Object Notation)과 파이썬의 딕셔너리는 모두 '키:값'의 쌍으로 이루어진 데이텨 형식이다.
# 파이썬의 JSON 패키지에 포함된 함수르 이용하여 두 형식을 쉽게 변환할 수 있다.

# loads() : JSON 형태의 문자열을 딕셔너리로 변환한다. 이 때 딕셔너리의 모든 원소는 문자열 타입으로 설정
# dumps() : 딕셔너리를 JSON 형태의 문자열로 변환한다.




