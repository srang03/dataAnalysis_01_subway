# book.csv 파일을 읽어서 제목의 리스트를 리턴하는 get_titles() 함수를 완성하시오.

import csv

def get_titles(books):
    with open(books) as file:
        reader = csv.reader(file, delimiter=',')

        get_title = lambda row: row[0]

        titles = map(get_title, reader)

        return list(titles)


books = './data/18_books.csv'

titles = get_titles(books)
for title in titles:
    print(title)

# map()은 데이터 구조의 각 원소들에 동일한 함수를 적용하여
# 새로운 데이터를 만드는 파이썬의 기본 함수이다.
# data라는 리스트가 주어졌을 때 아래의 두 코드는 유사한 연산한다.ArithmeticError

