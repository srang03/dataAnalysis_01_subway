# 데이터 분석 응용하기
# 트윗에 사용된 단어를 하나씩 살펴보기 위해서는 문자열을 리스트로 변환해야한다.
# trump_tweets 변수를 공백 기준으로 분리하고 리스트형으로 반환하는 break_into_words() 함수를 만들어라.

trump_tweets = "thank you to president moon of south korea for the beautiful welcoming ceremony it will always be remembered"

def break_into_words(text):
    t = text.split(' ')
    return t


print(break_into_words(trump_tweets))

# split() 메서드 사용법 
# 메서드는 특정 문자를 기준으로 문자열을 분리한다. 
# 입력값을 넣지 않을 경우 공백을 기준으로 분리한다.
# 분리된 문자열은 리스트의 원소로 저장된다.