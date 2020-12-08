# 데이터 분석 응용하기
# 단어의 사용 빈도수를 쉽게 확인하기 위해서는 단어를 빈도 순서대로 정렬해야 한다.
# get_freq() 함수와 sort_by_frequency() 함수를 구현하시오.

# get_freq() : (단어, 빈도수)의 쌍으로 이루어진 튜플을 인자로 받아, 빈도수를 리턴한다.
# sort_by_frequency() : (단어, 빈도수)의 원소로 이루어진 리스트를 인자로 받아, 빈도수가 낮은 순서대로 정렬하여 리턴한다.

pairs = [('a',5),('c',10),('b',13),('f',1),('k',3)]

def get_freq(pair):
    freq = pair[1]
    return freq

def sort_by_frequency(pairs):
    sort_by_freq = sorted(pairs, key=get_freq)
    return sort_by_freq

print(sort_by_frequency(pairs))

# sorted()를 활용하면 리스트를 특정 기준에 맞춰서 정렬할 수 있다.
# 정렬기준은 key에 저장한 함수를 따르게 된다.
