# 영어 단어 빈도수 찾기
# corpus.txt 파일은 특정 문서를 분석한 결과, 발견되는 모든 영어단어와 그 빈도를 저장한 문서입니다.
# corpus.txt 파일에는 영어 단어와 해당 단어의 빈도수가 각각 /(슬래쉬)를 기준으로 나뉘어져 쓰여져있습니다.
# 이 파일에서, 주어진 text로 시작하는 모든 단어와 그 빈도를 출력하는 기능을 하는 함수 filter_by_text(text)를 구현하세요.


# 지시사항
# 1. corpus.txt에 있는 모든 단어와 빈도수를 tuple의 형태로 리스트corpus에 추가합니다.
# 2. 리스트 corpus 에 저장된 데이터 중에서 text변수의 문자열로 시작하는 단어만을 추려 리스트 result에 저장합니다.
# 3. 리스트 result 에 저장된 데이터를 빈도수를 기준으로 내림차순 정렬하여 20개까지 출력합니다. 데이터가 20개 미만일 경우 모두 출력합니다.

# 입력 예시
#filter_by_text 함수는 영어 알파벳으로만 이루어진 문자열 text를 인자로 가집니다.
### a 

# 출력 예시
# filter_by_text 함수는 corpus.txt에 있는 데이터 중에서 입력받은 text로 시작하는 모든 단어 중, 빈도수가 높은 상위 20개의 단어와 빈도수를 출력합니다.
# [('and', 2682878), ('a', 2150885), ('as', 517788), ('at', 478178), ('are', 470949), ('an', 344046), ('all', 262447), ('about', 197116), ('also', 124885), ('any', 124108), ('after', 117138), ('another', 58188), ('again', 56231), ('against', 56208), ('always', 46228), ('around', 45286), ('although', 43637), ('away', 38747), ('area', 35144), ('already', 34292)]


def filter_by_text(text) :
    # 주어진 규칙에 맞추어 filter_by_text()함수를 구현해주세요.
    # corpus.txt에 있는 텍스트를 읽어와서 corpus라는 리스트에 추가한다.
    text_file = './data/corpus.txt'
    with open(text_file) as file:
        corpus = []
        for i in file:
            split = i.strip().split('/')
            tmp = (split[0], int(split[1]))
            corpus.append(tmp)


#     # corpus에 있는 데이터 중, text로 시작하는 단어만을 추려서 result라는 리스트에 저장한다.

        result = [word for word in corpus if word[0].startswith(text)]


#     # 찾은 영어 단어를 빈도수를 기준으로 내림차순으로 정렬하여 20개만 출력한다.

        sorted_by_words = sorted(result, key=lambda x: x[1], reverse=True)
        words = []
        count = 0
        for i in sorted_by_words :
            count = count + 1 
            words.append(i)
            if count == 20:
                break
        print(words)

# 아래 부분은 수정하지 마세요!
# 입력과 출력을 수행하는 코드입니다.
t = input()
filter_by_text(t)