# 데이터 분석 응용하기
# 데이터 분석하기 위해서 저장된 파일을 파이썬으로 읽는 작업이 필요하다.
# 파일의 내용을 각 라인의 번호와 함께 출력하는 print_lines() 함수를 작성하시오.

file_name = './data/06_data.txt'
def print_lines(filename):
    with open(filename) as file:
        line_number = 1
        for line in file:
            print(line_number, line)
            line_number += 1

print_lines(file_name)

# open() 함수를 이용하면 지정한 파일 이름에 해당하는 파일을 열고, 읽거나 수정할 수 있다.
# with ~ as를 사용하면 파일을 자동으로 닫을 수 있고, 반복문을 이용하여 파일의 내용을 한 줄씩 읽을 수 있다.
