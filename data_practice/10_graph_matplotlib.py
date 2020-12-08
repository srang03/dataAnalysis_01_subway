# 데이터 분석 응용하기
#matplotlib의 bar() 메서드를 활용하여 연도별 평균 기온 그래프를 그리시오.

import matplotlib.pyplot as plt

# 연도별 평균 기온을 설정한다.
years = [2014, 2015, 2016, 2017, 2018, 2019] # 연도 리스트
temperatures = [12, 15, 17, 18, 20, 19] # 평균 기온 리스트

# 막대 차트 출력하는 함수 구현
def draw_graph():
    # 막대 그래프의 막대 위치를 결정하는 pos를 선언한다.
    pos = range(len(years)) # [0, 1, 2, 3, 4, 5] 리스트 생성

    # 막대 그래프의 x축을 pos, y축을 temperatures로 설정하고 각 막대를 가운데 정렬한다.
    plt.bar(pos, temperatures, align='center')

    # x축의 각 막대별 연도를 표기한다.
    plt.xticks(pos, years)

    # 생성된 막대 그래프를 저장한다.
    plt.savefig('./graph/graph01.png')

# draw_graph() 함수 실행
draw_graph()
