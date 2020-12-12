# 데이터 분석 활용
# books.csv 파일을 읽어서 페이지 수가 250이 넘는 책들의 제목을 리스트로 리턴하는
# get_titles_of_long_books() 함수를 완성하시오.

import csv

def get_titles_of_long_books(books):
    with open(books) as file:
        reader = csv.reader(file, delimiter=',')

        is_long = lambda row: int(row[3]) > 250
        get_title = lambda row: row[0]
        
        long_books = list(filter(is_long, reader))
        
        long_books_titles = map(get_title, long_books)

        return list(long_books_titles)



books = './data/18_books.csv'
titles = get_titles_of_long_books(books)
for title in titles:
    print(title)

# 리스트에 함수 적용하기
# filter()는 주어진 데이터 구조에서 특정 조건을 만족하는 원소만 골라내는 파이선의 기본 함수이다.


