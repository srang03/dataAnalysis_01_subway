# 데이터 분석 응용하기
# trump_tweets 리스트의 문자열 요소에서 쉼표, 작은 따옴표, 느낌표를 제거하는
# remove_special_characters() 함수를 생성하시오.

trump_tweets = [
    "i hope everyone is having a great christmas, then tomorrow it’s back to work in order to make america great again.",
    "7 of 10 americans prefer 'merry christmas' over 'happy holidays'.",
    "merry christmas!!!",
]


def remove_special_characters(text):
    processed_text = []

    for i in text:
        i = i.replace(',','').replace('!','').replace('\'','')
        processed_text.append(i)
    return processed_text


print('\n'.join(remove_special_characters(trump_tweets)))
# 특수 기호 삭제하기
# replace() 메서드는 문자열에서 특정 문자나 문자열을 다른 문자(열)로 변경할 때 사용된다.
# replace()는 변경하고 싶은 문자열을 첫 번째 입력값으로, 대체할 문자열을 두 번째 입력값으로 받는다.

print('안녕하세요!!'.replace('!!','.'))
print('/* Hello */'.replace('/','').replace('*','').replace(' ', ''))

