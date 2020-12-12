# 파이썬 람다함수
# def로 선언된 함수를 동일한 기능을 가진 lambda 함수로 선언한다.

# 문자열이 Boolean의 자리, 즉 if나 while의 뒤에 들어갈 경우 string이 빈 문자열이면 False, 아니면 True 값을 가진다.
# A if B else C는 B를 만족할 경우 A, 아니면 C의 값을 가진다.

def addition_(x, y):
    return x + y

addition_lambda =lambda x, y : x + y


def _first_letter(string):
    if string :
        return string[0]
    else :
        return ''


def _first_letter_1(string):
    return string[0] if string else ''

_first_letter_lambda = lambda string: string[0] if string else ''


testcase_num = [3, 10, 1, -5, 0]
for num in testcase_num:
    assert(addition_(num, num) == addition_lambda(num, num))

testcase_string = ['', 'a', 'srang_', '   a b c   ']
for string in testcase_string:
    assert(_first_letter(string) == _first_letter_lambda(string))

print("테스트 성공")
# 한 줄 함수 작성하기
# lambda는 def와 비슷하게 함수를 생성하는 연산이다. 
# 단, 함수가 이름을 갖지 않고 특정 범위에서만 적용되기 때문에 한 번만 사용되거나
# 아주 간단한 함수를 선언할 경우 사용된다.
# 그 외의 경우 def를 이용한다.
