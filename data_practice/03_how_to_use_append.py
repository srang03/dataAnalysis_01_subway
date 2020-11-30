# 데이터 분석 응용하기
# trump_tweets 리스트에서 b로 시작하는 요소를 빈 리스트 new_list에 저장하는 make_new_list() 함수를 생성하시오.

trump_tweets = ['america', 'is', 'back', 'and', 'we', 'are', 'coming', 'back', 'bigger', 'and', 'better', 'and', 'stronger', 'than', 'ever', 'before']

def make_new_list(text):
    tmp_list = [] # 빈 tmp 리스트 생성
    for i in text:
        if i.startswith('b'): # 해당 i가 b로 시작하면 true 반환
            tmp_list.append(i)
    return tmp_list

new_list = make_new_list(trump_tweets)
print(new_list)

# 새로운 단어 추가하기
# append() 메서드는 리스트를 다룰 때 사용되는 가장 기본적인 메서드
# 리스트의 맨 마지막에 ()안의 새로운 요소를 추가한다.