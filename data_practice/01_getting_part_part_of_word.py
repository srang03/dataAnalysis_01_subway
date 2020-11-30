# 데이터 분석 응용하기
# 문자열로 이루어진 text 리스트에서 k로 시작하는 문자열을 하나씩 출력하는 print_korea() 함수를 완성하시오.
trump_tweets = ['thank', 'you', 'to', 'president', 'moon', 'of', 'south', 'korea', 'for', 'the', 'beautiful', 'welcoming', 'ceremony', 'it', 'will', 'always', 'be', 'remembered']

def print_korea(text):
    for i in text:
        if i[0] == 'k':
            print(i)
        if i.startswith('k'):
            print(i)


print_korea(trump_tweets)

# startswith() 메서드를 이용하여 단어가 특정 문자열로 시작하는지 쉽게 확인이 가능하다.
# 'Naver Cafe'.startswith('Naver') > True
# 'Kakao Taxi'.startswith('Naver') > False