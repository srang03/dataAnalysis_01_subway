# 데이터 분석 이용하기
# 데이터가 특정 범위에 속하는 유효값인지 검증하는 함수를 Validator 함수라고 한다.
# 데이터가 특정 범위의 정수 값이 맞는지 확인하는 min_validator()와 max_validator() 함수를 구현한다.


def min_validator(minimum):
    def helper(n):
        if type(n) is not int:
            return False
        if n < minimum:
            return False
        else:
            return True
    return helper

def max_validator(maximum):
    def helper(n):
        if type(n) is not int:
            return False
        if n > maximum:
            return False
        else:
            return True
    return helper

def validate(n, validators):
    for validator in validators:
        if not validator(n):
            return False
    return True

age_validators = [min_validator(0), max_validator(120)]
ages = [-1, 0, 9, -3, 7, 11, 2020, 333, 27, 121]

print("검증 결과")
for age in ages:
    result = "유효함" if validate(age, age_validators) else "유효하지 않음"
    print("{}세 : {}".format(age, result))




# 파이썬의 함수는 함수를 리턴값으로 가질 수 있다.
# 정수, 문자열과 같은 변수를 리턴하는 방법을 배웠지만, 함수를 리턴값으로 갖는 경우가 있다.

# itemgetter() 함수가 대표적인 함수를 리턴하는 함수이다.
# itemgetter의 리턴 값은 데이터의 모음을 받아 n 번째 원소를 리턴하는 함수이다.

# 함수 내부에서 함수를 리턴하는 방법은 lambda 함수를 사용할 수 있고 def 에서도 사용이 가능하다.


