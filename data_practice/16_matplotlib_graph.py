# 차트 설정하기
# 파이썬의 차트 라이브러리인 matploblib는 단순히 차트를 그리는 것 뿐만 아니라
# 차트에 더 많은 정보를 추가하고 보기 좋게 만드는 다양한 기능을 제공한다.

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import random

dates = ["1월 {}일".format(day) for day in range(1, 32)]
dates_num = ["{}일".format(day) for day in range(1, 32)]
temperatures = []
for i in range(31):
    x = random.randrange(0,12)
    temperatures.append(x)

print(temperatures)

pos = range(len(dates))
print(len(dates))
print(pos)

# 한국어를 보기 좋게 표시하기 위한 폰트 설정
font = fm.FontProperties(fname='./NanumBarunGothic.ttf')

# 막대의 높이가 빈도의 값이 되도록 설정
plt.bar(pos, temperatures, align='center')

# 각 막대에 해당되는 단어를 입력
plt.xticks(pos, dates_num, rotation='vertical',
f)

# 그래프의 제목 설정
plt.title('1월 중 기온 변화', fontproperties=font)

# X축에 대한 설명
plt.xlabel('일', fontproperties=font)
# Y축에 대한 설명
plt.ylabel('온도', fontproperties=font)

# 단어가 잘리지 않도록 여백 조정
plt.tight_layout()

plt.savefig('./data/16_graph.png')

