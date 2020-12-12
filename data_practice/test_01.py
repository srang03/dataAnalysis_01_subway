# 트윗 분류하기
# 주어진 트럼프 대통령의 트윗 메세지를 받아서 해시태그(#), 멘션(@), 메세지로 분류하는 함수 trump_tweet(text)를 작성하시오.

# 지시사항
# trump_tweet 함수는 text를 공백을 기준으로 nn개의 문자열로 나눕니다. 각각의 나뉘어진 문자열을 아래의 규칙을 따라 분류합니다.
# 1. 각 문자열이 '#'로 시작하면 'Hashtag'로 분류하여 리스트에 저장합니다.
# 2. 각 문자열이 '@'로 시작하면 'Mention'로 분류하여 리스트에 저장합니다.
# 3. 이외의 경우는 묶어서 따로 분류하여 리스트에 저장합니다.

# 입력 예시
# trump_tweet 함수의 인자는 text로 문자열 변수가 입력됩니다.
# 이 문자열은 1개 이상의 공백과 알파벳, ‘@’, ‘#’ 으로만 구성되어 있습니다.

## Make America Great Again @Trump #Speech #White_HOuse ##

# 출력 예시
# trump_tweet 함수는 입력받은 text 변수에서 각 단어를 분류합니다.
# @와 #문자는 단어를 분류하는 과정에서 포함되지 않습니다.

## hash list : ['Speech', 'White_HOuse'] ##
## mention list : ['Trump'] ##
## text list : ['Make', 'America', 'Great', 'Again'] ##

Hashtag = []
Mention = []
texts = []

def tweeter(text):
    split = text.split(' ')

    for i in split:
        if i.startswith('#'):
            tmp = i.replace('#', '')
            Hashtag.append(tmp)

        elif i.startswith('@'):
            tmp = i.replace('@', '')
            Mention.append(tmp)
        else:
            texts.append(i)

    print('hash list :', Hashtag)
    print('mention list :', Mention)
    print('text list :', texts)

    
t = input()
tweeter(t)