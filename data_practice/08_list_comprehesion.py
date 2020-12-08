# 데이터 분석 응용하기
# 단어 모음 words에서 prefix로 시작하는 단어만 리턴하는 filter_by_prefix 함수를 구현하시오.

words = ['apple', 'banana', 'cherry', 'orange', 'melon', 'alpha', 'bravo']
prefix = 'a'

def filter_by_prefix(words, prefix):
    _list = [word for word in words if word.startswith(prefix) ]

    return _list


def reverse(word):
    return str(reversed(word))



# for문을 리스트 안에 입력하면 새로운 리스트를 코드 한 줄로 간결하게 생성할 수 있다.
