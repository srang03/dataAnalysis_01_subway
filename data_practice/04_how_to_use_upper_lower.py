# 데이터 분석 응용하기
# trump_tweets 리스트의 문자열 요소를 모두 소문자로 변환하는 lowercase_all_characters() 함수를 완성하시오.

trump_tweets = [
    "FAKE NEWS - A TOTAL POLITICAL WITCH HUNT!",
    "Any negative polls are fake news, just like the CNN, ABC, NBC polls in the election.",
    "The Fake News media is officially out of control.",
]

def lowercase_all_characters(text):
    tmp_list = []
    for i in text:
        tmp_list.append(i.lower())

    return tmp_list


print('\n'.join(lowercase_all_characters(trump_tweets)))


# 대소문자 변환하기
# lower(), upper() 메서드를 활용하면 문자열을 쉽게 소문자 또는 대문자로 변환할 수 있다.
