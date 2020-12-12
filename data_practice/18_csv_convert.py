# 데이터 분석 이용하기
# CSV는 파일의 크기가 작다는 장점을 가지고 있지만 상황에 따라서 JSON 같은 다른 형식으로 변환하여 주고 받아야 한다.
# 책 데이터를 JSON 형식으로 변환하여 저장하는 book_to_json() 함수를 완성하시오.

# books.csv 파일은 1열부터 제목, 작가의 이름, 장르, 페이지 수, 출판사 데이터를 저장하고 있다.
# 이파일을 JSON 형식으로 변환하여 book.json 파일에 저장하시오.
# (페이지 수는 문자열이 아니라 정수이다.)


import csv
import json

def book_to_json(src_file, dsc_file):
    books = []
    with open(src_file) as file:
        reader = csv.reader(file, delimiter=',')

        for row in reader:
            book = {
                'title':row[0],
                'author' : row[1],
                'genre': row[2],
                'pages': int(row[3]),
                'publisher': row[4]
            }
            books.append(book)
    with open(dsc_file, 'w') as dst:
        json_string = json.dumps(books)
        dst.write(json_string)


src_file = './data/18_books.csv'
dst_file = './data/18_books.json'

book_to_json(src_file, dst_file)


# CSV 데이터의 각 열은 고유한 의미를 갖는다.
# 책 데이터를 CSV 형식으로 저장한다면 각 열은 제목, 작가, 페이지 수 등의 의미를 가지게 된다.
# 이 성질을 이용하면 CSV 데이터를 JSON으로 변환할 수 있다.

