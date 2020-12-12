# 데이터 분석 이용
# CSV 데이터를 분석하기 위해 각 열의 데이터를 분리해야한다.
# 책 정보가 담긴 CSV 파일의 데이터를 , 기준으로 분리하고
# 제목(저자): 페이지 수P 형식으로 출력하는 함수를 완성하시오.

# books.csv 파일은 1열부터 제목, 저자, 장르, 페이지 수, 출판사 순서로 나열되어 있다.


import csv

def print_book_info(filename):
    with open(filename) as file:
        reader= csv.reader(file, delimiter=',')

        for row in reader:
            title = row[0]
            author = row[1]
            pages = row[3]
            print("{} ({}) : {}p".format(title, author, pages))


filename = './data/17_books.csv'
print_book_info(filename)






# CSV 데이터 읽고 처리하기
# CSV는 콤마로 나누어진 데이터 형식으로, 용량이 작고 엑셀 등의 프로그램으로 보기 좋게 표현할 수 있는 장점을 가지고 있다.
# 파이썬 내장 csv 라이브러리를 활용하여 CSV 파일을 효율 적으로 읽어올 수 있따.
# reader()는 CSV 파일의 내용을 먼저 줄 별로 나눈 뒤, 구분 기호 (delimiter)를 기준으로 분리해 주는 함수이다.

